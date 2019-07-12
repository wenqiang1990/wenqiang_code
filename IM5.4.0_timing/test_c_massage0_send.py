#coding:utf-8
import time
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
from public import swip
from extend import Appium_Extend
from clear_massage import clear_massage
from set_driver import set_driver
class Imtest(unittest.TestCase):  
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)    
        self.extend = Appium_Extend(self.driver)     

    def test_send_readrurn(self):
        '''向其他账户发送消息'''
        #login.test_login(self,phoneid="13311267857")
        time.sleep(2)
        clear_massage(self,name=u"qiuqiu")#删除消息页面，昵称为**的聊天记录 
        driver = self.driver
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys("13366778604")
        #self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_my").click()#点击搜索
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").click()#点击账号
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_chat").click()#点击发消息        
        #发送阅后即焚图片
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

        #成员发送图片
        self.driver.find_element_by_id("chatting_attach_btn").click()#点击加号
        self.driver.find_element_by_name(u"相册").click()#点击相册
        self.driver.find_element_by_name("image").click()
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/checkmark").click()#点击选中
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_send").click()#点击发送

        #发送短视频
        self.driver.find_element_by_id("chatting_attach_btn").click()#点击加号
        self.driver.find_element_by_name(u"短视频").click()
        time.sleep(2) 
        action1 = TouchAction(self.driver)  
        el = self.driver.find_element_by_xpath("//android.widget.FrameLayout//android.view.View[2]")
        action1.long_press(el,duration=9000).perform()
        self.driver.find_element_by_xpath("//android.widget.FrameLayout//android.view.View[2]").click()#点击发送
        
        #发送阅后即焚
        self.driver.find_element_by_id("chatting_attach_btn").click()
        self.driver.find_element_by_name(u"阅后即焚").click()
        self.driver.find_element_by_name(u"拍照").click()
        time.sleep(2)
        self.driver.press_keycode('27')#点击拍照键  
        #self.driver.find_element_by_id("com.lenovo.scg:id/shutter_button").click()#联想快门
        time.sleep(2)
        self.driver.find_element_by_id("com.sec.android.app.camera:id/okay").click()#三星s5点击确定
        time.sleep(2)
        print "Start : %s" % time.ctime()
        ''' 
        self.driver.find_element_by_id("com.lenovo.scg:id/shutter_button").click()#联想P1拍照
        time.sleep(2)
        self.driver.find_element_by_id("com.lenovo.scg:id/btn_done").click()
        time.sleep(2)
        '''
        self.driver.find_element_by_name(u"确定").click()#预览页面点击确定
        time.sleep(2)
        self.driver.press_keycode('4')#点击返回键
        time.sleep(2)
        self.driver.press_keycode('4')#点击返回键
        time.sleep(1)
        self.driver.press_keycode('4')#点击返回键   
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_tab_msg").click()
        '''#消息置顶
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/nickname_tv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        driver.find_element_by_name(u"置顶聊天").click()
        print u"置顶聊天消息"'''

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_readrurn"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      