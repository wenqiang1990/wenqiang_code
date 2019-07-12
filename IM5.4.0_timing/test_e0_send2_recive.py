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
    
    def test_receive_massage(self):  
        '''群成员接收各种类型消息''' 
        logout.test_logout(self)#退出登录
        time.sleep(2)
        login.test_login(self,phoneid="13311267857")        
        clear_massage(self,name=u"系统通知")
        driver = self.driver
        with open('F:\Appium\group\groupID.txt','r') as f:
            el=f.read()
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        el=u"群组id:"+el
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组id,以后改为读取上一条用例创建群组的id
        #driver.find_element_by_name(el).click()#点击群组id,以后改为读取上一条用例创建群组的id 
        print "Start : %s" % time.ctime()#输出当前时间
        time.sleep(2)
        print "Stop : %s" % time.ctime()#输出当前时间  
        #验证接收消息
        driver.swipe(600,300,600,1500,500)#下划 
        time.sleep(2)
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv").get_attribute("text")
        assert_equal(el,u"中文1234567890ABCDEFGHIJKLMNOPQRSTUCWXYZabcdefghijklmnopqrstuvwxyz！#￥%……",msg=u'消息验证失败')
        print "群组内接收消息%s成功" % el
        #删除接收消息     
        action1 = TouchAction(self.driver)
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv")
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()
        #验证接收表情消息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv").get_attribute("text")
        assert_equal(el,"😄",msg=u'消息验证失败')
        print "群组内接收表情消息成功"   
        #删除表情消息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()         
        #验证接收语音消息
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_voice_play_anim_tv").click() 
        time.sleep(5)
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_user_tv")#发送者昵称
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除 
        
        #验证接收图片消息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_user_tv")#发送者昵称
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除        
        
        #验证接收短视频消息
        #self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_play_video").click() 
        #time.sleep(5)
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_user_tv")#发送者昵称
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除
        #发送群消息1，为下一脚本群组置顶
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_et").send_keys('1')#输入特殊字符
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_send_btn").click()#点击发送        
        
                     
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_receive_massage"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      