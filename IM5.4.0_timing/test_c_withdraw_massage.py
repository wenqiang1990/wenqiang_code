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
from clear_massage import clear_massage
from clear_massage import clear_allmassage
from set_driver import set_driver
import set
import get 
class Imtest(unittest.TestCase):
    #def __init__(self,driver):
        #self.driver = driver     
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)                  
               
    def test_send_txt(self):
        '''撤回文本、语音、图片、视频等消息'''
        try:
            logout.test_logout(self)#退出登录
        except:
            print u"未登录，无需执行退出登录操作" 
        time.sleep(2)
        login.test_login(self,phoneid="13311267857")
        time.sleep(2)
        driver= self.driver
        clear_massage(self,name=u"qiuqiu")
        clear_allmassage(self,id="com.yuntongxun.eckuailiao:id/nickname_tv")
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys("13311267857")
        #self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_my").click()#点击搜索 中文输入时无需收回键盘
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").click()#点击账号
        #print "Start : %s" % time.ctime()
        time.sleep(2)
        self.driver.find_element_by_name(u"发消息").click()#点击发消息
        #发送文本消息 
        set.set1()
        text1=get.get3()
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_et").send_keys(text1)#hello tester
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_send_btn").click()#发送
        time.sleep(2)
        #撤销发送的消息
        driver.swipe(600,300,600,1500,500)#下划 
        time.sleep(2)
        driver.swipe(600,300,600,1500,500)#下划 
        time.sleep(2)
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"撤销").click()
        time.sleep(2)
        #删除撤销的信息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_time_tv").get_attribute("text")
        assert_equal(el,u"你撤回了一条消息",msg=u'撤回消息消息验证失败')
        print u"撤回超长2048个字符消息成功"
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击聊天详情
        driver.find_element_by_name(u"清空聊天记录").click()#点击聊天详情
        driver.press_keycode('4')
        #发送混合消息
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_et").send_keys(u'中文1234567890ABCDEFGHIJKLMNOPQRSTUCWXYZabcdefghijklmnopqrstuvwxyz！#￥%……')#输入特殊字符
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_send_btn").click()#点击发送    
        #撤销发送的消息
        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"撤销").click()
        #删除撤销的信息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_time_tv").get_attribute("text")
        assert_equal(el,u"你撤回了一条消息",msg=u'撤回消息消息验证失败')
        print u"撤回表情文本混合消息成功"
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击聊天详情
        driver.find_element_by_name(u"清空聊天记录").click()#点击聊天详情
        driver.press_keycode('4')      
             
        #发送消息表情
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_smiley_btn").click()#点击切换表情
        self.driver.find_element_by_name("😄").click()#点击表情
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_send_btn").click()#点击发送
        #撤销发送的消息
        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"撤销").click()
        #删除撤销的信息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_time_tv").get_attribute("text")
        assert_equal(el,u"你撤回了一条消息",msg=u'撤回消息消息验证失败')
        print u"撤回表情消息成功"
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击聊天详情
        driver.find_element_by_name(u"清空聊天记录").click()#点击聊天详情
        driver.press_keycode('4')        
              
        #发送语音消息
        self.driver.find_element_by_id("chatting_mode_btn").click()#左下角语音按钮
        action1 = TouchAction(self.driver)  
        el = self.driver.find_element_by_id("voice_record_imgbtn")
        action1.long_press(el,duration=62000).perform()      
        #撤销发送的消息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_read_unread")#已读状态
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"撤销").click()
        #删除撤销的信息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_time_tv").get_attribute("text")
        assert_equal(el,u"你撤回了一条消息",msg=u'撤回消息消息验证失败')
        print u"撤回语音消息成功"
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击聊天详情
        driver.find_element_by_name(u"清空聊天记录").click()#点击聊天详情
        driver.press_keycode('4')        
        
        #成员发送图片
        self.driver.find_element_by_id("chatting_attach_btn").click()#点击加号
        self.driver.find_element_by_name(u"相册").click()#点击相册
        self.driver.find_element_by_name("image").click()
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/checkmark").click()#点击选中
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_send").click()#点击发送
        #撤销发送的消息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_read_unread")#已读状态
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"撤销").click()
        #删除撤销的信息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_time_tv").get_attribute("text")
        assert_equal(el,u"你撤回了一条消息",msg=u'撤回消息消息验证失败')
        print u"撤回图片消息成功"
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击聊天详情
        driver.find_element_by_name(u"清空聊天记录").click()#点击聊天详情
        driver.press_keycode('4') 

        #发送短视频
        self.driver.find_element_by_id("chatting_attach_btn").click()#点击加号
        self.driver.find_element_by_name(u"短视频").click()
        time.sleep(2) 
        action1 = TouchAction(self.driver)  
        el = self.driver.find_element_by_xpath("//android.widget.FrameLayout//android.view.View[2]")
        action1.long_press(el,duration=9000).perform()
        self.driver.find_element_by_xpath("//android.widget.FrameLayout//android.view.View[2]").click()#点击发送

        #撤销发送的消息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_read_unread")#已读状态
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"撤销").click()
        #删除撤销的信息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_time_tv").get_attribute("text")
        assert_equal(el,u"你撤回了一条消息",msg=u'撤回消息消息验证失败')
        print u"撤回短视频消息成功"
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击聊天详情
        driver.find_element_by_name(u"清空聊天记录").click()#点击聊天详情
        driver.press_keycode('4') 
  
  
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