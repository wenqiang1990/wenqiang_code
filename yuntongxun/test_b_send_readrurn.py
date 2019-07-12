#coding:utf-8
import time,os
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
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
        #获得机器屏幕大小x,y
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        l=[x,y]
        with open('F:\Appium\size\size.txt','w') as f:
            for i in range(len(l)):
                f.write(str(l[i])+'\n')                         
            f.close()
    def swipLeft(self,t):
        #l=[1080,1980]       
        with open('F:\Appium\size\size.txt','r') as f:
            l = f.readlines()
            for i in range(len(l)):
                l[i] = int(l[i][:len(l[i])-1])                   
        x1=int(l[0]*0.75)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.05)
        print [x1,y1,x2,y1]
        self.driver.swipe(x1,y1,x2,y1,t)
    def swipeUp(self,t):
        with open('F:\Appium\size\size.txt','r') as f:
            l = f.readlines()
            for i in range(len(l)):
                l[i] = int(l[i][:len(l[i])-1])
        x1=int(l[0]*0.5)  #x坐标
        y1=int(l[1]*0.75)   #起始y坐标
        y2=int(l[1]*0.25)   #终点y坐标
        self.driver.swipe(x1,y1,x1,y2,t)           
        
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
    
    def test_send_readrurn(self):
        '''发送阅后即焚'''
        login.test_login(self,el="13311267857") 
        self.driver.find_element_by_name(u"[图片]").click()
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
        self.driver.find_element_by_name(u"选择相册").click()
        self.driver.find_element_by_id("imageview_photo").click()
        self.driver.find_element_by_id("text_right").click()
        
        self.driver.press_keycode('4')#点击返回键
        #self.driver.find_element_by_id("chatting_content_itv").click()  
        time.sleep(2)
        logout.test_logout(self)#退出登录
        login.test_login(self,el="13366778604")#使用账号receive登录
        
        time.sleep(2)
        self.driver.find_element_by_name("13311267857").click()
        self.driver.find_element_by_id("chatting_content_iv").click()
        time.sleep(2)
        self.driver.press_keycode('4')#点击返回键        
        #获取点击后的图片
        self.test_get_screen_by_element()
        #对比焚毁的图片
        self.test_same_as()
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