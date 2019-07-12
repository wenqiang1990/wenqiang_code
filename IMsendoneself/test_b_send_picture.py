#coding:utf-8
import time,os
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from public import login
from public import logout
from public import swip
from appium import webdriver
from extend import Appium_Extend
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
        self.extend = Appium_Extend(self.driver)               

    def test_get_screen_by_element(self):  
        element = self.driver.find_element_by_id("chatting_content_iv")  
        self.extend.get_screenshot_by_element(element).write_to_file("f:\\screen", "image1") 
        #assert_true(os.path.isfile("f:\\screen\\image1.jpg"))  
  
    def test_same_as(self):  
        element = self.driver.find_element_by_id("chatting_content_iv")#chatting_content_iv
        load = self.extend.load_image("f:\\screen\\image1.jpg")
        #要求百分百相似  
        result = self.extend.get_screenshot_by_element(element).same_as(load, 0)  
        assert_true(result)

    def test_send_picture(self):
        '''发送图片'''
        time.sleep(5)
        swip.swipLeft(self,500)#左划
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/card_item_tv").click()
        self.driver.find_element_by_id("content").click()
        self.driver.find_element_by_id("content").send_keys("13311267857")
        self.driver.find_element_by_id("text_right").click()
        
        #发送图片
        self.driver.find_element_by_id("chatting_attach_btn").click()
        self.driver.find_element_by_id("app_grid_item_icon_mask").click()
        self.driver.find_element_by_id("imageview_photo").click()
        self.driver.find_element_by_id("text_right").click()
        time.sleep(2)
        self.test_get_screen_by_element()#获取图片保存到本地
        #删除发送的图片  
        el = self.driver.find_element_by_id("tv_read_unread")#状态
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()    
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除

        time.sleep(2)
        self.test_same_as()

        #接收到的图片对比发送的图片 
        #self.test_get_screen_by_element()#获取接收到的图片保存到本地  
        print u"接收图片成功"
        
        x1=self.driver.find_element_by_id("chatting_content_iv").location.get('x')
        y1=self.driver.find_element_by_id("chatting_content_iv").location.get('y')
        print x1,y1
        x1=int(x1)+400
        y1=int(y1)+100
        print x1,y1
        
        self.driver.tap([(x1,y1)],5000)
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除               

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_picture"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      