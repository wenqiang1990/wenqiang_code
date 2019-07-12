#coding:utf-8
import time
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import swip
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
from set_driver import set_driver
 
class Imtest(unittest.TestCase):
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)  


    def test_logout(self):
        '''退出当前账号''' 
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