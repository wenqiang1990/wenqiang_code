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
        desired_caps['appPackage'] = 'com.yuntongxun.ecdemo'  
        desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.LauncherActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(30)

    #屏幕向上滑动
    def swipeUp(self,t):
        l=[1080,1980]
        x1=int(l[0]*0.5)  #x坐标
        y1=int(l[1]*0.75)   #起始y坐标
        y2=int(l[1]*0.25)   #终点y坐标
        self.driver.swipe(x1,y1,x1,y2,t)

    def test_logout(self,el="13311267857"):
        '''设置个人信息''' 
        driver = self.driver
        #退出
        #driver.find_element_by_id("btn_left").click()    
        driver.find_element_by_id("btn_plus").click()#加号
        time.sleep(2)
        driver.context#可以定位到悬浮窗口 
        driver.find_element_by_name(u"设置").click()  
        #driver.tap([(590,1190)], )#点击设置
        time.sleep(2)
        driver.find_element_by_id("text_right").click()           
        #设置个人信息
        driver.find_element_by_xpath("//android.widget.EditText[@text='昵 称']").set_text(el)
        driver.find_element_by_xpath("//android.widget.EditText[@text='I am signature']").set_text("I am signature")
        driver.find_element_by_id("sign_in_button").click()
        el=driver.find_element_by_name(u"沟通").get_attribute("text")
        assert_equal(el, u"沟通", msg=u"登陆失败")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_logout"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)


