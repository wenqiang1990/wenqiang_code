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
        #desired_caps['unicodeKeyboard'] = "true"#使用 Unicode 输入法。默认值false
        #desired_caps['resetKeyboard'] = "true"#在设定了 unicodeKeyboard 关键字的 Unicode 测试结束后，重置输入法到原有状态。如果单独使用，将会被忽略。默认值 false         
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
        '''我的——用户信息设置——设置默认收货地址''' 
        number = self.driver.find_element_by_id("activity_amin_rb3")#点击我的
        self.assertIsNotNone(number)
        number.click()
        self.driver.find_element_by_xpath("//android.widget.ImageButton").click()#点击修改按钮
   
        #强制等待
        print "Start : %s" % time.ctime()
        time.sleep(2)
        print "End : %s" % time.ctime()
        self.driver.find_element_by_name(u"收货地址管理").click()#点击
        self.driver.find_element_by_id("btn_edit").click()#点击第一条地址修改按钮
        self.driver.find_element_by_id("cb").click()#点击设为默认
        self.driver.find_element_by_id("btn_save").click()#点击保存
        
        el=self.driver.find_element_by_id("tv_default").get_attribute("text")#获取弹窗信息
        assert_equal(el, u"默认", msg="验证设置默认地址失败")
        print u"验证默认地址标志成功" 
        self.driver.press_keycode("4")
        time.sleep(2)
        self.driver.press_keycode("4")
        self.driver.find_element_by_id("activity_amin_rb1").click()#点击主页
        number = self.driver.find_element_by_id("iv_home_buysim")#点击YOYO卡链接
        self.assertIsNotNone(number)
        number.click()     
        el=self.driver.find_element_by_id("tv_address_name").get_attribute("text")#获取地址信息
        assert_equal(el, u"name", msg="验证设置默认地址失败")
        print u"验证置默认地址收货人成功" 
        el=self.driver.find_element_by_id("tv_address_phone").get_attribute("text")#获取地址信息
        assert_equal(el, "133****8604", msg="验证设置默认地址失败")
        print u"验证置默认地址自动加载成功"         
             
        
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