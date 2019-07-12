#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#发送邮箱
sender = '13366778604@189.cn'
#接收邮箱
receiver = 'wenqiang@xiaojiuwo.cn'
#发送邮箱服务器
smtpserver = 'smtp.189.cn'
#发送邮箱用户/密码
username = '13366778604@189.cn'
password = '121518abc'

msgRoot = MIMEMultipart('related')
#邮件主题
msgRoot['Subject'] = 'Python email test'

#构造附件
att = MIMEText(open('D:\\selenium_test\\report\\log.txt', 'rb').read(), 'base64',
'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="log.txt"'
msgRoot.attach(att)
smtp = smtplib.SMTP()
smtp.connect('smtp.189.cn')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
