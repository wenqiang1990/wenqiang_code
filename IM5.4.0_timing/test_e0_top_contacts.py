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
        '''联系人置顶''' 
        driver = self.driver
        print "Start : %s" % time.ctime()#输出当前时间
        time.sleep(2)
        print "Stop : %s" % time.ctime()#输出当前时间
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        driver.find_element_by_name(u"温强").click()#点击名字
        driver.find_element_by_name(u"发消息").click()#点击
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_et").send_keys("1")#hello tester
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_send_btn").click()#发送 
        driver.press_keycode('4')
        time.sleep(1)
        driver.press_keycode('4')
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_tab_msg").click()#消息
        time.sleep(1)         
        el=driver.find_element_by_name(u"温强")#定位名字
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        driver.find_element_by_name(u"置顶聊天").click()  
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/nickname_tv").get_attribute('text')
        assert_equal(el,u"温强",msg=u'置顶消息验证失败')
        print u"联系人置顶成功"
        #取消置顶
        el=driver.find_element_by_name(u"温强")#定位名字
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        driver.find_element_by_name(u"取消置顶").click()
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/nickname_tv").get_attribute('text')
        assert_equal(el,u"系统通知",msg=u'置顶消息验证失败')
        print u"联系人取消置顶成功"  
        el=driver.find_element_by_name(u"group")#定位名字
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        driver.find_element_by_name(u"置顶聊天").click()  
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/nickname_tv").get_attribute('text')
        assert_equal(el,"group",msg=u'置顶消息验证失败')
        print u"联系人为群组置顶成功"
        #取消置顶
        el=driver.find_element_by_name(u"group")#定位名字
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        driver.find_element_by_name(u"取消置顶").click()
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/nickname_tv").get_attribute('text')
        assert_equal(el,u"系统通知",msg=u'置顶消息验证失败')
        print u"联系人为群组取消置顶成功"
        el=driver.find_element_by_name(u"group")#定位名字
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        driver.find_element_by_name(u"置顶聊天").click()  
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/nickname_tv").get_attribute('text')
        assert_equal(el,u"group",msg=u'置顶消息验证失败')
        print u"联系人为群组置顶成功"
        el=driver.find_element_by_name(u"温强")#定位名字
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        driver.find_element_by_name(u"置顶聊天").click()
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/nickname_tv").get_attribute('text')
        assert_equal(el,u"group",msg=u'置顶消息验证失败')
        print u"联系人置顶成功" 
        driver.find_element_by_name(u"温强").click()
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chat_add").click()
        driver.find_element_by_name(u"温强").click()
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_invite").click()
        driver.press_keycode('4')
        driver.press_keycode('4')
        time.sleep(2)
        driver.press_keycode('4')        
        el=driver.find_element_by_name(u"qiuqiu、温强创建的讨论组")#定位名字
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        driver.find_element_by_name(u"置顶聊天").click()  
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/nickname_tv").get_attribute('text')
        assert_equal(el,u"qiuqiu、温强创建的讨论组",msg=u'置顶消息验证失败')
        print u"联系人为讨论组置顶成功"
        logout.test_logout(self)#退出登录
        #账号重新登录
        login.test_login(self,phoneid="13311267857")
        #取消置顶
        el=driver.find_element_by_name(u"温强")#定位名字
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        driver.find_element_by_name(u"取消置顶").click()
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/nickname_tv").get_attribute('text')
        assert_equal(el,u"qiuqiu、温强创建的讨论组",msg=u'置顶消息验证失败')
        print u"重新登录后联系人取消置顶成功"         
        el=driver.find_element_by_name(u"group")#定位名字
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        driver.find_element_by_name(u"取消置顶").click()
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/nickname_tv").get_attribute('text')
        assert_equal(el,u"qiuqiu、温强创建的讨论组",msg=u'置顶消息验证失败')
        print u"重新登录后联系人为群组取消置顶成功"   
        #取消置顶
        el=driver.find_element_by_name(u"qiuqiu、温强创建的讨论组")#定位名字
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        driver.find_element_by_name(u"取消置顶").click()
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/nickname_tv").get_attribute('text')
        assert_equal(el,u"qiuqiu、温强创建的讨论组",msg=u'置顶消息验证失败')
        print u"重新登录后联系人为讨论组取消置顶成功"        
             
         
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