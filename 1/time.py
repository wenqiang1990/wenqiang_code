# -*- coding: utf-8 -*-  
import time
import datetime 
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  
print timecode
code1 = int(timecode) + 20 
formcode=range(int(timecode),int(int(timecode) + 20 ))
print formcode

print "Start : %s" % time.ctime()#输出当前时间


