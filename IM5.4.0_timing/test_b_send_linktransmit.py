#coding:utf-8
import time
import datetime 
import unittest
from robot.utils.asserts import *
from appium import webdriver
from public import logout
from public import login
from public import swip
from appium.webdriver.common.touch_action import TouchAction
from clear_massage import clear_massage
from set_driver import set_driver
 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)                     
    
    def test_send_txt(self):
        '''转发链接消息给自己，现在自己显示为账号，会出错，以后改为昵称''' 
        time.sleep(2)
        clear_massage(self,name=u"qiuqiu")#删除消息页面，昵称为**的聊天记录
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys("13311267857")
        #self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_my").click()#点击搜索
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").click()#点击账号
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_chat").click()#点击发消息
        self.driver.find_element_by_id("chatting_content_et").send_keys("https://www.baidu.com")
        print "Start : %s" % time.ctime()
        time.sleep(2)
        print "Start : %s" % time.ctime() + u"等待两秒打开连接"
        self.driver.find_element_by_id("chatting_send_btn").click()     
        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()  
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()        

        self.driver.find_element_by_name("https://www.baidu.com").click()
        el=self.driver.contexts#获取H5页面
        time.sleep(2)
        print el
        el=self.driver.find_element_by_id("btn_middle").get_attribute("text")
        assert_equal(el, u"容联IM专有云", msg=u"访问链接失败")            
        print u"访问链接  %s 成功" % el  
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击分享
        self.driver.find_element_by_name(u"转发").click()#点击分享
        self.driver.find_element_by_name(u"qiuqiu").click()#点击分享
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button3").click()#点击确认
        self.driver.press_keycode('4')#点击返回键  
        self.driver.press_keycode('4')#点击返回键 
        el = self.driver.find_element_by_id("chatting_content_itv")
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