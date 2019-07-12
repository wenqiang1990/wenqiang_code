#coding:utf-8
import time
import re
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
from public import swip
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {}
        desired_caps['deviceName'] = '3a11d697'  
        desired_caps['platformName'] = 'Android'   
        desired_caps['platformVersion'] = '5.1.1'   
        desired_caps['appPackage'] = 'com.yuntongxun.ecdemo'  
        desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.LauncherActivity' 
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(10)
    
    def test_send_expression(self):
        '''查找联系人，发送表情'''
        #login.test_login(self,el="13311267857") 
        time.sleep(5)
        swip.swipLeft(self,500)#左划
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/card_item_tv").click()
        self.driver.find_element_by_id("content").click()
        self.driver.find_element_by_id("content").send_keys("13311267857")
        self.driver.find_element_by_id("text_right").click()
        time.sleep(3)
        #all=self.driver.page_source
        action1 = TouchAction(self.driver)
        try:
            #wq=str(self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/chatting_avatar_iv"))#头像
            itv=str(self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/chatting_content_itv"))#文字表情图片等
            #filesize=str(self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/tv_filesize"))#视频大小等
            while itv:
                el=self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/chatting_content_itv")#文字
                action1.long_press(el,duration=5000).perform()
                self.driver.find_element_by_name(u"删除").click()
                self.driver.find_element_by_id("dilaog_button3").click()              
        except:
            self.driver.press_keycode('4')#点击返回键
            time.sleep(2)
            self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/card_item_tv").click()
            self.driver.find_element_by_id("content").click()
            self.driver.find_element_by_id("content").send_keys("13311267857")
            self.driver.find_element_by_id("text_right").click()          
            print u"已经无历史数据"                 

            elif filesize:
                while filesize:
                    el=self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/tv_filesize")#文字
                    action1.long_press(el,duration=5000).perform()
                    self.driver.find_element_by_name(u"删除").click()
                    self.driver.find_element_by_id("dilaog_button3").click()   
                    
        except:
            self.driver.press_keycode('4')#点击返回键
            time.sleep(2)
            self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/card_item_tv").click()
            self.driver.find_element_by_id("content").click()
            self.driver.find_element_by_id("content").send_keys("13311267857")
            self.driver.find_element_by_id("text_right").click()          
            print u"已经无历史数据" 
                        
        #发送表情 
        self.driver.find_element_by_id("chatting_content_et").click()
        el=self.driver.find_element_by_id("chatting_smiley_btn")
        self.assertIsNotNone(el,msg=u"定位表情切换图标失败")
        el.click()#点击切换到表情输入
        time.sleep(2)
   
        self.driver.find_element_by_name("😄").click()#点击表情
        self.driver.find_element_by_id("chatting_send_btn").click()
        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()  
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()    

        el=self.driver.find_element_by_id("chatting_content_itv").get_attribute("text")
        assert_equal(el, "😄", msg=u"接收表情失败")            
        print u"接收表情成功" + el

        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()  
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()
        self.driver.press_keycode('4')#点击返回键       
  
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_expression"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      