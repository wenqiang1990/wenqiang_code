#coding=utf-8
import smtplib
from email.mime.text import MIMEText
import unittest
import HTMLTestRunner
import time,os

#=============定义发送邮件==========
def send_mail(file_new):
    #发信邮箱
    mail_from='13366778604@189.cn'
    mail_to=['wenqiang@xiaojiuwo.cn']#收件箱
    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    #定义标题
    msg['Subject']=u"自动化测试报告"
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
    #连接 SMTP 服务器，此处用的 189 的 SMTP 服务器
    smtp.connect('smtp.189.cn')
    #用户名密码
    smtp.login('13366778604@189.cn','121518abc')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print 'email has send out !'
#======查找测试报告目录，找到最新生成的测试报告文件====
def send_report(testreport):
    result_dir = testreport
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
    #print (u'最新测试生成的报告： '+lists[-1])
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-1])
    print file_new
    #调用发邮件模块
    send_mail(file_new)

#================将用例添加到测试套件===========    
def creatsuite():
    #测试套件
    testunit = unittest.TestSuite()
    #定义测试文件查找的目录
    test_dir='D:\\workspace\\zidonghua'
    #定义 discover 方法的参数
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py',
                                                 top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_case in discover:
    #for test_case in test_suite:   
    #for test_case in discover:
        testunit.addTests(test_case)
        print test_case
    return testunit

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    testreport = 'D:\\selenium_test\\report\\'
    filename = testreport+now+'result.html'
    fp = file(filename, 'wb')
    #定义测试报告
    runner =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'如风达官网冒烟测试报告',
        description=u'用例执行情况：')
    
    alltestnames = creatsuite()
    runner.run(alltestnames)
    fp.close()
    send_report(testreport) #发送报告





    
