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
import set
import get
from set_driver import set_driver
 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)        

    
    def test_group_dissolve(self):  
        '''转让群组'''     
        driver = self.driver
        logout.test_logout(self)#退出登录
        login.test_login(self,phoneid="13311267857")         
        with open('F:\Appium\group\groupID.txt','r') as f:
            el=f.read()
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        el=u"群组id:"+el
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组id,以后改为读取上一条用例创建群组的id
        #driver.find_element_by_name(el).click()#点击群组id,读取上一条用例创建群组的id 
        #解散群组     
        driver.find_element_by_name(u"群name7？").click()#点击群组 
        time.sleep(2)
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_middle").get_attribute("text")
        assert_equal(el,u'群name7？',msg=u'群组聊天页面群组名称显示不对')
        print u"群组聊天页面群组名称是 【"+el+"】 显示正确"
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理 
        time.sleep(2)
        driver.swipe(600,800,600,100,500)#上划
        driver.find_element_by_name(u"解散该群").click()#点击群组管理        
        driver.find_element_by_name(u"group").click()#点击群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理 
        driver.find_element_by_name(u"转让群组").click()#点击转让
        driver.find_element_by_name("17600645696").click()#点击转让
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button3").click()#点击转让       
        self.driver.press_keycode('4')#点击返回
        time.sleep(2)
        self.driver.press_keycode('4')#点击返回
        time.sleep(2)
        self.driver.press_keycode('4')#点击返回
        time.sleep(2)
        self.driver.press_keycode('4')#点击返回
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_tab_msg").click()#点击消息
        driver.find_element_by_name(u"系统通知").click()#点击系统通知
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/result_summary").get_attribute("text")
        assert_equal(el,u"[group的联通]已变更成群主",msg=u'系统通知显示不对')
        print "系统通知显示   "+el+"正确"
        
         
        #logout.test_logout(self)#退出登录
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_group_dissolve"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      