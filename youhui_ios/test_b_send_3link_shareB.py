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
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver('3a11d697','4725')#联想
        self.verificationErrors = []
        self.driver.implicitly_wait(10)                  
               
    def test_send_txt(self):
        '''账号魏阳阳验证接收到的链接消息，分享到同事圈，转发给杨进仁，发送100个表情'''
        try:
            self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_negative_btn").click()#点击取消下载
        except:
            print (u"未弹出更新页")        
        self.driver.find_element_by_name(u"温强").click()#点击账号
        sendoutcontent = self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_content_itv").get_attribute("text")
        #验证接收到的消息
        self.assertEqual(sendoutcontent,'https://www.baidu.com')
        print(u'接收到的'+sendoutcontent)
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_content_itv").click()
        time.sleep(3)
        el=self.driver.contexts#获取H5页面
        time.sleep(2)
        print(el)
        #self.driver.find_element_by_class_name("android.widget.TextView").click()
        self.driver.tap([(936,73),(1080,217)], 100)#[936,73][1080,217]
        self.driver.find_element_by_name(u"分享到同事圈").click()#
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/shareContent").send_keys('share')
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/action_option_style_button").click()#点击发送
        #self.driver.find_element_by_class_name("android.widget.ImageButton").click()#点击返回
        self.driver.tap([(0,72),(168,219)], 100)#[0,72][168,219]
        #转发接收到的消息      
        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"转发").click()
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/multi_select_contact_edittext").send_keys('yjr')
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_select_cb").click()#点击选中
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/action_option_style_button").click()#点击确定
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_positive_btn").click()#点击确定
        #删除接收到的消息      
        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_positive_btn").click()        
        
        #发送100个表情
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_smiley_btn").click()
        for i in range(101):
            #self.driver.find_element_by_name("😄").click()#点击表情
            self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/emoji_id").click()#点击表情
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_send_btn").click()#发送
        #删除发送的消息 
        time.sleep(2)
        print(u'发送100表情')
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