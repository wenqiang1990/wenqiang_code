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
    #屏幕向上滑动
    def swipeUp(self,t):
        l=[1080,1980]
        x1=int(l[0]*0.5)  #x坐标
        y1=int(l[1]*0.75)   #起始y坐标
        y2=int(l[1]*0.25)   #终点y坐标
        self.driver.swipe(x1,y1,x1,y2,t)

    def test_creategroup(self):  
        '''创建群组只填写名称''' 
        driver = self.driver
        time.sleep(5) 
        #driver.find_element_by_id("btn_left").click()    
        driver.find_element_by_id("btn_plus").click()#加号
        time.sleep(2)
        driver.context#可以定位到悬浮窗口    
        driver.find_element_by_name(u"创建群组").click()
        #driver.tap([(640,725)], )#点击创建群组
        time.sleep(2)
        driver.find_element_by_id("group_name").send_keys("11111111")
        driver.find_element_by_id("group_notice").send_keys("groupannouncement")
        #driver.find_element_by_id("group_provice").send_keys("province")
        #driver.find_element_by_id("group_city").send_keys("groupcity")
        #driver.find_element_by_id("group_city").click()
        #driver.press_keycode(4)
        #driver.find_element_by_id("str_group_type").click()#选择所属类型
        #driver.find_element_by_name(u"朋友").click()#选择所属类型
        #driver.find_element_by_id("str_group_permission_spinner2").click()#点击加入方式
        #driver.find_element_by_name(u"需要身份验证").click()#选择加入方式
        driver.find_element_by_id("create").click()#点击创建
        driver.find_element_by_id("name_tv").click()#选择联系人
        driver.find_element_by_xpath("//android.widget.TextView[@text='13671378634']").click()#选择联系人
        #driver.tap([(500,570)], )#选择联系人
        driver.find_element_by_id("text_right").click()#点击确定
        driver.find_element_by_id("btn_right").click()#点击群组图标
        el=driver.find_element_by_id("btn_middle").get_attribute("text")#群组名称
        print el
        time.sleep(5)
        assert_equal(el,u"11111111(3)",msg=u"群组名称验证失败")
        print u"群名称显示为------"+el
        el=driver.find_element_by_xpath("//android.widget.ScrollView//android.widget.TextView[@text='13366778604']").get_attribute("text")#查找选择组成员
        print u"群成员之一为------"+el
        #el=driver.find_element_by_xpath("//android.widget.ScrollView//android.widget.TextView[@text='I am a nickname[创建者]']").get_attribute("text")#查找选择组成员
        #print u"创建者显示为------"+el
        driver.find_element_by_name(u"群聊名片").click()
        el=driver.find_element_by_id("accessory_checked").get_attribute("text")#群组名id
        print "群组id为------"+el
        #将群组id保存到本地
        with open('F:\Appium\group\groupID.txt','w') as f:
            f.write(el)
        driver.find_element_by_id("btn_left").click()#back
        #el=el[-12:]
 
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