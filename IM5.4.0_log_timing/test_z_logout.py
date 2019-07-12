#coding:utf-8
import time
import datetime 
import unittest
from appium import webdriver
from public import login
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
 
class Imtest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['deviceName'] = '3a11d697'# 3a11d697 ：红米note3
        desired_caps['udid'] = '3a11d697' #设备的udid 实际控制启动哪台机器
        desired_caps['platformName'] = 'Android'   
        desired_caps['platformVersion'] = '5.1.1'   
        desired_caps['appPackage'] = 'com.yuntongxun.eckuailiao' #com.yuntongxun.eckuailiao
        desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.account.SplashActivity'#com.yuntongxun.ecdemo.ui.phonemodel.PhoneUI#com.yuntongxun.ecdemo.ui.account.LoginActivity
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(10)  


    def test_logout(self):
        '''退出当前账号''' 
        #login.test_login(self,phoneid="13311267857")
        driver = self.driver
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_my").click()#点击我的
        time.sleep(2)
        driver.context#可以定位到悬浮窗口
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_my_setting").click()#设置
        driver.find_element_by_name(u"退出当前账号").click()
        driver.find_element_by_id("dilaog_button3").click()
        print "退出登录"

  
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