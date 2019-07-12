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
        '''成员接收各种类型消息''' 
        try:
            logout.test_logout(self)#退出登录
        except:
            print "未登录，无需执行退出登录操作" 
        time.sleep(2)
        login.test_login(self,phoneid="13366778604")        
        clear_massage(self,name=u"系统通知")
        driver = self.driver
        driver.find_element_by_name("qiuqiu").click()
        print "Start : %s" % time.ctime()#输出当前时间
        time.sleep(2)
        print "Stop : %s" % time.ctime()#输出当前时间  
        #验证接收消息
        driver.swipe(600,300,600,1500,500)#下划 
        time.sleep(2)
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv").get_attribute("text")
        assert_equal(el,u"中文1234567890ABCDEFGHIJKLMNOPQRSTUCWXYZabcdefghijklmnopqrstuvwxyz！#￥%……",msg=u'消息验证失败')
        print "接收消息%s成功" % el
        #删除接收消息     
        action1 = TouchAction(self.driver)
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv")
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()
        #验证接收表情消息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv").get_attribute("text")
        assert_equal(el,"😄",msg=u'消息验证失败')
        print "接收表情消息成功"   
        #删除表情消息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()         
        #验证接收语音消息
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv").click()
        time.sleep(5)
        l = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv").get_attribute("text")
        l=l.split('"')
        l=l[0]
        assert_equal(l,"4",msg=u'消息验证失败')        
        print "接收语音消息成功" 
        #删除语音消息
        x1=self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv").location.get('x')
        y1=self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv").location.get('y')
        print x1,y1
        x1=int(x1)+400
        y1=int(y1)+100
        print x1,y1  
        self.driver.tap([(x1,y1)],5000)
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除   
        
        #删除接收图片消息，验证以后加
        x1=self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_iv").location.get('x')
        y1=self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_iv").location.get('y')
        print x1,y1
        x1=int(x1)+400
        y1=int(y1)+100
        print x1,y1  
        self.driver.tap([(x1,y1)],5000)
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除   
        
        #验证接收短视频消息
        #self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_play_video").click() 
        #time.sleep(5)
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_filesize")#视频大小
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除
         
        #验证接收阅后即焚消息
        x1=self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_iv").location.get('x')
        y1=self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_iv").location.get('y')
        print x1,y1
        x1=int(x1)+400
        y1=int(y1)+100
        print x1,y1
        
        self.driver.tap([(x1,y1)],5000)
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除                      
        
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