#coding:utf-8
import time,os
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
#from robot.utils.asserts import *
from public import login
from public import logout,swip
from public.extend import Appium_Extend
from public.clear_massage import clear_allmassage
from public.set_driver import set_driver
import pytest,allure
from params import yaml_handle
config = yaml_handle.read_yaml("device.yaml")
config1 = yaml_handle.read_yaml("data.yaml")
uid = config["蓝色ipod"]
iphone_password=config["13366778604"]
massage=config1["massage"]

class Imtest(unittest.TestCase):
    #def __init__(self,driver):
        #self.driver = driver     
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver(uid,'4723')
        self.verificationErrors = []
        self.driver.implicitly_wait(10)                  
        self.extend = Appium_Extend(self.driver)
    lines=massage.vslues()
    print("lines: %s " %lines)
    @pytest.mark.parametrize("i", lines)  # 参数化
    def test_send_txt(self,i):
        '''查找联系人，发送各种文本消息'''
        try:
            logout.test_logout(self)#退出登录
        except:
            print ("未登录，无需执行退出登录操作") 
        #time.sleep(2)
        login.test_login(self,phoneid="13366778604",password=iphone_password)
        time.sleep(2)
        self.driver.find_element_by_name(u"通讯录").click()#com.yuntongxun.rongxin.lite:id/input_search_et
        self.driver.find_element_by_name(u"朱磊可").click()
        self.driver.find_element_by_accessibility_id("yhc address chat").click()

        #self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_my").click()#点击搜索 中文输入时无需收回键盘
        self.driver.find_element_by_class_name("XCUIElementTypeTextView").click()#点击输入框
        self.driver.find_element_by_class_name("XCUIElementTypeTextView").send_keys(i)  #
        #print "Start : %s" % time.ctime()
        time.sleep(2)
        self.driver.press_keycode('66')#点击回车
        time.sleep(2)
        #验证发送消息
        sendoutcontent = self.driver.find_element_by_accessibility_id(i).get_attribute("text")
        #print sendoutcontent
        assert(sendoutcontent,i)
        #删除发送消息
        self.driver.find_element_by_accessibility_id("chat single right").click()
        self.driver.find_element_by_accessibility_id(u"清空聊天记录").click()
        self.driver.find_element_by_class_name("XCUIElementTypeButton").click()
        swip.swipRight(200)
        print(u'发送消息'+ i)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_txt"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      