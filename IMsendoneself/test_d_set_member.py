#coding:utf-8
import time
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import logout
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

    def swipLeft(self,t):
        l=[1080,1980]                           
        x1=int(l[0]*0.75)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.05)
        print [x1,y1,x2,y1]
        self.driver.swipe(x1,y1,x2,y1,t)   
    def swipRight(self,t):
        l=[1080,1980]                           
        x1=int(l[0]*0.75)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.05)
        print [x1,y1,x2,y1]
        self.driver.swipe(x2,y1,x1,y1,t)               
    #屏幕向上滑动
    def swipeUp(self,t):
        l=[1080,1980]
        x1=int(l[0]*0.5)  #x坐标
        y1=int(l[1]*0.75)   #起始y坐标
        y2=int(l[1]*0.25)   #终点y坐标
        self.driver.swipe(x1,y1,x1,y2,t)

    def test_creategroup(self):  
        '''踢出群成员''' 
        driver = self.driver
        time.sleep(5) 
        self.swipLeft(500)
        time.sleep(2)
        self.swipLeft(500)
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.ecdemo:id/group_name").click()#点击群组  
        driver.find_element_by_id("com.yuntongxun.ecdemo:id/btn_right").click()#点击群组管理  
        #转让群组
        action1 = TouchAction(driver)  
        el = driver.find_element_by_name("13671378634")
        action1.long_press(el,duration=5000).perform()#长按成员
        driver.find_element_by_name(u"设为成员").click()
        driver.find_element_by_id("dilaog_button3").click()#点击确认
        time.sleep(2)
        self.driver.press_keycode('4')#点击返回键
        time.sleep(2)
        self.driver.press_keycode('4')#点击返回键 
        self.swipRight(500)
        time.sleep(2)
        self.swipRight(500)
        time.sleep(2)
        el=driver.find_element_by_id("com.yuntongxun.ecdemo:id/last_msg_tv").get_attribute("text")
        x = el.split(']')
        assert_equal(x[1],u"已变更成成员", msg=u"系统通知错误")
        print u"系统通知显示"+el+" 系统通知外部正确"
        driver.find_element_by_id("nickname_tv").click()#id/nickname_tv
        el=driver.find_element_by_id("com.yuntongxun.ecdemo:id/result_summary").get_attribute("text")
        x = el.split(']')
        assert_equal(x[1],u"已变更成成员", msg=u"系统通知错误")
        print u"系统通知显示"+el+"  系统通知内部正确"
        driver.find_element_by_id("text_right").click()#清空         
        self.driver.press_keycode('4')#点击返回键 
        el = self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/nickname_tv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()  
        self.driver.find_element_by_name(u"删除该聊天").click()
        time.sleep(2)            
        #logout.test_logout(self)#退出登录
        
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