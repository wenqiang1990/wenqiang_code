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
from clear_massage import clear_allmassage 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)        

    
    def test_set_administrator(self):  
        '''设置群组管理员''' 
        driver = self.driver
        time.sleep(2)
        member = "13366778604"  #被设置成管理员账号
        clear_allmassage(self,id="com.yuntongxun.eckuailiao:id/nickname_tv")#清空消息记录
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组id,以后改为读取上一条用例创建群组的id 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理  
        time.sleep(2)
        #设置群组管理员
        driver.find_element_by_name(u"设置管理员").click()#点击设置群组管理员
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_note").click()#点击添加管理员
        driver.find_element_by_name(member).click()#点击成员
        driver.press_keycode('4')
        time.sleep(2)
        driver.press_keycode('4')
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_left").click()#群组内返回按钮
        time.sleep(2)
        driver.press_keycode('4')
        time.sleep(2)
        driver.press_keycode('4')
        logout.test_logout(self)#退出登录
        login.test_login(self,phoneid = member)#被设置成管理员账号登录
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组id,以后改为读取上一条用例创建群组的id 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理 
        el=driver.find_element_by_name(u"设置群内禁言").get_attribute("text")
        assert_equal(el,u"设置群内禁言",msg=u'发送的消息验证失败')
        print "设置群组管理员成功"
        
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_set_administrator"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      