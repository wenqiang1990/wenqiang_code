# -*- coding: utf-8 -*-  
import time,os
import datetime 
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  
print(timecode)
code1 = int(timecode) + 20 
formcode=range(int(timecode),int(int(timecode) + 20 ))
print (formcode)

print ("Start : %s" % time.ctime())#输出当前时间

print ('***获取当前目录***')
print(os.getcwd())
print (os.path.abspath(os.path.dirname(__file__)))
print ('***获取上级目录***')
print (os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print (os.path.abspath(os.path.dirname(os.getcwd())))
print (os.path.abspath(os.path.join(os.getcwd(), "..")))
print ('***获取上上级目录***')
print (os.path.abspath(os.path.join(os.getcwd(), "../..")))


