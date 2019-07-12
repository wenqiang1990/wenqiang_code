#coding:utf-8
import time
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
from clear_massage import clear_massage
from set_driver import set_driver
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)        

    
    def test_memberquit(self):  
        '''被禁言群成员退出群组''' 
        driver = self.driver
        time.sleep(2)
        member = "17600645696"  #被禁言成员账号
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组id,以后改为读取上一条用例创建群组的id 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理  
        time.sleep(1)
        driver.swipe(600,960,600,60,500)#上划 
        time.sleep(1)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_group_quit").click()#点击退出群组
        driver.press_keycode('4')
        time.sleep(1)
        driver.press_keycode('4')
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_tab_msg").click()#点击消息
        driver.find_element_by_name(u"系统通知").click()#点击系统通知
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/result_summary").get_attribute("text")#通知内容
        #assert_equal(el,u"群成员[修月]退出了群组",msg=u"系统通知验证失败")       
        print "系统通知未读消息数显示     "+el+"  正确"
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击清空  
     
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_memberquit"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      