#coding:utf-8
import threading
import ready1
import time
lock = threading.Lock()
  
def mul(device,path_to_apk):
    lock.acquire()
    ready1.readyH(device,path_to_apk).main_case()
    lock.release()
              
def nul(device,path_to_apk):        
    ready1.readyH(device,path_to_apk).main_case1()

#if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
#a = threading.Thread(target=nul,args=('e52f9b61','4725'))
b = threading.Thread(target=mul,args=('S9B7N17506015085','D:/541demo/5.4.1sc_app-debug.apk'))#S9B7N17506015085 3a11d697
#a.start()
b.start()
