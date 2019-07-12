#coding:utf-8
import os
import time,random
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


        #获得机器屏幕大小x,y
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        l=[x,y]
        #print l
        with open('F:\Appium\size\size.txt','w') as f:
            for i in range(len(l)):
                f.write(str(l[i])+'\n')                         
                #print l[i]
            f.close()
              
    #屏幕向上滑动
    def swipeUp(self,t):
        with open('F:\Appium\size\size.txt','r') as f:
            l = f.readlines()
            for i in range(len(l)):
                l[i] = int(l[i][:len(l[i])-1])
            #print l
        x1=int(l[0]*0.5)    #x坐标
        y1=int(l[1]*0.75)   #起始y坐标
        y2=int(l[1]*0.25)   #终点y坐标
        #print [x1,y1,x1,y2]
        self.driver.swipe(x1,y1,x1,y2,t)

         
    def test_login(self,phoneid="13366778606"):#13366778606
        '''登陆，设置用户信息''' 
        phoneid = random.choice(["111", "13366778899", "123456789", "111111", "12345678901"])
        for i in range(500):
            self.driver.find_element_by_id("edittext").click()
            self.driver.find_element_by_id("edittext").set_text(phoneid)#timecode
            self.driver.find_element_by_id("sign_in_button").click()#点击登陆                     
            '''退出登陆''' 
            self.driver.find_element_by_id("btn_plus").click()#加号
            self.driver.context#可以定位到悬浮窗口
            self.driver.find_element_by_name(u"设置").click()
            time.sleep(2)
            self.swipeUp(500)#上滑
            time.sleep(2)
            self.driver.find_element_by_name(u"退出当前账号").click()
            self.driver.find_element_by_id("dilaog_button3").click()
            print i   
      
      
    def runTest(self):
        pass

    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_login"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)   