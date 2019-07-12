#coding:utf-8
import time
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
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
        login.test_login(self,el="13311267857") #登录
        
        #driver.find_element_by_id("btn_left").click()    
        driver.find_element_by_id("btn_plus").click()#加号
        time.sleep(2)
        driver.context#可以定位到悬浮窗口    
        driver.find_element_by_name(u"创建讨论组").click()
        #driver.tap([(640,725)], )#点击创建讨论组
        time.sleep(2)
        driver.find_element_by_id("name_tv").click()#选择联系人
        driver.find_element_by_xpath("//android.widget.TextView[@text='13671378634']").click()#选择联系人
        #driver.find_element_by_xpath("//android.widget.TextView[@text='001']").click()#选择联系人
        driver.find_element_by_id("text_right").click()#点击确定
        driver.find_element_by_id("btn_right").click()#点击群组图标
        
        #踢出第一个群组成员
        driver.find_element_by_id("remove_btn").click()#点击踢出
        driver.find_element_by_id("dilaog_button3").click()#点击确认
        el=driver.find_element_by_id("group_count").get_attribute("text")
        assert_equal(el,u"成员个数(2)", msg=u"成员数不正确")
        print u"系统通知角标显示"+el+"正确"        

  
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