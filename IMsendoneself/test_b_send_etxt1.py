#coding:utf-8
import time,os
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
from extend import Appium_Extend
import set
import get 
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
         
    def test_send_txt(self):
        '''查找联系人，发送文本消息''' 
        time.sleep(5)
        self.driver.swipe(810,960,54,960,500)#左划
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/card_item_tv").click()
        self.driver.find_element_by_id("content").click()
        self.driver.find_element_by_id("content").send_keys("13311267857")
        self.driver.find_element_by_id("text_right").click()
        #发送文本消息 
        set.set1()
        text200=get.get()
        self.driver.find_element_by_id("chatting_content_et").click()
        self.driver.find_element_by_id("chatting_content_et").send_keys(text200)#hello tester
        self.driver.find_element_by_id("chatting_send_btn").click()#发送
        self.driver.press_keycode('4')#点击返回键
        time.sleep(2)
        #验证发送消息
        sendoutcontent = self.driver.find_element_by_id("chatting_content_itv").get_attribute("text")
        print sendoutcontent
        receivecontent = self.driver.find_element_by_id("tv_read_unread").get_attribute("text")
        print receivecontent
        assert_equal(sendoutcontent,text200,msg=u'发送的消息验证失败')
        assert_equal(receivecontent,u"已读",msg=u'消息状态验证失败')
        
        #删除发送消息
        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()        
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()        
        #验证接收的消息
        sendoutcontent = self.driver.find_element_by_id("chatting_content_itv").get_attribute("text")    
        assert_equal(sendoutcontent,text200,msg=u'接收的消息验证失败')
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