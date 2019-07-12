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
import threading
from clear_massage import clear_massage

class myCase(object):  
    def __init__(self,driver):
        self.driver = driver  
    def case_one(self):
        lock = threading.Lock()
        lock.acquire()
        #self.driver = driver 
        '''查找联系人，发送文本消息''' 
        time.sleep(2)
        #login.test_login(self,phoneid="13311267857")
        time.sleep(2)
        clear_massage(self,name=u"球球")
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys("13366778604")
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_my").click()#点击搜索
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").click()#点击账号
        print "Start : %s" % time.ctime()
        time.sleep(2)
        self.driver.find_element_by_name(u"发消息").click()#点击发消息
        #发送文本消息 
        set.set1()
        text1=get.get1()
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_et").send_keys(text1)#hello tester
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_send_btn").click()#发送
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_et").send_keys("text1")#hello tester
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_send_btn").click()#发送        
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_et").send_keys("text1")#hello tester
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_send_btn").click()#发送                     
        print "已经点击发送"
        '''
        #验证发送消息
        sendoutcontent = self.driver.find_element_by_id("chatting_content_itv").get_attribute("text")
        print sendoutcontent
        receivecontent = self.driver.find_element_by_id("tv_read_unread").get_attribute("text")
        print receivecontent
        assert_equal(sendoutcontent,text1,msg=u'发送的消息验证失败')
        assert_equal(receivecontent,u"已读",msg=u'消息状态验证失败')
        
        #删除发送消息
        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()
        '''
  
  
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(myCase("case_one"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      