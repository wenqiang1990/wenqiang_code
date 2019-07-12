#coding:utf-8
import time
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
from clear_massage import clear_massage
import set
import get
from set_driver import set_driver 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)
    
    def test_send_txtmassage(self):  
        '''群成员发送语音消息是滑动取消发送''' 
        clear_massage(self,name="group")
        clear_massage(self,name=u"系统通知")
        driver = self.driver
        with open('F:\Appium\group\groupID.txt','r') as f:
            el=f.read()
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        el=u"群组id:"+el
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组id,以后改为读取上一条用例创建群组的id
        #driver.find_element_by_name(el).click()#点击群组id,以后改为读取上一条用例创建群组的id 
        #群成员发送消息
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
        time.sleep(2) 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理
        time.sleep(2)
        driver.swipe(600,800,600,100,500)#上划 (810,960,54,960,500)
        time.sleep(2)
        driver.find_element_by_name(u"清空聊天记录").click()#点击删除群聊天记录
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button3").click()#点击确认        
            
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_txtmassage"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      