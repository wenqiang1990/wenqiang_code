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

    
    def test_creategroup(self):  
        '''修改讨论组组名称''' 
        driver = self.driver
        time.sleep(3)
        clear_allmassage(self,id="com.yuntongxun.eckuailiao:id/nickname_tv")
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_discussion").click()#点击讨论组
        with open('F:\Appium\group\groupID.txt','r') as f:
            el=f.read()
        el="讨论组id:"+el
        print el
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击讨论组   
        #driver.find_element_by_name(el).click()#点击群组id,以后改为读取上一条用例创建群组的id 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理  
        time.sleep(2)
        #修改讨论组组名称
        discussionname='discussionname1'
        driver.find_element_by_name(u"讨论组名称").click()#点击讨论组名片
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/content").clear()
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/content").send_keys(discussionname)#讨论组名称
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击确认
        driver.press_keycode('4')
        time.sleep(2)
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_middle").get_attribute("text")
        assert_equal(el,discussionname,msg=u'讨论组聊天页面讨论组名称数显示不对')
        print "讨论组聊天页面讨论组名称%s显示正确"%el
        driver.press_keycode('4')#点击返回主页面
        time.sleep(2)
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").get_attribute("text")
        assert_equal(el,discussionname,msg=u'讨论组聊天页面讨论组名称数显示不对')
        print "讨论组列表页面讨论组名称%s显示正确"%el      
        driver.press_keycode('4')#点击返回主页面
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_tab_msg").click()#点击消息
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tipcnt_tv").get_attribute("text")
        assert_equal(el,"1",msg=u'系统通知未读消息数显示不对')
        print u"系统通知未读消息数显示正确"
        driver.find_element_by_name(u"系统通知").click()#点击成员
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击清空  
        driver.press_keycode('4')#点击返回主页面
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_discussion").click()#点击讨论组        
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击具体讨论组   
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理  
        time.sleep(2)       
        #修改讨论组组名称为128字符
        driver.find_element_by_name(u"讨论组名称").click()#点击讨论组名片
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/content").clear()
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/content").send_keys(u"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678")#讨论组名称
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击确认     
        #修改讨论组组名称为‘符号’
        driver.find_element_by_name(u"讨论组名称").click()#点击讨论组名片
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/content").clear()
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/content").send_keys(u"【】！@#￥%……&*（）——+-=")#讨论组名称
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击确认           
        #修改讨论组组名称为‘中文’
        driver.find_element_by_name(u"讨论组名称").click()#点击讨论组名片
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/content").clear()
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/content").send_keys(u"讨论组一号")#讨论组名称
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击确认        
        driver.press_keycode('4')
        time.sleep(2) 
        driver.press_keycode('4')
        time.sleep(2)
        driver.press_keycode('4')
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_tab_msg").click()#点击消息
        driver.find_element_by_name(u"系统通知").click()#点击系统通知
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击清空 
        
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