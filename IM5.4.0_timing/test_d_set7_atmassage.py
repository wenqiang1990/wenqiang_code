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
from set_driver import set_driver 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)        

    
    def test_group_atmassage(self):  
        '''群成员发送@消息''' 
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
        print el
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组id,以后改为读取上一条用例创建群组的id
        #driver.find_element_by_name(el).click()#点击群组id,以后改为读取上一条用例创建群组的id 
        #群成员发送@消息
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_et").send_keys("@")#输入@
        driver.find_element_by_name(u"联通").click()#点击确认
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_send_btn").click()#点击发送
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理
        time.sleep(2)
        #driver.swipe(600,800,600,100,500)#上划 (810,960,54,960,500)
        driver.find_element_by_name(u"清空聊天记录").click()#点击删除群聊天记录
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button3").click()#点击确认
        driver.press_keycode('4')        
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_left").click()#群组内返回按钮
        driver.press_keycode('4')
        time.sleep(2)
        driver.press_keycode('4')
        logout.test_logout(self)#退出登录
        login.test_login(self,phoneid = "17600645696")#@成员登录
        clear_massage(self,name=u"系统通知")    
        time.sleep(2)
        #验证接收@消息
        #el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/last_msg_tv").get_attribute("text")
        #assert_equal(el,u"[有人@我]球球: @联通 ",msg=u'@消息验证失败')
        #print "群组内@成员发送消息成功"
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/nickname_tv").click()#点击群组消息
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理        
        time.sleep(2)
        driver.swipe(600,960,600,60,500)#上划 (810,960,54,960,500)
        driver.find_element_by_name(u"清空聊天记录").click()#点击删除群聊天记录
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button3").click()#点击确认            
        
           
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_group_atmassage"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      