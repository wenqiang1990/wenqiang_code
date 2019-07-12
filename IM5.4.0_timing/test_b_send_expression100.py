#coding:utf-8
import time
import re
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
    
    def test_send_expression(self):
        '''查找联系人，发送表情'''
        #login.test_login(self,el="13311267857") 
        time.sleep(2)
        clear_massage(self,name=u"qiuqiu")#删除消息页面，昵称为**的聊天记录
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys("13311267857")
        #self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_my").click()#点击搜索
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").click()#点击账号
        time.sleep(2)
        #发送表情 
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_chat").click()#点击发消息
        el=self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_smiley_btn")
        self.assertIsNotNone(el,msg=u"定位表情切换图标失败")
        el.click()#点击切换到表情输入
        time.sleep(2)
        for i in range(101):
            #self.driver.find_element_by_name("😄").click()#点击表情
            self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"😄\"]").click()#点击表情
            print i
        self.driver.find_element_by_id("chatting_send_btn").click()
        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()    

        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()  
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()
        self.driver.press_keycode('4')#点击返回键       
  
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_expression"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      