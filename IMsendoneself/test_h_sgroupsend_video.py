#coding:utf-8
import time
import datetime 
import unittest
from robot.utils.asserts import *
from appium import webdriver
from public import swip
from appium.webdriver.common.touch_action import TouchAction
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

    
    def test_send_txt(self):
        '''查找联系人，发送文本消息''' 
        #查找联系人
        time.sleep(5) 
        swip.swipLeft(self,500)#左划
        time.sleep(2)
        swip.swipLeft(self,500)#左划
        self.driver.find_element_by_id("group_name").click()
        wq = self.driver.find_element_by_id("chatting_attach_btn")
        assert_not_none(wq,u"未定位到加号按钮")
        wq.click()
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