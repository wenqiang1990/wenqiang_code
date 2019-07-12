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
        self.driver.implicitly_wait(30)        

    
    def test_send_video(self):
        '''发送小视频''' 
        time.sleep(5)
        swip.swipLeft(self,500)#左划
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/card_item_tv").click()
        self.driver.find_element_by_id("content").click()
        self.driver.find_element_by_id("content").send_keys("13311267857")
        self.driver.find_element_by_id("text_right").click()          
        #发送小视频
        time.sleep(5)
        self.driver.find_element_by_id("chatting_attach_btn").click()
        time.sleep(2)
        photograph_x=self.driver.find_element_by_name(u"拍照").location.get('x')
        photograph_y=self.driver.find_element_by_name(u"拍照").location.get('y')
        print photograph_x,photograph_y
        photograph_x=int(photograph_x)
        photograph_y=int(photograph_y)-100
        print photograph_x,photograph_y
        self.driver.tap([(photograph_x,photograph_y)], )#点击
        self.driver.find_element_by_name(u"录制小视频").click()
        self.driver.find_element_by_id("switch_btn").click()
        time.sleep(2)
        self.driver.find_element_by_id("start").click()
        time.sleep(10)#录制10秒小视频
        self.driver.find_element_by_id("stop").click()
        time.sleep(2)
        self.driver.find_element_by_id("text_right").click()
        
        el=self.driver.find_element_by_id("tv_read_unread").get_attribute("text")
        assert_equal(el, u"已读", msg=u"状态验证失败")            
        print el+u" 阅读状态验证成功"
        el = self.driver.find_element_by_id("tv_read_unread")#状态
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()    
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除
        
        time.sleep(2)
        self.driver.find_element_by_id("iv_file_mp4").click()
        time.sleep(3)
        self.driver.find_element_by_id("iv_file_mp4").click()
        time.sleep(5)
        self.driver.press_keycode('4')#点击返回键        
        #获取点击后的图片
        time.sleep(2)
        print u"接收小视频成功"        
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