#coding:utf-8
from appium import webdriver
class eleA(object):  
    def __init__(self):   
        desired_caps = {}
        desired_caps['deviceName'] = 'a2c3e2d9'  #adb devices查到的设备名
        desired_caps['platformName'] = 'Android'   #设备系统
        desired_caps['platformVersion'] = '5.1.1'   #系统版本       
        desired_caps['appPackage'] = 'com.yuntongxun.ecdemo'  #被测App的包名
        desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.LauncherActivity' #启动时的Activity
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)#启动app
        
        
class eleB(eleA):
    driver = webdriver
    def __init__(self):
        #这一行解决了问题
        eleA.__init__(self)
        
    def getSize(self):#获得机器屏幕大小x,y
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return(x,y)           
                            
    def sign_in(self,phone_number):
        self.driver.find_element_by_id("edittext").click()
        self.driver.find_element_by_id("edittext").send_keys(phone_number)
        self.driver.find_element_by_id("sign_in_button").click()#登陆   

        
        
           
        #屏幕向上滑动
    def swipeUp(self,t):
        l=self.getSize()
        x1=int(l[0]*0.5)  #x坐标
        y1=int(l[1]*0.75)   #起始y坐标
        y2=int(l[1]*0.25)   #终点y坐标
        self.driver.swipe(x1,y1,x1,y2,t)
        #屏幕向下滑动
    def swipeDown(self,t):
        l=self.getSize()
        x1=int(l[0]*0.5)  #x坐标
        y1=int(l[1]*0.35)  #起始y坐标
        y2=int(l[1]*0.75)   #终点y坐标
        print [x1,y1,x1,y2]
        self.driver.swipe(x1,y1,x1,y2,t)
        #屏幕向左滑动
    def swipLeft(self,t):
        l=self.getSize()
        x1=int(l[0]*0.75)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.05)
        print [x1,y1,x2,y1]
        self.driver.swipe(x1,y1,x2,y1,t)
        #屏幕向右滑动
    def swipRight(self,t):
        l=self.getSize()
        x1=int(l[0]*0.05)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.75)
        self.driver.swipe(x1,y1,x2,y1,t)
        
A=eleA()
B=eleB()
B=B.getSize()
B=B.sign_in(1331)
B=B.swipeDown(500)
B=B.swipeUp(500)
B=B.swipLeft(500)
B=B.swipRight(500)






    