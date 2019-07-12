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
        '''退出讨论组，@成员，发消息'''
        try:
            self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_negative_btn").click()#点击取消下载
        except:
            print (u"未弹出更新页")
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/icon").click()#点击加号
        self.driver.find_element_by_name(u"发起群聊").click()#发起群聊
        self.driver.find_element_by_name(u"魏阳阳").click()#点击魏阳阳
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/action_option_style_button").click()#点击确认
        time.sleep(1)
        #验证创建群组的名称及人数显示
        el = self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_action_title").get_attribute("text")
        self.assertEqual(el,u'温强、魏阳阳')
        el1 = self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_action_title_count").get_attribute("text")         
        self.assertEqual(el1,'(2)')
        #修改群名称、群公告、昵称 
        self.driver.tap([(940,80),(1060,200)], 100)#点击群组设置图标
        self.driver.find_element_by_name(u"群组名称").click()#点击确认
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/content").click()#点击
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/content").clear()
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/content").send_keys(u'自动化测试创建群组')
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/action_option_style_button").click()#点击
        
        
        
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