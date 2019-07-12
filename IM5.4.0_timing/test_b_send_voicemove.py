#coding:utf-8
import time
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
from public import swip
from clear_massage import clear_massage
from set_driver import set_driver 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10) 

    
    def test_send_voicemessage(self):
        '''发送语音消息取消功能''' 
        clear_massage(self,name=u"qiuqiu")#删除消息页面，昵称为**的聊天记录
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys("13311267857")
        #self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_my").click()#点击搜索
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").click()#点击账号 
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_chat").click()#点击发消息          
        self.driver.find_element_by_id("chatting_attach_btn").click()                  
        #发送语音
        self.driver.find_element_by_id("chatting_mode_btn").click()#左下角语音按钮
        #action1 = TouchAction(self.driver)  
        #el = self.driver.find_element_by_id("voice_record_imgbtn")
        self.driver.swipe(550,1450,550,1000,5000)
        time.sleep(2)
        print "上滑取消发送消息"
        self.driver.swipe(550,1450,350,1450,5000)
        time.sleep(2)
        print "左滑取消发送消息"
        self.driver.swipe(550,1450,750,1450,5000)
        time.sleep(2)
        print "右滑取消发送消息"
        self.driver.swipe(810,1600,54,1600,500)#左划
        print "切换到变音消息页面"
        time.sleep(2)
        print "上滑取消发送变音消息"
        self.driver.swipe(550,1450,550,1000,5000)
        time.sleep(2)
        print "左滑取消发送变音消息"      
        self.driver.swipe(550,1450,350,1450,5000)
        time.sleep(2)
        print "右滑取消发送变音消息"        
        self.driver.swipe(550,1450,750,1450,5000)
        #action1.long_press(el,duration=5000).perform()      
  
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_voicemessage"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      