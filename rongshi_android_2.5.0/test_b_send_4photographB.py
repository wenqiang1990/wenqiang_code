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
        self.driver=wq.get_driver('3a11d697','4725')#联想
        self.verificationErrors = []
        self.driver.implicitly_wait(10)                  
               
    def test_send_txt(self):
        '''验证接收图片，发送图片消息'''
        try:
            self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_negative_btn").click()#点击取消下载
        except:
            print (u"未弹出更新页")
        self.driver.find_element_by_name(u"温强").click()#点击账号
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_content_iv").click()
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/imagebrower_iv_save").click()#下载
        time.sleep(3)
        el=self.driver.contexts#获取H5页面
        print(el)
        self.driver.press_keycode('4')
        #self.driver.tap([(500,900),(600,1000)],100)
        #sendoutcontent = self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_content_iv").get_attribute("text")
        #验证接收到的消息
        #self.assertEqual(sendoutcontent,'5')
        print(u'接收到图片')  
        #删除接收到的消息      
        el = self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_content_iv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_positive_btn").click()
        #self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_history_lv").click()#点击+
        
        #发送本地照片
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_attach_btn").click()#点击+号
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_attach_btn").click()#点击+号
        self.driver.find_element_by_name(u"图片").click()
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/rcv_choice").click()#点击
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/action_option_style_button").click()#点击发送
        #self.driver.find_element_by_id("cameraswitchtofront").click()#切换摄像头
        time.sleep(3)

        print(u'发送图片')
        el = self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_content_iv")
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