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
        '''创建非公开群组名称中英文数字字符，类型家政，公告100，省份64，城市空'''
        driver = self.driver
        print "Start : %s" % time.ctime()#输出当前时间
        time.sleep(3)
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
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_group_name").send_keys(u'群name7？')
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_province").send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        #driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_city").send_keys("HarbinMunicipality")
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_notice_select").click()#点击公告
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_notice").send_keys(u"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")#输入公告      
        driver.find_element_by_xpath("//android.widget.TextView[@text='保存']").click()#点击保存
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_group_type").click()#群组类型
        driver.find_element_by_name(u"家政").click()#群组类型
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/accessory_checked").click()#公开
        driver.find_element_by_name(u"下一步").click()#下一步
        time.sleep(2)
        driver.press_keycode('4')#点击返回
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        time.sleep(1)
        driver.find_element_by_name(u"群name7？").click()#点击群组
        time.sleep(2)
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_middle").get_attribute("text")
        assert_equal(el,u'群name7？',msg=u'群组聊天页面群组名称显示不对')
        print u"群组聊天页面群组名称是 【"+el+"】 显示正确"
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理 
        time.sleep(2)
        driver.swipe(600,800,600,100,500)#上划
        driver.find_element_by_name(u"解散该群").click()#点击群组管理

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