# -*- coding: utf-8 -*-
import xlrd,json,sys
import ConfigParser,os
import logging,os
import hashlib
import smtplib
from email.mime.text import MIMEText
import requests
import xlrd,hashlib,json,os,logging,sys,hashlib,smtplib,re


#通过自带的ConfigParser模块，读取邮件发送的配置文件，作为字典返回
def get_conf():
    conf_file = ConfigParser.ConfigParser()

    conf_file.read(os.path.join(os.getcwd(),'conf.ini'))

    conf = {}

    conf['sender'] = conf_file.get("email","sender")

    conf['receiver'] = conf_file.get("email","receiver")

    conf['smtpserver'] = conf_file.get("email","smtpserver")

    conf['username'] = conf_file.get("email","username")

    conf['password'] = conf_file.get("email","password") 

    return conf

#此处使用python自带的logging模块，用来作为测试日志，记录测试中系统产生的信息。

log_file = os.path.join(os.getcwd(),'log/sas.log')
log_format = '[%(asctime)s] [%(levelname)s] %(message)s'     #配置log格式
logging.basicConfig(format=log_format, filename=log_file, filemode='w', level=logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(log_format)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)



def runTest(testCaseFile):
    testCaseFile = './TestCase/testcase.xlsx'
    testCaseFile = os.path.join(os.getcwd(),testCaseFile)
    if not os.path.exists(testCaseFile):
        logging.error('测试用例文件不存在！')
        sys.exit()
    testCase = xlrd.open_workbook(testCaseFile)
    table = testCase.sheet_by_index(0)
    errorCase = []                #用于保存接口返回的内容和HTTP状态码

    s = None
    for i in range(1,table.nrows):
        if table.cell(i, 9).value.replace('\n','').replace('\r','') != 'Yes':
            continue
        num = str(int(table.cell(i, 0).value)).replace('\n','').replace('\r','')
        api_purpose = table.cell(i, 1).value.replace('\n','').replace('\r','')
        api_host = table.cell(i, 2).value.replace('\n','').replace('\r','')
        request_url = table.cell(i, 3).value.replace('\n','').replace('\r','')
        request_method = table.cell(i, 4).value.replace('\n','').replace('\r','')
        request_data_type = table.cell(i, 5).value.replace('\n','').replace('\r','')
        request_data = table.cell(i, 6).value.replace('\n','').replace('\r','')
        encryption = table.cell(i, 7).value.replace('\n','').replace('\r','')
        check_point = table.cell(i, 8).value

        if encryption == 'MD5':              #如果数据采用md5加密，便先将数据加密
            request_data = json.loads(request_data)
            print request_data
            request_data['Password'] = md5Encode(request_data['Password'])
            print request_data['Password']
            
        status, resp ,s = interfaceTest(num, api_purpose, api_host, request_url, request_method, request_data_type, request_data, check_point, s)
        if status != 200 or check_point not in resp:            #如果状态码不为200或者返回值中没有检查点的内容，那么证明接口产生错误，保存错误信息。
            errorCase.append((num + ' ' + api_purpose, str(status), 'http://'+api_host+request_url, resp))
    return errorCase


#接受runTest的传参，利用requests构造HTTP请求

def interfaceTest(num, api_purpose, api_host, request_url, request_method, request_data_type, request_data, check_point, s):
    headers = {'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
                      'X-Requested-With' : 'XMLHttpRequest',
                      'Connection' : 'keep-alive',
                      'Referer' : 'http://' + api_host,
                      'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}

    if s == None:
        s = requests.session()
    if request_method == 'POST':
        if request_url != '/login' :
            r = requests.post(url= api_host+request_url, data = request_data, headers = headers)         #由于此处数据没有经过加密，所以需要把Json格式字符串解码转换成**Python对象**
            print r.json
        elif request_url == '/login' :
            s = requests.session()
            r = requests.post(url='http://'+api_host+request_url, data = request_data, headers = headers)          #由于登录密码不能明文传输，采用MD5加密，在之前的代码中已经进行过json.loads()转换，所以此处不需要解码
    else:
        logging.error(num + ' ' + api_purpose + '  HTTP请求方法错误，请确认[Request Method]字段是否正确！！！')
        s = None
        return 400, s
    status = r.status_code
    resp = r.text
    print resp
    if status == 200 :
        if re.search(check_point, str(r.text)):
            logging.info(num + ' ' + api_purpose + ' 成功，' + str(status) + ', ' + str(r.text))
            return status, resp, s
        else:
            logging.error(num + ' ' + api_purpose + ' 失败！！！，[' + str(status) + '], ' + str(r.text))
            return 200, resp , None
    else:
            logging.error(num + ' ' + api_purpose + '  失败！！！，[' + str(status) + '],' + str(r.text))
            return status, resp.decode('utf-8'), None



def md5Encode(data):
    hashobj = hashlib.md5()
    hashobj.update(data.encode('utf-8'))
    return hashobj.hexdigest()

def sendMail(text):
    mail_info = get_conf()
    sender = mail_info['sender']
    receiver = mail_info['receiver']
    subject = '[AutomationTest]接口自动化测试报告通知'
    smtpserver = mail_info['smtpserver']
    username = mail_info['username']
    password = mail_info['password']
    msg = MIMEText(text,'html','utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ''.join(receiver)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


def main():
    errorTest = runTest('TestCase/TestCase.xlsx')
    if len(errorTest) > 0:
        html = '<html><body>接口自动化扫描，共有 ' + str(len(errorTest)) + ' 个异常接口，列表如下：' + '</p><table><tr><th style="width:100px;text-align:left">接口</th><th style="width:50px;text-align:left">状态</th><th style="width:200px;text-align:left">接口地址</th><th   style="text-align:left">接口返回值</th></tr>'
        for test in errorTest:
            html = html + '<tr><td style="text-align:left">' + test[0] + '</td><td style="text-align:left">' + test[1] + '</td><td style="text-align:left">' + test[2] + '</td><td style="text-align:left">' + test[3] + '</td></tr>'
            sendMail(html)

if __name__ == '__main__':
    main()