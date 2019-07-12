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
        '''阿尔法卡管理-手动绑定''' 
        number = self.driver.find_element_by_id("activity_amin_rb3")#点击我的
        self.assertIsNotNone(number)
        number.click()
        self.driver.find_element_by_id("manage_sim").click()#点击阿尔法卡管理

        
        #强制等待
        print "Start : %s" % time.ctime()
        time.sleep(2)
        print "End : %s" % time.ctime()
        
        self.driver.find_element_by_name(u"管理").click()#点击管理
        self.driver.find_element_by_id("btn_unbind").click()#点击重新绑定
        self.driver.find_element_by_id("ed_serial_no").send_keys("0202 0016 0100 0006")
        self.driver.find_element_by_id("btn_bind_sim").click()#点击立即绑定
        time.sleep(2)
        self.driver.find_element_by_name(u"继续绑定").click()
        self.driver.find_element_by_name(u"确定").click()
        #self.driver.tap([(780,1130)], )
        #self.driver.find_element_by_name(u"继续绑定").click()#点击继续绑定
      
          
        el=self.driver.find_element_by_id("content_text").get_attribute("text")#获取连接提示
        assert_equal(el, u"恭喜您绑卡成功", msg="绑卡操作验证失败")
        print u"绑卡操作提示验证通过"        
        self.driver.find_element_by_id("confirm_button").click()
        self.driver.find_element_by_name(u"管理").click()#点击管理
        time.sleep(2)
        el=self.driver.find_element_by_id("tv_card_no").get_attribute("text")#获取阿尔法卡编号
        assert_equal(el, u"0202 0016 0100 0006", msg="绑卡操作验证失败")
        print u"绑卡操作验证通过"         
        self.driver.press_keycode("4")
        time.sleep(2)
        self.driver.press_keycode("4")
        el=self.driver.find_element_by_id("tv_pcenter_cardNo").get_attribute("text")#获取阿尔法卡编号
        assert_equal(el, "0202001601000006", msg="绑卡操作验证失败")
        print u"绑定号码与管理页显示号码相同验证通过" 
        
        self.driver.find_element_by_name(u"管理").click()#点击管理
        self.driver.find_element_by_id("btn_unbind").click()#点击重新绑定
        self.driver.find_element_by_id("ed_serial_no").send_keys("0203 0016 0101 3685")
        self.driver.find_element_by_id("btn_bind_sim").click()#点击立即绑定
        time.sleep(2)        
        
               
        
        
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