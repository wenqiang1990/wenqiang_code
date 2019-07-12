#coding:utf-8
import time
import datetime 
import unittest
from robot.utils.asserts import *
from appium import webdriver
from public import logout
from public import login
from public import swip
from appium.webdriver.common.touch_action import TouchAction
from clear_massage import clear_massage
 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {}
        desired_caps['deviceName'] = '3a11d697'# 3a11d697 ：红米note3
        desired_caps['udid'] = '3a11d697' #设备的udid 实际控制启动哪台机器
        desired_caps['platformName'] = 'Android'   
        desired_caps['platformVersion'] = '5.1.1'   
        desired_caps['appPackage'] = 'com.yuntongxun.eckuailiao' #com.yuntongxun.eckuailiao
        desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.account.SplashActivity'#com.yuntongxun.ecdemo.ui.phonemodel.PhoneUI#com.yuntongxun.ecdemo.ui.account.LoginActivity
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(10)                       
    
    def test_send_txt(self):
        '''发送链接消息''' 
        time.sleep(2)
        #clear_massage(self,name=u"球球")#删除消息页面，昵称为**的聊天记录
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys("13311267857")
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/name_tv").click()
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_chat").click()
 
        self.driver.find_element_by_id("chatting_content_et").send_keys("https://www.baidu.com")
        time.sleep(2)
        self.driver.find_element_by_id("chatting_send_btn").click()
        
        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()  
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()        

        self.driver.find_element_by_name("https://www.baidu.com").click()
        el=self.driver.contexts#获取H5页面
        print el
        el=self.driver.find_element_by_id("btn_middle").get_attribute("text")
        assert_equal(el, u"下载", msg=u"访问链接失败")            
        print u"访问链接成功"
        self.driver.press_keycode('4')#点击返回键  
        el = self.driver.find_element_by_id("chatting_content_itv")
        action1.long_press(el,duration=5000).perform()        
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()   

        
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_txt"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      