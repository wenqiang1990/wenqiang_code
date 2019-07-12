#coding:utf-8
import time
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {}
        desired_caps['deviceName'] = '3a11d697'  
        desired_caps['platformName'] = 'Android'   
        desired_caps['platformVersion'] = '5.1.1'
        #desired_caps['unicodeKeyboard'] = "true"#使用 Unicode 输入法。默认值false
        #desired_caps['resetKeyboard'] = "true"#在设定了 unicodeKeyboard 关键字的 Unicode 测试结束后，重置输入法到原有状态。如果单独使用，将会被忽略。默认值 false   
        desired_caps['appPackage'] = 'com.yuntongxun.ecdemo'  
        desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.LauncherActivity' 
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(30)        

    
    def test_creategroup(self):
        '''创建讨论组''' 
        driver = self.driver
        #查找联系人
        time.sleep(5) 
        #退出
        #driver.find_element_by_id("btn_left").click()    
        driver.find_element_by_id("btn_plus").click()#加号
        time.sleep(2)
        driver.context#可以定位到悬浮窗口    
        driver.find_element_by_name(u"视频会议").click()
        time.sleep(2)
        driver.find_element_by_id("text_right").click()#点击创建会议
        driver.find_element_by_name(u"请输入房间名称").send_keys("999")
        driver.press_keycode('4')
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.ecdemo:id/create_video_c_submit").click()
        time.sleep(2)
        el=driver.find_element_by_id("btn_middle").get_attribute("text")
        if el == u"视频会议聊天":
            print u'创建视频会议成功'
        else:
            print u'创建视频会议失败'
        driver.find_element_by_id("com.yuntongxun.ecdemo:id/out_video_c_submit").click()
        driver.find_element_by_name(u"退出视频会议").click()

  
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
   
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_creategroup"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      