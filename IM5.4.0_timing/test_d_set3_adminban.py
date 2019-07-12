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
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)        

    
    def test_group_ban(self):  
        '''管理员设置群成员禁言''' 
        driver = self.driver
        time.sleep(3)
        member = "17600645696"  #被禁言成员账号
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        time.sleep(1)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组id,以后改为读取上一条用例创建群组的id 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理  
        time.sleep(2)
        #设置群成员禁言
        driver.find_element_by_name(u"设置群内禁言").click()#点击设置群内禁言
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_note").click()#点击添加成员
        driver.find_element_by_name(member).click()#点击成员
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_invite").click()#点击确定
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button3").click()#点击确认
        driver.press_keycode('4')
        time.sleep(2)
        driver.press_keycode('4')
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_left").click()#群组内返回按钮
        driver.press_keycode('4')
        time.sleep(2)
        driver.press_keycode('4')
        time.sleep(2)
        logout.test_logout(self)#退出登录
        login.test_login(self,phoneid = member)#被禁言账号登录
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组id,以后改为读取上一条用例创建群组的id 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_et").send_keys("hello")
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_send_btn").click()#点击发送
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button1").click()#点击确认
        print "被设置禁言用户发送消息，页面弹出[您已经被禁言]提示"
        
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_group_ban"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      