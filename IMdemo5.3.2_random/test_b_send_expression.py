#coding:utf-8
import time
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
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
    
    def test_send_expression(self):
        '''查找联系人，发送表情''' 
        time.sleep(5)
        self.swipLeft(500)#左划
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/card_item_tv").click()
        self.driver.find_element_by_id("content").click()
        self.driver.find_element_by_id("content").send_keys("13366778604")
        self.driver.find_element_by_id("text_right").click()
        time.sleep(2)          
        #发送表情 
        self.driver.find_element_by_id("chatting_content_et").click()
        el=self.driver.find_element_by_id("chatting_smiley_btn")
        self.assertIsNotNone(el,msg=u"定位表情切换图标失败")
        el.click()#点击切换到表情输入
        time.sleep(2)
        #driver.tap([(530,1450)], )#点击表情 失败了
        #driver.tap([(80,1255)], )#点击表情          
        self.driver.find_element_by_name("😄").click()#点击表情
        self.driver.find_element_by_id("chatting_send_btn").click()
        self.driver.press_keycode('4')#点击返回键

        logout.test_logout(self)#退出登录
        login.test_login(self,el="13366778604")#使用账号13366778606登录
        self.driver.find_element_by_name("13311267857").click()
        el=self.driver.find_element_by_id("chatting_content_itv").get_attribute("text")
        assert_equal(el, "😄", msg=u"接收表情失败")            
        print u"接收表情成功" + el

        el = self.driver.find_element_by_id("chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()  
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()
        self.driver.press_keycode('4')#点击返回键 
        logout.test_logout(self)#退出登录
        time.sleep(5)        
  
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