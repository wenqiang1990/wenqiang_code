#coding:utf-8
import os
import time
import datetime 
import unittest
from robot.utils.asserts import *
from appium import webdriver
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S") 
class Imtest(unittest.TestCase):   
    def setUp(self):    
        desired_caps = {}
        desired_caps['deviceName'] = '3a11d697'# 3a11d697 ：红米note3
        desired_caps['platformName'] = 'Android'   
        desired_caps['platformVersion'] = '5.1.1'   
        desired_caps['appPackage'] = 'com.yuntongxun.ecdemo'  
        desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.LauncherActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(30) 
        IME_LISE = self.driver.available_ime_engines
        print(IME_LISE)
        #self.driver.deactivate_ime_engine()#g关闭当前输入法
        #self.driver.activate_ime_engine(IME_LISE[-1])

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
         
    def test_login(self,phoneid="1058099258@qq."):#13366778606
        '''错误邮箱格式账号登陆'''

        number = self.driver.find_element_by_id("edittext")
        self.assertIsNotNone(number)
        number.click()
        self.driver.find_element_by_id("edittext").set_text(phoneid)#timecode
        self.driver.find_element_by_id("sign_in_button").click()#点击登陆
        time.sleep(2)
        el=self.driver.find_element_by_id("sign_in_button").get_attribute("text")
        if el ==u"登录":
            print u"错误邮箱格式账号不能登陆验证通过"


    def runTest(self):
        pass

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_login"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)   