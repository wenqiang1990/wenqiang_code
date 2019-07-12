#coding:utf-8
import time,os
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
          
    '''        
    def test_get_screen_by_element(self):  
        element = self.driver.find_element_by_id("chatting_content_iv")  
        self.extend.get_screenshot_by_element(element).write_to_file("f:\\screen", "image2") 
        assert_true(os.path.isfile("f:\\screen\\image2.jpg"))  
  
    def test_same_as(self):  
        element = self.driver.find_element_by_id("chatting_content_iv")  
  
        load = self.extend.load_image("f:\\screen\\image2.jpg")
        #要求百分百相似  
        result = self.extend.get_screenshot_by_element(element).same_as(load, 0)  
        assert_true(result)
    '''    
    def test_send_readrurn(self):
        '''拍摄照片发送阅后即焚'''
        #login.test_login(self,phoneid="13311267857")
        time.sleep(2) 
        '''el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/nickname_tv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"取消置顶").click()
        print u"取消置顶成功"'''
        clear_massage(self,name=u"qiuqiu")#删除消息页面，昵称为**的聊天记录 
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys("13311267857")
        #self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_my").click()#点击搜索
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").click()#点击账号
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_chat").click()#点击发消息        
        #发送阅后即焚图片
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
        time.sleep(3)
        self.driver.press_keycode('4')#点击返回键
        #self.driver.find_element_by_id("chatting_content_itv").click()  
        time.sleep(2)
        self.driver.press_keycode('4')#点击返回键
        self.driver.press_keycode('4')#点击返回键
        logout.test_logout(self)#退出登录
        login.test_login(self,phoneid="13311267857")#使用账号receive登录 
        time.sleep(2)
        self.driver.find_element_by_name(u"温强").click()
        self.driver.find_element_by_id("chatting_content_iv").click()
        time.sleep(2)
        self.driver.press_keycode('4')#点击返回键  
        print "Start : %s" % time.ctime()#输出当前时间  
        time.sleep(2)
        print "Stop : %s" % time.ctime()#输出当前时间    
        #获取点击后的图片
        #self.test_get_screen_by_element()#截取屏幕
        #对比焚毁的图片
        time.sleep(2)
        #self.test_same_as()#对比图片
        time.sleep(2)
        print u"接收图片成功"        
        #发送阅后即焚图片

        x1=self.driver.find_element_by_id("chatting_content_iv").location.get('x')
        y1=self.driver.find_element_by_id("chatting_content_iv").location.get('y')
        print x1,y1
        x1=int(x1)+400
        y1=int(y1)+100
        print x1,y1
        
        self.driver.tap([(x1,y1)],5000)
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除
         
        self.driver.press_keycode('4')#点击返回键    


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