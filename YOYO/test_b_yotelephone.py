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
    
           
    def test_b_yotelephone(self):   
        '''yo电话充值''' 
        number = self.driver.find_element_by_id("activity_amin_rb2")#点击yo电话
        self.assertIsNotNone(number)
        number.click()
        self.driver.find_element_by_name("更多").click()
        self.driver.context
        self.driver.find_element_by_id("tv_balance").click()#点击充值
        self.driver.find_element_by_id("bnt_10").click()#选择金额
        self.driver.find_element_by_id("yy_summit_bt").click()#提交订单
        self.driver.find_element_by_id("ck_right").click()#选中支付宝
        #self.driver.find_element_by_id("btn_pay").click()#点击确认支付
        time.sleep(2)
        self.driver.press_keycode("4")
        #self.driver.press_keycode("4")
        
        #强制等待
        print "Start : %s" % time.ctime()
        time.sleep(2)
        print "End : %s" % time.ctime()
        el=self.driver.find_element_by_id("search_content").get_attribute("text")
        assert_equal(el, u"0.15元/分钟", msg=u"返回验证失败")
        print u"返回网络电话页面"
        number = self.driver.find_element_by_id("activity_amin_rb3")
        self.assertIsNotNone(number)
        number.click()
        self.driver.find_element_by_id("tv_manager_order").click()#点击订单管理
        
        self.driver.find_element_by_name(u"待付款订单").click()#点击待付款订单
        el=self.driver.find_element_by_id("tv_order_name_ka").get_attribute("text")
        assert_equal(el, u"用户充值", msg=u"验证失败")
        
        el=self.driver.find_element_by_id("tv_order_state").get_attribute("text")
        assert_equal(el, u"待支付", msg=u"验证失败")
        print u"用户充值代付款订单验证通过"
            
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_b_yotelephone"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)   