# -*- coding: utf-8 -*-
import base64
import hashlib

def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

mch_id='100000000000019'
channel_id='29'
channel_name ='广发银企直连-博裕'
out_trade_no='c349a7507a395e174a4fba153900eae9'
trade_no='91029154408446299168'
status='-1'
tri_trade_no= '2018120616225990'
time_start= '0000-00-00 00:00:00'
time_end='2018-12-06 16:22:59'
err_msg='测试模拟'
err_code=''
payer_name= '博裕融资租赁（天津）有限公司 '
payer_card_no= '9550880209469900147'
amount='500000'
secret='88bceeb2d5b91d06da677afe2416dd51'

#distance = {'mch_id':100000000000019,'channel_id':2,'channel_name':广发银企直连-博裕,'out_trade_no':c349a7507a395e174a4fba153900eae9,'trade_no':91029154408446299168,'status':-1,'tri_trade_no':2018120616225990,'time_start':0000-00-00 00:00:00,'time_end':2018-12-06 16:22:59,'err_msg':测试模拟,'err_code':'','payer_name':博裕融资租赁（天津）有限公司 ,'payer_card_no':9550880209469900147,'amount':500000,'secret':88bceeb2d5b91d06da677afe2416dd51}

str1=mch_id+'&'+channel_id+'&'+channel_name+'&'+out_trade_no+'&'+trade_no+'&'+status+'&'+tri_trade_no+'&'+time_start+'&'+time_end+'&'+err_msg+'&'+err_code+'&'+payer_name+'&'+payer_card_no+'&'+amount#+'&'+secret
str12=mch_id+channel_id+channel_name+out_trade_no+trade_no+status+tri_trade_no+time_start+time_end+err_msg+err_code+payer_name+payer_card_no+amount#+'&'+secret
str22='c349a7507a395e174a4fba153900eae9博裕融资租赁（天津）有限公司 广发银企直连-博裕测试模拟-10000-00-00 00:00:001000000000000192018-12-06 16:22:5920181206162259902950000091029154408446299168955088020946990014788bceeb2d5b91d06da677afe2416dd51'
str2=md5(str22.encode('utf8'))
#string 拆分为List 
strSplit=str1.split('&')  #str.split(str="", num=string.count(str)).
print (strSplit)
print ('\n')

#List排序
strSorted=sorted(strSplit)
print (strSorted)
print ('\n')
print(sorted(distance.items(),key=lambda  item:item[0]))
#List转为string，以&连接
strConvert = ''.join(strSorted)
strConvert = strConvert+secret
print(strConvert+'\n')
str3=md5(strConvert.encode('utf8'))

str4=base64.b64encode(str3.encode('utf8'))
print(str22)
print(str2)
str13=base64.b64encode(str2.encode('utf8'))
print(str13)
print(str3)
print(str4)
