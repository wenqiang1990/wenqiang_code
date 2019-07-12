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
from set_driver import set_driver
from clear_massage import clear_massage 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)        

    def test_setsex(self):  
        '''设置性别''' 
        driver = self.driver
        time.sleep(2)
        member = "17600645696"  #被@成员账号
        time.sleep(2) 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_my").click()#点击我的
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/self_info").click()#点击个人信息
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_sex").click()#点击性别
        time.sleep(2) 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/cb_nan").click()#点击性别女
        driver.find_element_by_name(u"保存").click()#点击保存
        time.sleep(2)
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_my_sex").get_attribute("text")
        assert_equal(el,u"女",msg=u'消息验证失败')
        print u"set sex women success"           
          
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_setsex"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      