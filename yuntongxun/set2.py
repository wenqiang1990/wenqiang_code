#coding:utf-8
import os
import time
import datetime 
import unittest
from robot.utils.asserts import *
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S") 
class Imtest(unittest.TestCase):   
    def setUp(self):    
        desired_caps = {}
        desired_caps['deviceName'] = '3a11d697'  
        desired_caps['platformName'] = 'Android'   
        desired_caps['platformVersion'] = '5.1.1'   
        desired_caps['appPackage'] = 'com.yuntongxun.ecdemo'  
        desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.LauncherActivity' 
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(30) 

        #获得机器屏幕大小x,y
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        l=[x,y]
        print l
        with open('F:\Appium\size\size.txt','w') as f:
            for i in range(len(l)):
                f.write(str(l[i])+'\n')                         
                print l[i]
            f.close()
              
    #屏幕向上滑动
    def swipeUp(self,t):
        with open('F:\Appium\size\size.txt','r') as f:
            l = f.readlines()
            for i in range(len(l)):
                l[i] = int(l[i][:len(l[i])-1])
            print l
        x1=int(l[0]*0.5)    #x坐标
        y1=int(l[1]*0.75)   #起始y坐标
        y2=int(l[1]*0.25)   #终点y坐标
        print [x1,y1,x1,y2]
        self.driver.swipe(x1,y1,x1,y2,t)

    def swipLeft(self,t):
        #l=[1080,1980]       
        with open('F:\Appium\size\size.txt','r') as f:
            l = f.readlines()
            for i in range(len(l)):
                l[i] = int(l[i][:len(l[i])-1])
            print l
        x1=int(l[0]*0.75)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.05)
        print [x1,y1,x2,y1]
        self.driver.swipe(x1,y1,x2,y1,t)
         
    def test_set(self,connect='',port1='',lvs='',fileserver='',appid='aaf98f8944e7df950144e8da282e0118',apptoken='d9e42bd10dae11e5ac73ac853d9f54f2'):
        '''登陆，设置app''' 
        action1 = TouchAction(self.driver)  
        el = self.driver.find_element_by_id("btn_middle")#长按云通讯进入设置页面
        action1.long_press(el,duration=3000).perform()
        self.driver.find_element_by_id("setup_connect").set_text(connect)
        #self.driver.find_element_by_name("8085").clear()
        self.driver.find_element_by_id("setup_connect_port").set_text(port1)
        self.driver.find_element_by_id("setup_lvs").set_text(lvs)
        self.driver.find_element_by_id("setup_fileserver").set_text(fileserver)
        self.driver.press_keycode('4')#点击返回键
        self.driver.find_element_by_id("setup_appid").set_text(appid)
        self.driver.press_keycode('4')#点击返回键
        self.driver.find_element_by_id("setup_apptoken").set_text(apptoken)
        self.driver.press_keycode('4')#点击返回键
        if connect=='':
            self.driver.find_element_by_id("set_app_button").click()#点击设置appid
        else:
            self.driver.find_element_by_id("set_all_button").click()#点击设置全部
        self.driver.find_element_by_id("btn_left").click() 
                

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_set"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)   