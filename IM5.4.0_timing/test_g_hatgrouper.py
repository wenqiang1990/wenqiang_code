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
from clear_massage import clear_allmassage
 
class Imtest(unittest.TestCase):
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)        

    
    def test_creategroup(self):  
        '''讨论组@成员''' 
        driver = self.driver
        time.sleep(2)
        member = "17600645696"  #被@成员账号
        time.sleep(2)
        clear_allmassage(self,id="com.yuntongxun.eckuailiao:id/nickname_tv") 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_discussion").click()#点击讨论组
        '''with open('F:\Appium\group\groupID.txt','r') as f:
            el=f.read()
        el="讨论组id:"+el
        print el'''
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击讨论组  
        #driver.find_element_by_name(u"讨论组一号").click()       
        #driver.find_element_by_name(el).click()#点击群组id,以后改为读取上一条用例创建群组的id 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_et").send_keys("@")#输入@
        driver.find_element_by_name(u"联通").click()#点击确认
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_send_btn").click()#点击发送    
        driver.press_keycode('4')
        time.sleep(2)
        driver.press_keycode('4')
        time.sleep(2)
        logout.test_logout(self)#退出登录
        login.test_login(self,phoneid = member)#@成员登录   
        time.sleep(2)
        clear_massage(self,name=u"系统通知")
        #验证接收@消息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/last_msg_tv").get_attribute("text")
        assert_equal(el,u"[有人@我] [3条]qiuqiu: @联通 ",msg=u'@消息验证失败')
        print u"群组内@成员发送消息成功"                
          
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_creategroup"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      