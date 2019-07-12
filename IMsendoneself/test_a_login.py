#coding:utf-8
import datetime 
import unittest
from appium import webdriver

class Imtest(unittest.TestCase):   
    def setUp(self):    
        desired_caps = {}
        desired_caps['deviceName'] = '3a11d697'# 3a11d697 ：红米note3
        desired_caps['platformName'] = 'Android'   
        desired_caps['platformVersion'] = '5.1.1'   
        desired_caps['appPackage'] = 'com.yuntongxun.ecdemo'  
        desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.LauncherActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(10) 
  
    def test_login(self,phoneid="13311267857"):#13366778606
        '''登陆''' 
        self.driver.find_element_by_id("edittext").set_text(phoneid)#timecode
        self.driver.find_element_by_id("sign_in_button").click()#点击登陆                     
        print u"成功点击登陆" 
         

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