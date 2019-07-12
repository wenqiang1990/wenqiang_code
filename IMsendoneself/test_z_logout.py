#coding:utf-8
import time
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import swip
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
 
class Imtest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['deviceName'] = '3a11d697'  
        desired_caps['platformName'] = 'Android'   
        desired_caps['platformVersion'] = '5.1.1'   
        desired_caps['appPackage'] = 'com.yuntongxun.ecdemo'  
        desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.LauncherActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(30)


    def test_logout(self):
        '''退出当前账号''' 
        driver = self.driver
        #查找联系人
        time.sleep(5) 
        #退出
        #driver.find_element_by_id("btn_left").click()    
        driver.find_element_by_id("btn_plus").click()#加号
        time.sleep(2)
        driver.context#可以定位到悬浮窗口 
        driver.find_element_by_name(u"设置").click()  
        #driver.tap([(590,1190)], )#点击设置
        time.sleep(2)
        swip.swipeUp(self,500)#上滑
        driver.find_element_by_name(u"退出当前账号").click()
        driver.find_element_by_id("dilaog_button3").click()

  
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_logout"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      