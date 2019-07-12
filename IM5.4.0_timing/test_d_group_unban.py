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
from clear_massage import clear_allmassage 
from set_driver import set_driver 

class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)       

    
    def test_group_unban(self):  
        '''被禁言群成员解除禁言''' 
        driver = self.driver
        time.sleep(2)
        member = "13366778604"  #被禁言成员账号
        clear_allmassage(self,id="com.yuntongxun.eckuailiao:id/nickname_tv")
        logout.test_logout(self)#退出登录
        login.test_login(self,phoneid = "13311267857")
        with open('F:\Appium\group\groupID.txt','r') as f:
            el=f.read()
        print el
        el="群组id:"+el
        print el
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击列表中第一个群组
        #driver.find_element_by_name(el).click()#点击群组id,以后改为读取上一条用例创建群组的id
        time.sleep(2) 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理  
        driver.find_element_by_name(u"设置群内禁言").click()#点击设置群内禁言
        #群成员解除禁言
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_clear_gag").click()#点击解禁
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button3").click()#点击确认
        driver.press_keycode('4')
        time.sleep(2)
        driver.press_keycode('4')
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_left").click()#群组内返回按钮
        driver.press_keycode('4')
        time.sleep(2)
        driver.press_keycode('4')
        logout.test_logout(self)#退出登录
        login.test_login(self,phoneid = member)#被禁言账号登录
        clear_massage(self,name="hello")#删除历史记录
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组id,以后改为读取上一条用例创建群组的id 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_et").send_keys("hello")
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_send_btn").click()#点击发送
        time.sleep(2)
        #验证发送消息
        sendoutcontent = self.driver.find_element_by_id("chatting_content_itv").get_attribute("text")
        print sendoutcontent
        receivecontent = self.driver.find_element_by_id("tv_read_unread").get_attribute("text")
        print receivecontent
        assert_equal(sendoutcontent,"hello",msg=u'发送的消息验证失败')
        assert_equal(receivecontent,u"未读",msg=u'消息状态验证失败')
        print "群组内被解禁成员发送消息成功" 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理
        time.sleep(2)
        driver.swipe(600,960,600,60,500)#上划 (810,960,54,960,500)
        time.sleep(1)
        driver.find_element_by_name(u"清空聊天记录").click()#点击删除群聊天记录
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button3").click()#点击确认        
          
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_group_unban"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      