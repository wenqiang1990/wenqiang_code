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
    
           
    def test_login(self):   
        '''兑换''' 
        number = self.driver.find_element_by_id("tv_home_exchange")#点击兑换
        self.assertIsNotNone(number)
        number.click()
        self.driver.find_element_by_id("tv_u_store").click()#
        self.driver.find_element_by_name(u"中国移动").click()#
        time.sleep(2)     
        self.driver.find_element_by_id("btn_change").click()#点击立即兑换     
        self.driver.find_element_by_id("ed_phone").click()#点击手机号输入
        self.driver.find_element_by_id("ed_phone").send_keys("13711111111")#手机号输入
        self.driver.find_element_by_id("confirm_button").click()#点击提交
        self.driver.find_element_by_id("confirm_button").click()#点击确定
        time.sleep(2)
        self.driver.find_element_by_id("cancel_button").click()#点击完成
        self.driver.press_keycode('4')
        time.sleep(2)
        self.driver.press_keycode('4')
        time.sleep(2)  
        self.driver.find_element_by_id("tv_u_record").click()#点击兑换记录
        el=self.driver.find_element_by_id("tv_order_state").get_attribute("text")#获取兑换状态   
        assert_equal(el, u"兑换成功", msg=u"兑换状态验证失败")
        print u"兑换状态验证通过"        

   
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