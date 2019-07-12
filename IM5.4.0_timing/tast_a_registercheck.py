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
from set_driver import set_driver
 
class Imtest(unittest.TestCase):
    #def __init__(self,driver):
        #self.driver = driver     
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)                  
               
    def test_send_massage(self):
        '''查找联系人，发送文本消息'''
        driver = self.driver
        #try:
            #logout.test_logout(self)#退出登录
        #except:
           #print "未登录，无需执行退出登录操作"      
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/bu_register").click()
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_name").send_keys("11111111111")
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_getcode").click()#点击获取验证码
        el=[]
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_getcode").get_attribute("text")
        el=el[2]
        print el
        assert_equal(el,u"秒",msg=u'点击验证码后显示不对')
        print "验证码变化正确"              
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_yanzhengma").send_keys("222222")#输入了固定错误验证码
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_pwd").send_keys("11111111111111111111111111111111")#输入最大32位密码
        print "输入最大32位密码"
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_pwd").get_attribute("text")
        assert_equal(el,"",msg=u'密码没有加密显示')
        print "密码加密显示" 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_regi").click()#点击注册

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_massage"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      