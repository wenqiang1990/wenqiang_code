#coding:utf-8
import time
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
#from test_a_login import Imtest
from public import login
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

        #获得机器屏幕大小x,y
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        l=[x,y]
        print l
        with open('F:\Appium\size\size.txt','w') as f:
            for i in range(len(l)):
                f.write(str(l[i])+'\n')                         
                print l[i]
            f.close()
    def swipLeft(self,t):
        #l=[1080,1980]       
        with open('F:\Appium\size\size.txt','r') as f:
            l = f.readlines()
            for i in range(len(l)):
                l[i] = int(l[i][:len(l[i])-1])
            print l                     
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

    
    def test_creategroup(self):
        '''按群组ID查找群组''' 
        driver = self.driver
        time.sleep(2)
        #Imtest.test_login(phoneid="13366778605")
        #test_a_login#调用登录
        login.test_login(self,el="13366778604")
        #查找群组 
        #self.swipLeft(500)#左划
        #self.swipLeft(500)#左划
        with open('F:\Appium\group\groupID.txt','r') as f:
            el=f.read()
        driver.find_element_by_id("btn_plus").click()#加号
        driver.context#可以定位到悬浮窗口
        driver.find_element_by_name(u"查找群组").click()
        driver.find_element_by_name(u"按群组ID精确查询").click()
        driver.find_element_by_id("search_flite").send_keys(el)#加号
        driver.find_element_by_id("text_right").click()#点击确定
        time.sleep(2)    
        driver.find_element_by_id("group_name").click()#点击群组加入
        driver.find_element_by_id("red_btn").click()#点击申请加入
        driver.find_element_by_id("btn_right").click()#点击申请加入
        el=driver.find_element_by_xpath("//android.widget.ScrollView//android.widget.TextView[@text='13671378634']").get_attribute("text")#查找选择组成员
        print "账号"+el+"加入群组成功"
        self.driver.press_keycode('4')#点击返回键
        #logout.test_logout(self)#退出登录
                   


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
    def runTest(self):
        pass
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_creategroup"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      