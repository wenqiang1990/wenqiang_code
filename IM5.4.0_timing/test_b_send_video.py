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
    
    def test_send_video(self):
        '''发送小视频10秒''' 
        clear_massage(self,name=u"qiuqiu")#删除消息页面，昵称为**的聊天记录
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys("13311267857")
        #self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_my").click()#点击搜索
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").click()#点击账号
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_chat").click()#点击发消息         
        #发送小视频
        time.sleep(5)
        self.driver.find_element_by_id("chatting_attach_btn").click()#点击加号
        time.sleep(2)
        '''
        photograph_x=self.driver.find_element_by_name(u"拍照").location.get('x')
        photograph_y=self.driver.find_element_by_name(u"拍照").location.get('y')
        print photograph_x,photograph_y
        photograph_x=int(photograph_x)
        photograph_y=int(photograph_y)-100
        print photograph_x,photograph_y
        self.driver.tap([(photograph_x,photograph_y)], )#点击
        '''
      
        self.driver.find_element_by_name(u"短视频").click()
        time.sleep(2) 
        action1 = TouchAction(self.driver)  
        el = self.driver.find_element_by_xpath("//android.widget.FrameLayout//android.view.View[2]")
        action1.long_press(el,duration=9000).perform()
        self.driver.find_element_by_xpath("//android.widget.FrameLayout//android.view.View[2]").click()#点击发送         
        time.sleep(10)
        el=self.driver.find_element_by_id("tv_read_unread").get_attribute("text")
        assert_equal(el, u"已读", msg=u"状态验证失败")            
        print el+u" 阅读状态验证成功"
        el = self.driver.find_element_by_id("tv_read_unread")#状态
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()    
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除
        
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_play_video").click()
        time.sleep(5)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_play_video").click()
        time.sleep(5)
        self.driver.press_keycode('4')#点击返回键        
        #获取点击后的图片
        time.sleep(2)
        print u"接收小视频并播放成功"        
        #删除小视频
        el = self.driver.find_element_by_id("tv_filesize")
        action1.long_press(el,duration=5000).perform()        
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click() 
                                                       
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_video"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      