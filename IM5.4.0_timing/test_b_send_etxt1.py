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
from clear_massage import clear_massage
from set_driver import set_driver
 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)                             
         
    def test_send_txt(self):
        '''查找联系人，发送文本消息2049字符''' 
        time.sleep(2)
        clear_massage(self,name=u"qiuqiu")#删除消息页面，昵称为**的聊天记录
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#联系人
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys("13311267857")
        #self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_my").click()#点击搜索
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").click()#点击账号
        #发送文本消息 
        set.set1()
        text2049=get.get()
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_chat").click()#点击发消息
        self.driver.find_element_by_id("chatting_content_et").send_keys(text2049)#hello tester
        self.driver.find_element_by_id("chatting_send_btn").click()#发送
        time.sleep(2)
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dialog_tv_message").get_attribute("text")
        assert_equal(el,u"您发送的文本超过最大长度限制",msg=u'消息验证失败')
        print u"发送文本长度最大2048验证通过"
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button1").click()#点击确认
        time.sleep(2)
        
        #删除发送失败的消息
        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
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