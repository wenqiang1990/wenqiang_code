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

    
    def test_send_picture(self):  
        '''群成员发送图片消息''' 
        clear_massage(self,name="groupname1")
        clear_massage(self,name=u"系统通知")
        driver = self.driver
        with open('F:\Appium\group\groupID.txt','r') as f:
            el=f.read()
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        el=u"群组id:"+el
        driver.find_element_by_name(el).click()#点击群组id,以后改为读取上一条用例创建群组的id 
        #群成员发送图片
        self.driver.find_element_by_id("chatting_attach_btn").click()#点击加号
        self.driver.find_element_by_name(u"相册").click()#点击相册
        self.driver.find_element_by_name("image").click()
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/checkmark").click()#点击选中
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_send").click()#点击发送
        print "Start : %s" % time.ctime()#输出当前时间
        time.sleep(5)
        print "Stop : %s" % time.ctime()#输出当前时间
        #self.test_get_screen_by_element()#获取图片保存到本地
        #删除发送的图片  
        el = self.driver.find_element_by_id("tv_read_unread")#状态
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()    
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_picture"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      