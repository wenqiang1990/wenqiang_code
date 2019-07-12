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
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
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
        '''发送阅后即焚，相册选取图片'''
        try:
            logout.test_logout(self)#退出登录
        except:
            print "未登录，无需执行退出登录操作"   
        login.test_login(self,phoneid="13311267857") 
        self.driver.find_element_by_name(u"温强").click()
        time.sleep(2)
        #验证并删除上次发送的图片
        el=self.driver.find_element_by_id("tv_read_unread").get_attribute("text")
        assert_equal(el, u"已读", msg=u"状态验证失败")            
        print el+u" 阅读状态验证成功"
        el = self.driver.find_element_by_id("tv_read_unread")#状态
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()    
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除
        #发送阅后即焚图片
        self.driver.find_element_by_id("chatting_attach_btn").click()
        self.driver.find_element_by_name(u"阅后即焚").click()
        self.driver.find_element_by_name(u"从相册选择").click()
        self.driver.find_element_by_name("image").click()
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/checkmark").click()#点击选中
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_send").click()#点击发送
        
        self.driver.press_keycode('4')#点击返回键
        #self.driver.find_element_by_id("chatting_content_itv").click()  
        time.sleep(2)
        logout.test_logout(self)#退出登录
        login.test_login(self,phoneid="13366778604")#使用账号receive登录
        
        time.sleep(2)
        self.driver.find_element_by_name("[图片]").click()
        self.driver.find_element_by_id("chatting_content_iv").click()
        time.sleep(2)
        self.driver.press_keycode('4')#点击返回键   
        print "Start : %s" % time.ctime()#输出当前时间  
        time.sleep(2)
        print "Stop : %s" % time.ctime()#输出当前时间   
        #获取点击后的图片
        #self.test_get_screen_by_element()
        #对比焚毁的图片
        #self.test_same_as()
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
        logout.test_logout(self)#退出登录        


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