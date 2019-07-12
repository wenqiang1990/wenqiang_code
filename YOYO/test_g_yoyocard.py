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
              
    #屏幕向上滑动
    def swipeUp(self,t):
        with open('F:\Appium\size\size.txt','r') as f:
            l = f.readlines()
            for i in range(len(l)):
                l[i] = int(l[i][:len(l[i])-1])
        x1=int(l[0]*0.5)  #x坐标
        y1=int(l[1]*0.75)   #起始y坐标
        y2=int(l[1]*0.25)   #终点y坐标
        self.driver.swipe(x1,y1,x1,y2,t)
    
           
    def test_login(self):   
        '''购买阿尔法卡''' 
        number = self.driver.find_element_by_id("iv_home_buysim")#点击YOYO卡链接
        self.assertIsNotNone(number)
        number.click()
        time.sleep(3)
        el=self.driver.find_element_by_id("tv_product_name").get_attribute("text")
        assert_equal(el, u"阿尔法卡", msg="阿尔法卡名称显示错误")
        self.driver.find_element_by_id("btn_pre_order").click()#点击立即支付
        self.driver.find_element_by_id("ck_right").click()#点击余额
        self.driver.find_element_by_id("btn_pay").click()#点击确认支付
        self.driver.find_element_by_id("confirm_button").click()#点击确定
        el=self.driver.find_element_by_id("content_text").get_attribute("text")#获取弹窗信息
        assert_equal(el, u"支付成功", msg="支付失败")
        print u"使用余额支付成功"          
        self.driver.find_element_by_id("cancel_button").click()#点击完成
        number = self.driver.find_element_by_id("activity_amin_rb3")#点击我的
        self.assertIsNotNone(number)
        number.click()
        self.driver.find_element_by_id("tv_manager_order").click()#点击订单管理    
        self.driver.find_element_by_name(u"已完成订单").click()#点击待付款订单
        el=self.driver.find_element_by_id("tv_order_name_ka").get_attribute("text")
        assert_equal(el, u"阿尔法卡", msg=u"验证失败")
        
        el=self.driver.find_element_by_id("tv_order_state").get_attribute("text")
        assert_equal(el, u"支付完成", msg=u"验证失败")
        print u"阿尔法卡已完成订单验证通过"
        

                      
   
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