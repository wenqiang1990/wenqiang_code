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

    def test_revocation(self):  
        '''讨论组撤回消息，验证已读列表''' 
        driver = self.driver
        time.sleep(2)
        try:
            logout.test_logout(self)#退出登录
        except:
            print u"未登录，无需执行退出登录操作"   
        login.test_login(self,phoneid="13311267857")     
        member = "17600645696"  #被@成员账号
        time.sleep(2) 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_discussion").click()#点击讨论组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击讨论组   
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_et").send_keys("2")#输入1
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_send_btn").click()#点击发送           
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()        
        self.driver.find_element_by_name(u"确认").click()
        
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv")       
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()        
        self.driver.find_element_by_name(u"确认").click()
           
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"撤销").click()
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_time_tv").get_attribute("text")
        assert_equal(el,u"你撤回了一条消息",msg=u'消息验证失败')
        driver.press_keycode('4')
        print u"操作撤回消息"
        driver.press_keycode('4')
        logout.test_logout(self)#退出登录
        login.test_login(self,phoneid="17600645696")
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_discussion").click()#点击讨论组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击讨论组   
        #查看已读消息成员列表，此处后期需加入图片对比
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"查看已读未读").click()
        self.driver.find_element_by_name(u"已读").click()
        time.sleep(2)
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/messageAccount").get_attribute("text")
        assert_equal(el,"qiuqiu",msg=u'消息验证失败')        
        print u"已读消息列表成员为%s验证通过" %el
        driver.press_keycode('4')
        time.sleep(2)
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()        
        self.driver.find_element_by_name(u"确认").click()        
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_time_tv").get_attribute("text")
        assert_equal(el,u"13311267857撤销了一条消息",msg=u'消息验证失败')                
        print u"撤回消息成功"                     
          
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_revocation"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      