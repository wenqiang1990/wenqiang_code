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
        desired_caps['deviceName'] = '3a11d697'  
        desired_caps['platformName'] = 'Android'   
        desired_caps['platformVersion'] = '5.1.1'   
        desired_caps['appPackage'] = 'com.yuntongxun.yuya'  
        desired_caps['appActivity'] = 'com.yuntongxun.yuya.ui.guilder.SplashActivity' 
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(10) 

    def swipLeft(self,t):
        l=[1080,1980]
        x1=int(l[0]*0.75)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.05)
        print [x1,y1,x2,y1]
        self.driver.swipe(x1,y1,x2,y1,t)
    
           
    def test_login(self):   
        '''领yo币，''' 
        number = self.driver.find_element_by_id("tv_home_sign")#点击领yo币
        self.assertIsNotNone(number)
        number.click()
        el=self.driver.find_element_by_id("tv_sign_days").get_attribute("text")#获取签到天数
        el1=self.driver.find_element_by_id("tv_u_no").get_attribute("text")#获取总yo币数
        self.driver.find_element_by_id("btn_sign").click()#点击签到
        try:
            self.driver.find_element_by_id("confirm_button").click()#点击确定
            self.driver.find_element_by_id("confirm_button").click()#点击确定    
        except:
            print u"已经签过到了，"+el+u"，总yo币数是"+el1
               
        self.driver.press_keycode('4')#点击返回
        el=self.driver.find_element_by_id("tv_home_charge").get_attribute("text")#获取流量充值    
        assert_equal(el, u"国内流量", msg=u"主页面验证失败")
        print u"领取yo币，用例执行完毕，成功回到主页面"
        
   
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