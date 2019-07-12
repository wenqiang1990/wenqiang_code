#coding:utf-8
import time,os
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from public import login
from public import logout
from public import swip
from appium import webdriver
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
    '''
    def test_get_screen_by_element(self):  
        element = self.driver.find_element_by_id("chatting_content_iv")  
        self.extend.get_screenshot_by_element(element).write_to_file("f:\\screen", "image1") 
        #assert_true(os.path.isfile("f:\\screen\\image1.jpg"))  
  
    def test_same_as(self):  
        element = self.driver.find_element_by_id("chatting_content_iv")#chatting_content_iv
        load = self.extend.load_image("f:\\screen\\image1.jpg")
        #要求百分百相似  
        result = self.extend.get_screenshot_by_element(element).same_as(load, 20)  
        assert_true(result)
    '''
    def test_send_picture(self):
        '''图片原图预览后发送'''
        #clear_massage(self,name=u"球球")#删除消息页面，昵称为**的聊天记录
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys("13311267857")
        #self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_my").click()#点击搜索
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").click()#点击账号 
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_chat").click()#点击发消息
        #发送图片
        self.driver.find_element_by_id("chatting_attach_btn").click()#点击加号
        self.driver.find_element_by_name(u"相册").click()#点击相册
        self.driver.find_element_by_name("image").click()
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/checkmark").click()#点击选中
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/cb").click()#点击原图
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/button_preview").click()#点击预览
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/button_apply").click()#预览状态下点击发送
        print "Start : %s" % time.ctime()#输出当前时间
        time.sleep(5)
        print "Stop : %s" % time.ctime()#输出当前时间
        #self.test_get_screen_by_element()#获取图片保存到本地
        #删除发送的图片  
        el = self.driver.find_element_by_id("tv_read_unread")#状态
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()    
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除
        print "Start : %s" % time.ctime()#输出当前时间
        time.sleep(5)
        print "Stop : %s" % time.ctime()#输出当前时间
        #self.test_same_as()

        #接收到的图片对比发送的图片 
        #self.test_get_screen_by_element()#获取接收到的图片保存到本地  
        print u"接收图片成功"
        
        x1=self.driver.find_element_by_id("chatting_content_iv").location.get('x')
        y1=self.driver.find_element_by_id("chatting_content_iv").location.get('y')
        print x1,y1
        x1=int(x1)+400
        y1=int(y1)+100
        print x1,y1
        
        self.driver.tap([(x1,y1)],5000)
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除               

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_picture"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      