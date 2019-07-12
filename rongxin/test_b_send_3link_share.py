#coding:utf-8
import time,os
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
#from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
from public.extend import Appium_Extend 
from public.clear_massage import clear_massage
from public.clear_massage import clear_allmassage
from public.set_driver import set_driver
from public import set
from public import get
 
class Imtest(unittest.TestCase):
    #def __init__(self,driver):
        #self.driver = driver     
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver('e52f9b61','4723')#三星
        self.verificationErrors = []
        self.driver.implicitly_wait(10)                  
               
    def test_send_txt(self):
        '''账号温强验证接收到的语音消息长度，发送链接消息'''
        try:
            self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_negative_btn").click()#点击取消下载
        except:
            print (u"未弹出更新页")          
        self.driver.find_element_by_name(u"魏阳阳").click()#点击账号
        
        sendoutcontent = self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_content_itv").get_attribute("text")
        #验证接收到的消息
        self.assertEqual(sendoutcontent,'59"')
        print(u'接收到的')  
        #删除接收到的消息      
        el = self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_voice_play_anim_tv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_positive_btn").click()
        #self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_history_lv").click()#点击+
        
        #发送链接
        set.set1()
        text6=get.get6()
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_content_et").send_keys(text6)#hello tester
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_send_btn").click()#发送
    
        #删除发送的消息 
        time.sleep(2)
        print(u'发送'+text6)
        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_positive_btn").click()  
  
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