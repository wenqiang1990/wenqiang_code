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
        '''账号温强验证接收到的表情消息，发送拍照图片消息'''
        try:
            self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_negative_btn").click()#点击取消下载
        except:
            print (u"未弹出更新页")
                 
        self.driver.find_element_by_name(u"魏阳阳").click()#点击账号
        sendoutcontent = self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_content_itv").get_attribute("text")
        #验证接收到的消息
        #self.assertEqual(sendoutcontent,'5')
        print(u'接收到的')  
        #删除接收到的消息      
        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_positive_btn").click()
        #self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_history_lv").click()#点击+
        
        #拍照
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_attach_btn").click()#点击+号
        self.driver.find_element_by_name(u"拍摄").click()
        #self.driver.find_element_by_id("cameraswitchtofront").click()#切换摄像头
        time.sleep(3)
        #self.driver.context#可以定位到悬浮窗口
        self.driver.tap([(372,1534),(708,1870)], 100)
        #self.driver.press_keycode('27')#点击拍照键  
        #self.driver.find_element_by_id("com.lenovo.scg:id/shutter_button").click()#联想快门
        time.sleep(4)#[690,1582][930,1822]
        print("Start : %s" % time.ctime() + u"拍照成功")#输出当前时间
        self.driver.tap([(690,1582),(930,1822)], 100)#[690,1582][930,1822]
        #self.driver.find_element_by_id("com.lenovo.scg:id/btn_done").click()#联想点击保存
        time.sleep(2)
        #self.driver.find_element_by_id("text_right").click()
        print("Start : %s" % time.ctime() + u"拍照成功")#输出当前时间
        time.sleep(2)
        print("Start : %s" % time.ctime() + u"等待5秒")
        #删除发送的消息 
        time.sleep(2)
        print(u'发送拍摄的图片')
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