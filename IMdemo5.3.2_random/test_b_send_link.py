#coding:utf-8
import time
import datetime 
import unittest
from robot.utils.asserts import *
from appium import webdriver
from public import logout
from public import login
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

        #获得机器屏幕大小x,y
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        l=[x,y]
        print l
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
    #屏幕向上滑动
    def swipeUp(self,t):
        with open('F:\Appium\size\size.txt','r') as f:
            l = f.readlines()
            for i in range(len(l)):
                l[i] = int(l[i][:len(l[i])-1])
        x1=int(l[0]*0.5)  #x坐标
        y1=int(l[1]*0.75)   #起始y坐标
        y2=int(l[1]*0.25)   #终点y坐标
        self.driver.swipe(x1,y1,x1,y2,t)        

    
    def test_send_txt(self):
        '''发送链接消息''' 
        time.sleep(2) 
        #发送文本链接消息  
        login.test_login(self,el="13311267857") 
        self.driver.find_element_by_name("a1").click()
        el=self.driver.find_element_by_id("tv_read_unread").get_attribute("text")
        assert_equal(el, u"已读", msg=u"阅读状态验证失败")            
        print el+u" 阅读状态验证成功"
        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()    
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除
                
        self.driver.find_element_by_id("chatting_content_et").send_keys("https://www.baidu.com")
        time.sleep(2)
        self.driver.find_element_by_id("chatting_send_btn").click()
        self.driver.press_keycode('4')#点击返回键
        #self.driver.find_element_by_id("chatting_content_itv").click()  
        time.sleep(2)
        logout.test_logout(self)#退出登录
        login.test_login(self,el="13366778604")#使用账号receive登录
        time.sleep(2)
        self.driver.find_element_by_name("https://www.baidu.com").click()
        self.driver.find_element_by_id("chatting_content_itv").click()
        el=self.driver.contexts#获取H5页面
        print el
        el=self.driver.find_element_by_id("btn_middle").get_attribute("text")
        assert_equal(el, u"下载", msg=u"访问链接失败")            
        print u"访问链接成功"
        self.driver.press_keycode('4')#点击返回键
        el = self.driver.find_element_by_id("chatting_content_itv")
        action1.long_press(el,duration=5000).perform()        
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()   
        self.driver.press_keycode('4')#点击返回键
        logout.test_logout(self)#退出登录
        
        
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