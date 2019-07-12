#coding=utf-8
import subprocess
import os
def start_Appium(host, port, bootstrap_port, appium_log_path): #device_uid,
    #appium -p 4723 -bp 4724 -U 22238e79 --command-timeout 600
    errormsg = ""
    appium_server_url =""
    try:
        if True:#self.port_is_free(host,port)
            cmd ='start /b appium -a '+ host +' -p '+ str(port)+ ' --bootstrap-port '+ str(bootstrap_port) +  ' --session-override --log '+ '"'+appium_log_path + '" --command-timeout 600'  #' -U '+ device_uid+
            print cmd
            #p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #stdout=PIPE, stderr=PIPE)
            p = subprocess.call(cmd, shell=True,stdout=open('E:/appium_logs/logs.log','w'),stderr=subprocess.STDOUT)
            print p
            appium_server_url = 'http://' + host +':' + str(port) +'/wd/hub'
            print appium_server_url
        else:
            print "port:%d is used!"%(port)
    except Exception, msg:
        errormsg = str(msg)
    return appium_server_url, errormsg
def stop_Appium(Appium_port):
    cmd = 'StopAppium.bat %s'%(Appium_port)
    print cmd
    p = os.popen(cmd)
    print p.read()

#start_Appium('127.0.0.1','4723','4724','E:/appium_logs')   
    
#stop_Appium('4723')
subprocess.Popen('taskkill /F /IM node.exe',shell=True)    
    
    
    