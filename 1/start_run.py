#coding=utf-8
import subprocess
subprocess.Popen('killall node',shell=True)
#subprocess.Popen("cd C:\Program Files (x86)\Appium\\node_modules\\appium\lib\server\main.js --address 127.0.0.1 --port 4723")
#subprocess.Popen('C:\Program Files (x86)\Appium\\node_modules\\appium\lib\server\main.js –address "127.0.0.1" -p "4723" –command-timeout "100" –automation-name "Appium" >/tmp/1.txt',shell=True)
#subprocess.Popen('C:\Program Files (x86)\Appium\\node_modules\\appium\lib\server\main.js –address "127.0.0.1" -p "'+str(4723+2*i)+'" –command-timeout "100" –automation-name "Appium" -U "'+ip[i]+':'+str(5555+i)+'">/tmp/1.txt',shell=True) 
'''
k=1
while k <2:
    now_time=time.strftime('%H_%M')
    if now_time == '13_49':
        print u"开始运行脚本:"
        os.chdir("D:\\appium\\rf\\APItest\\apitest\\TestItem\\TestItem\\TestItem")
        os.system('pybot runningfishtestcase.txt') #执行脚本
        print u"运行完成退出"
        break
    else:
        time.sleep(10)
        print now_time
start /b node        
cd        
'''



