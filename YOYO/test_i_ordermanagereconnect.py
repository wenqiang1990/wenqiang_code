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
        self.driver.implicitly_wait(30) 

    def swipLeft(self,t):
        l=[1080,1980]
        x1=int(l[0]*0.75)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.05)
        print [x1,y1,x2,y1]
        self.driver.swipe(x1,y1,x2,y1,t)
    
           
    def test_i_ordermanagereconnect(self):   
        '''阿尔法卡管理-已连接状态下连接其他套餐''' 
        number = self.driver.find_element_by_id("activity_amin_rb3")#点击我的
        self.assertIsNotNone(number)
        number.click()
        self.driver.find_element_by_id("manage_sim").click()#点击阿尔法卡管理

        
        #强制等待
        print "Start : %s" % time.ctime()
        time.sleep(2)
        print "End : %s" % time.ctime()
        
        self.driver.find_element_by_id("iv_flow_pic").click()#点击选择套餐
        
        self.driver.find_element_by_name(u"日本10日套餐").click()#选择可用套餐
        #改成选择第二份可用套餐
        
        time.sleep(2)
        self.driver.find_element_by_id("confirm_button").click()
        time.sleep(16)
        el=self.driver.find_element_by_id("tv_state").get_attribute("text")#获取连接状态
        assert_equal(el, u"已连接", msg="连接失败")
        print u"连接状态验证通过" 
        el=self.driver.find_element_by_id("tv_manager").get_attribute("text")#获取连接提示
        assert_equal(el, u"点击断开", msg="连接操作验证失败")
        print u"连接其他可用套餐操作提示验证通过"                      

        time.sleep(2)
        self.driver.press_keycode("4")
        self.driver.press_keycode("4")
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_i_ordermanagereconnect"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)   