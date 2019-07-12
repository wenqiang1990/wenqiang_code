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
        '''邀请群成员''' 
        driver = self.driver
        time.sleep(2)
        member = "13366778604"  #被踢出成员账号
        clear_allmassage(self,id="com.yuntongxun.eckuailiao:id/nickname_tv")#清空消息记录
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组id,以后改为读取上一条用例创建群组的id 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理  
        time.sleep(2)
        #踢出群成员
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_card_item_avatar_iv").click()#点击+号
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys(member)#查询   
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").click()#点击成员
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").get_attribute("text")#成员账号
        assert_equal(el,u"13366778604",msg=u"群组名称验证失败")
        #driver.press_keycode('4')
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_invite").click()#点击邀请
        time.sleep(2)
        driver.press_keycode('4')
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_left").click()#群组内返回按钮
        driver.press_keycode('4')
        time.sleep(2)
        driver.press_keycode('4')
        logout.test_logout(self)#退出登录
        login.test_login(self,phoneid = member)#登录
        time.sleep(2)
        driver.find_element_by_name(u"系统通知").click()#点击系统通知消息     
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/accept_btn").click()#点击同意按钮
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/result_show").get_attribute("text")
        assert_equal(el,u"已接受",msg=u'邀请加入群组通知状态变显示不对')
        print "邀请加入群组通知状态变为已接受" 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击清空       
        driver.press_keycode('4')
        logout.test_logout(self)#退出登录
        login.test_login(self,phoneid = "13311267857")
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tipcnt_tv").get_attribute("text")
        assert_equal(el,"1",msg=u'系统通知未读消息数显示不对')
        print "系统通知未读消息数显示正确"
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组id,以后改为读取上一条用例创建群组的id 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理  
        #el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_right").get_attribute("text")
        #assert_equal(el,u"3人",msg=u'被邀请人加入群组失败')
        print "被邀请人成功加入群"                
         
        
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