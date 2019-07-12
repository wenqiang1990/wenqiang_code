#coding:utf-8
import os
import time
import datetime 
import unittest
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
        desired_caps['appPackage'] = 'com.yuntongxun.yuya'  
        desired_caps['appActivity'] = 'com.yuntongxun.yuya.ui.guilder.SplashActivity' 
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(10) 

    def swipLeft(self,t):
        l=[1080,1980]
        x1=int(l[0]*0.75)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.05)
        print [x1,y1,x2,y1]
        self.driver.swipe(x1,y1,x2,y1,t)
    
           
    def test_login(self):   
        '''我的——用户信息设置——修改密码'''
        try:
            self.driver.find_element_by_id("cancel_button").click()
        except:
            print u"没有出现【检测到阿尔法卡是否登录弹窗】"  
        number = self.driver.find_element_by_id("activity_amin_rb3")#点击我的
        self.assertIsNotNone(number)
        number.click()
        self.driver.find_element_by_xpath("//android.widget.ImageButton").click()#点击修改按钮
   
        #强制等待
        print "Start : %s" % time.ctime()
        time.sleep(2)
        print "End : %s" % time.ctime()
        self.driver.find_element_by_name(u"修改密码").click()#点击修改密码      
        self.driver.find_element_by_id("yy_xiugai_pwd").click()
        self.driver.find_element_by_id("yy_xiugai_pwd").send_keys("111111")
        self.driver.find_element_by_id("yy_xiugai_pwd_new").click()
        self.driver.find_element_by_id("yy_xiugai_pwd_new").send_keys("111111")
        self.driver.find_element_by_id("yy_xiugai_pwd_again").click()
        self.driver.find_element_by_id("yy_xiugai_pwd_again").send_keys("111111")      
        self.driver.press_keycode("4")
        self.driver.find_element_by_id("bu_modify").click()#点击提交
        #重新登陆操作
        try:
            self.driver.find_element_by_id("cancel_button").click()
        except:
            print u"没有出现【检测到阿尔法卡是否登录弹窗】"            
        self.driver.find_element_by_id("ed_pwd").send_keys("111111")
        self.driver.find_element_by_id("btn_submit").click()#点击登录     
        #强制等待
        print "Start : %s" % time.ctime()
        time.sleep(2)
        print "End : %s" % time.ctime()
        el=self.driver.find_element_by_id("yy_pcenter_userid").get_attribute("text")
        assert_equal(el, "13311267857", msg=u"登录账号验证失败")
        print u"登录账号是+++++++++"+el+"+++++++++"       
        
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_login"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)   