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
        '''yo电话充值''' 
        number = self.driver.find_element_by_id("activity_amin_rb2")#点击yo电话
        self.assertIsNotNone(number)
        number.click()
        self.driver.find_element_by_name("更多").click()
        self.driver.context
        self.driver.find_element_by_id("tv_fee").click()#点击通讯录
        self.driver.find_element_by_xpath("//android.widget.LinearLayout").click()
        #强制等待
        print "Start : %s" % time.ctime()
        time.sleep(5)
        print "End : %s" % time.ctime()
        self.driver.press_keycode("4")
        #self.driver.press_keycode("4")
        

        el=self.driver.find_element_by_id("search_content").get_attribute("text")
        assert_equal(el, u"0.15元/分钟", msg=u"返回验证失败")
        print u"返回网络电话页面"
            
        
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