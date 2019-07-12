#coding:utf-8
import time
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import logout
from public import login
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {}
        desired_caps['deviceName'] = '3a11d697'# 3a11d697 ：红米note3
        desired_caps['udid'] = '3a11d697' #设备的udid 实际控制启动哪台机器
        desired_caps['platformName'] = 'Android'   
        desired_caps['platformVersion'] = '5.1.1'   
        desired_caps['appPackage'] = 'com.yuntongxun.eckuailiao' #com.yuntongxun.eckuailiao
        desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.account.SplashActivity'#com.yuntongxun.ecdemo.ui.phonemodel.PhoneUI#com.yuntongxun.ecdemo.ui.account.LoginActivity
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(30)      

    
    def test_kickgroup(self):  
        '''踢出群成员''' 
        driver = self.driver
        time.sleep(2) 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组id,以后改为读取上一条用例创建群组的id 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理  
        time.sleep(2)
        #踢出群成员
        driver.find_element_by_xpath("//android.widget.FrameLayout[5]//android.widget.TextView").click()#点击-号
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys("13366778604")#查询   
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").click()#点击成员
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").get_attribute("text")#成员账号
        assert_equal(el,u"13366778604",msg=u"群组名称验证失败")
        driver.press_keycode('4')
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_invite").click()#点击删除
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button3").click()#点击确认删除
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_right").get_attribute("text")#成员账号
        assert_equal(el,u"2人",msg=u"群组成员数验证失败")
        driver.press_keycode('4')
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_left").click()#点击返回群组列表页
        driver.press_keycode('4')#点击返回主页面
        time.sleep(2)
        driver.press_keycode('4')#点击返回主页面
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_tab_msg").click()#点击消息
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_unread_msg_number").get_attribute("text")#获取总消息数
        assert_equal(el,"1",msg=u'总未读消息数显示不对')
        print "总未读消息数"+el+"显示正确"
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tipcnt_tv").get_attribute("text")
        assert_equal(el,"1",msg=u'系统通知未读消息数显示不对')
        print "系统通知未读消息数显示正确"
        driver.find_element_by_name(u"系统通知").click()#点击成员
        #el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_unread_msg_number").get_attribute("text")#获取总消息数
        #assert_equal(el,"1",msg=u'总未读消息数显示不对')
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击清空
        
        
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_kickgroup"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      