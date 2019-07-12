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
    
    def test_git_status(self):  
        '''已读未读消息列表展示''' 
        driver = self.driver
        time.sleep(2)
        member = "17600645696"  #被@成员账号
        time.sleep(2) 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_discussion").click()#点击讨论组
        '''with open('F:\Appium\group\groupID.txt','r') as f:
            el=f.read()
        el="讨论组id:"+el
        print el        
        driver.find_element_by_name(el).click()#点击群组id,以后改为读取上一条用例创建群组的id'''
        #driver.find_element_by_name(u"讨论组一号").click()
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击讨论组
        #查看未读消息 成员列表
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"查看已读未读").click()
        self.driver.find_element_by_name(u"未读").click()
        time.sleep(2)
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/messageAccount").get_attribute("text")
        assert_equal(el,u"温强",msg=u'消息验证失败')
        print u"未读消息列表展示成员成功"   
        #查看已读消息成员列表，此处后期需加入图片对比
        driver.press_keycode('4')
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"查看已读未读").click()
        self.driver.find_element_by_name(u"已读").click()
        time.sleep(2)
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_middle").get_attribute("text")
        assert_equal(el,u"已读列表",msg=u'消息验证失败')        
        print u"已读消息列表成员为空"
            
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_git_status"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      