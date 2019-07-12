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
        '''群成员发送文本消息''' 
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
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_et").send_keys(u'中文1234567890ABCDEFGHIJKLMNOPQRSTUCWXYZabcdefghijklmnopqrstuvwxyz！#￥%……')#输入特殊字符
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_send_btn").click()#点击发送
        #验证发送消息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv").get_attribute("text")
        assert_equal(el,u"中文1234567890ABCDEFGHIJKLMNOPQRSTUCWXYZabcdefghijklmnopqrstuvwxyz！#￥%……",msg=u'消息验证失败')
        print "群组内发送消息成功"     
        #发送消息表情
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_smiley_btn").click()#点击切换表情
        self.driver.find_element_by_name("😄").click()#点击表情
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_send_btn").click()#点击发送
        #发送语音消息
        self.driver.find_element_by_id("chatting_mode_btn").click()#左下角语音按钮
        action1 = TouchAction(self.driver)  
        el = self.driver.find_element_by_id("voice_record_imgbtn")
        action1.long_press(el,duration=5000).perform()

        #群成员发送图片
        self.driver.find_element_by_id("chatting_attach_btn").click()#点击加号
        self.driver.find_element_by_name(u"相册").click()#点击相册
        self.driver.find_element_by_name("image").click()
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/checkmark").click()#点击选中
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_send").click()#点击发送

        #群成员发送短视频
        self.driver.find_element_by_id("chatting_attach_btn").click()#点击加号
        self.driver.find_element_by_name(u"短视频").click()
        time.sleep(2) 
        action1 = TouchAction(self.driver)  
        el = self.driver.find_element_by_xpath("//android.widget.FrameLayout//android.view.View[2]")
        action1.long_press(el,duration=9000).perform()
        self.driver.find_element_by_xpath("//android.widget.FrameLayout//android.view.View[2]").click()#点击发送
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