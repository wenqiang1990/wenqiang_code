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
from clear_massage import clear_massage
from set_driver import set_driver 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)       

    
    def test_send_voicemessage(self):
        '''发送空灵变声语音消息30秒''' 
        clear_massage(self,name=u"qiuqiu")#删除消息页面，昵称为**的聊天记录
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys("13311267857")
        #self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_my").click()#点击搜索
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").click()#点击账号
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_chat").click()#点击发消息   
                  
        #发送变声语音
        self.driver.find_element_by_id("chatting_mode_btn").click()#左下角语音按钮
        time.sleep(2)
        self.driver.swipe(810,1600,54,1600,500)
        action1 = TouchAction(self.driver)  
        el = self.driver.find_element_by_id("voice_record_imgbtn_biansheng")
        action1.long_press(el,duration=30000).perform()
        self.driver.find_element_by_name(u"空灵").click()
        self.driver.find_element_by_id("layout_send_changevoice").click()
        time.sleep(6)
        #删除
        el=self.driver.find_element_by_id("tv_read_unread").get_attribute("text")
        assert_equal(el, u"已读", msg=u"状态验证失败")            
        print el+u" 阅读状态验证成功"
        el = self.driver.find_element_by_id("tv_read_unread")#状态
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        print "Start : %s" % time.ctime()#输出当前时间
        time.sleep(2)
        print "Stop : %s" % time.ctime()#输出当前时间   
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除 

        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_voice_play_content").click()
        time.sleep(5)
        #删除接收语音
        action1 = TouchAction(self.driver)
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_time_tv")#时间
        action1.long_press(el,duration=5000).perform()    
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除    
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_voicemessage"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      