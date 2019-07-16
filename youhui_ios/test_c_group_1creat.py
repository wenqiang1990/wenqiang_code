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
        '''创建群组，设置群组个人名片，昵称、手机号、邮箱、备注'''
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
        
        self.driver.find_element_by_name(u"群公告").click()#点击确认
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/content").send_keys(u'自动化测试群公告')
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/action_option_style_button").click()#点击
        
        self.driver.find_element_by_name(u"我在本群的昵称").click()#点击确认
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_edittext").clear()
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_edittext").send_keys(u'自动化测试群昵称')
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_positive_btn").click()#点击确定      
        #踢出成员
        self.driver.find_element_by_name(u"删除").click()#点击删除
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_del").click()#点击删除
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_positive_btn").click()#点击确定
        #邀请成员
        self.driver.find_element_by_name(u"添加").click()#点击添加
        self.driver.find_element_by_name(u"魏阳阳").click()#点击魏阳阳
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/action_option_style_button").click()#点击确认
        #验证成员
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/group_all").click()#点击查看全部成员
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_search_et").click()#点击
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_search_et").send_keys('13671378634')#点击
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_name").click()#点击
        #验证名称
        el2 = self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/nameTv").get_attribute("text")         
        self.assertEqual(el2,u'魏阳阳')        
        self.driver.press_keycode(4)
        time.sleep(1)
        self.driver.press_keycode(4)   
        #踢出成员
        self.driver.find_element_by_name(u"删除").click()#点击删除
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_del").click()#点击删除
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_positive_btn").click()#点击确定        
        #验证群组名称修改
        time.sleep(1)
        self.driver.press_keycode(4)       
        self.driver.press_keycode(4) 
        el3 = self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_action_title").get_attribute("text")
        self.assertEqual(el3,u'自动化测试创建群组')        
        
        
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