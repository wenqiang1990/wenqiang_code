#coding:utf-8
import time,os
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
from public import swip
from extend import Appium_Extend
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {}
        desired_caps['deviceName'] = '3a11d697'# 3a11d697 ：红米note3
        desired_caps['platformName'] = 'Android'   
        desired_caps['platformVersion'] = '5.1.1'   
        desired_caps['appPackage'] = 'com.yuntongxun.eckuailiao' #com.yuntongxun.eckuailiao
        desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.account.SplashActivity'#com.yuntongxun.ecdemo.ui.phonemodel.PhoneUI#com.yuntongxun.ecdemo.ui.account.LoginActivity
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(10)
        self.extend = Appium_Extend(self.driver)          
       
        
    def test_get_screen_by_element(self):  
        element = self.driver.find_element_by_id("video_icon")  
        self.extend.get_screenshot_by_element(element).write_to_file("f:\\screen", "image")  
        assert_true(os.path.isfile("f:\\screen\\image.jpg"))  
  
    def test_same_as(self):  
        element = self.driver.find_element_by_id("video_icon")  
  
        load = self.extend.load_image("f:\\screen\\image.jpg")  
        #要求百分百相似  
        result = self.extend.get_screenshot_by_element(element).same_as(load, 0)  
        assert_true(result)  
    
    def test_videocall(self):
        '''视频通话''' 
        driver = self.driver
        #查找联系人
        login.test_login(self,phoneid="13311267857")#使用账号13366778606登录
        #点击聊天
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys("13366778604")
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/name_tv").click()
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_chat").click()         
        self.driver.find_element_by_id("chatting_a ttach_btn").click()  
        time.sleep(5)
        swip.swipLeft(self,500)#左划
        self.driver.find_element_by_name("17710556903").click()
        self.driver.find_element_by_id("entrance_chat").click()        
        #self.driver.find_element_by_name("a1").click()
        time.sleep(5)
        wq = driver.find_element_by_id("chatting_attach_btn")
        assert_not_none(wq,u"未定位到加号按钮")
        wq.click()
        time.sleep(2)
        driver.tap([(400,1660)], )#点击

        print "Start : %s" % time.ctime()
        time.sleep(6)
        print "End : %s" % time.ctime()
        #图片对比
        self.test_get_screen_by_element()
        self.test_same_as()
        time.sleep(2)
        driver.find_element_by_id("video_botton_cancle").click()
        time.sleep(5)
        self.driver.press_keycode('4')#点击返回键
        #logout.test_logout(self)#退出登录            
  
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_videocall"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      