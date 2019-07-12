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
        '''国际流量''' 
        number = self.driver.find_element_by_id("tv_home_flow")#点击国际流量
        self.assertIsNotNone(number)
        number.click() 
        self.driver.find_element_by_id("iv_country").click()#点击国家 
        self.driver.find_element_by_id("tv_price").click()#点击套餐
        el1=self.driver.find_element_by_id("tv_product_name").get_attribute("text")
        print u"购买的套餐名称是" +el1
        
        time.sleep(2)
        self.driver.find_element_by_id("btn_pre_order").click()#点击立即支付
        time.sleep(2)
        self.driver.find_element_by_id("ck_right").click()#选中余额
        self.driver.find_element_by_id("btn_pay").click()#点击确认支付
        self.driver.find_element_by_id("confirm_button").click()#点击确定
        el=self.driver.find_element_by_id("content_text").get_attribute("text")#获取弹窗信息
        assert_equal(el, u"支付成功", msg="支付失败")
        print u"使用余额支付成功"
        self.driver.find_element_by_id("cancel_button").click()#点击完成
        self.driver.press_keycode('4')#点击返回
        time.sleep(2)
        self.driver.press_keycode('4')#点击返回
        
        el=self.driver.find_element_by_id("tv_home_charge").get_attribute("text")#获取流量充值    
        assert_equal(el, u"国内流量", msg=u"主页面验证失败")
        print u"购买国际流量，用例执行完毕，成功回到主页面"
        
        number = self.driver.find_element_by_id("activity_amin_rb3")#点击我的
        self.assertIsNotNone(number)
        number.click()
        self.driver.find_element_by_id("tv_manager_order").click()#点击订单管理
        
        self.driver.find_element_by_name(u"已完成订单").click()#点击待付款订单
        el=self.driver.find_element_by_id("tv_order_name_ka").get_attribute("text")
        assert_equal(el, el1, msg=u"验证失败")
        
        el=self.driver.find_element_by_id("tv_order_state").get_attribute("text")
        assert_equal(el, u"支付完成", msg=u"验证失败")
        print u"国际流量已完成订单验证通过"        
             
   
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