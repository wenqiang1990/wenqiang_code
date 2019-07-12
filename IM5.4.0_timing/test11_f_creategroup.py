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
from set_driver import set_driver 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)      


    def test_creategroup(self):  
        '''创建名称为多种字符的群组'''
        driver = self.driver
        print "Start : %s" % time.ctime()#输出当前时间
        time.sleep(2)
        print "Stop : %s" % time.ctime()#输出当前时间  
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        print "Start : %s" % time.ctime()#输出当前时间
        time.sleep(2)
        print "Stop : %s" % time.ctime()#输出当前时间
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        print "Stop : %s" % time.ctime()#输出当前时间
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        driver.find_element_by_xpath("//android.widget.ImageButton[2]").click()#点击加号
        time.sleep(2)
        groupname = ["群组","1234567890",'中文1234567890ABCDEFGHIJKLMNOPQRSTUCWXYZabcdefghijklmnopqrstuvwxyz！#￥%……']#
        for i in range(groupname):
            driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_group_name").send_keys(groupname[i])
            driver.find_element_by_name(u"下一步").click()#下一步
            self.driver.press_keycode('4')#点击返回
            driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
            driver.find_element_by_xpath("//android.widget.ImageButton[2]").click()#点击加号

        time.sleep(2)
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_middle").get_attribute("text")
        assert_equal(el,groupname,msg=u'群组聊天页面群组名称显示不对')
        print "群组聊天页面群组名称是 "+groupname+" 显示正确"
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理 
        time.sleep(2)
        driver.find_element_by_name(u"群组个人名片").click()#点击群名片
        #将群组id保存到本地
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/accessory_checked").get_attribute("text")
        with open('F:\Appium\group\groupID.txt','w') as f:
            f.write(el)
        print "群组ID    "+el   
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_left").click()#点击返回按钮
        time.sleep(2)
        self.driver.press_keycode('4')#点击返回
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_left").click()#点击返回按钮
        self.driver.press_keycode('4')#点击返回键收回键盘
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_tab_msg").click()#点击消息
        driver.find_element_by_name(u"系统通知").click()#点击系统通知消息
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