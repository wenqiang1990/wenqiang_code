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
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)       
   
    def test_group_ban(self):  
        '''设置群组个人名片，昵称、手机号、邮箱、备注''' 
        driver = self.driver
        time.sleep(2)
        member = "13366778604"  #被禁言成员账号
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        print "Start : %s" % time.ctime()#输出当前时间
        time.sleep(2)
        print "Stop : %s" % time.ctime()#输出当前时间
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        print "Start : %s" % time.ctime()#输出当前时间
        time.sleep(2)
        print "Stop : %s" % time.ctime()#输出当前时间
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组id,以后改为读取上一条用例创建群组的id 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理  
        time.sleep(2)
        #设置群成员群内昵称
        driver.find_element_by_name(u"群组个人名片").click()#点击设置群族个人
        driver.find_element_by_name(u"昵称").click()#点击添加成员
        driver.find_element_by_id(u"com.yuntongxun.eckuailiao:id/sendrequest_content").clear()#改名
        driver.find_element_by_id(u"com.yuntongxun.eckuailiao:id/sendrequest_content").send_keys(u"球球")#改名
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button3").click()#点击确认
        time.sleep(1)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击确定
        driver.press_keycode('4')
        time.sleep(1)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理         
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_bo").get_attribute("text")#点击确定
        assert_equal(el,u"球球",msg=u'系统通知消息显示不对')
        print u"群内成员昵称【%s】显示正确"%el
        
        #设置群成员名片电话
        driver.find_element_by_name(u"群组个人名片").click()#点击设置群族个人
        driver.find_element_by_name(u"电话").click()#点击添加成员
        driver.find_element_by_id(u"com.yuntongxun.eckuailiao:id/sendrequest_content").clear()#改名
        driver.find_element_by_id(u"com.yuntongxun.eckuailiao:id/sendrequest_content").send_keys("13311267857")#改名
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button3").click()#点击确认
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击确定
        driver.find_element_by_name(u"群组个人名片").click()#点击设置群族个人
        driver.find_element_by_name(u"电话").click()#点击
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/sendrequest_content").get_attribute("text")#
        assert_equal(el,u"13311267857",msg=u'系统页面显示不对')
        print u"群内成员电话【%s】显示正确"%el      
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button1").click()#点击取消

        #设置群成员名片邮箱
        driver.find_element_by_name(u"邮箱").click()#点击添加成员
        driver.find_element_by_id(u"com.yuntongxun.eckuailiao:id/sendrequest_content").clear()#改名
        driver.find_element_by_id(u"com.yuntongxun.eckuailiao:id/sendrequest_content").send_keys("1058099258@qq.com")#改名
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button3").click()#点击确认
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击确定
        driver.find_element_by_name(u"群组个人名片").click()#点击设置群族个人
        driver.find_element_by_name(u"邮箱").click()#点击
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/sendrequest_content").get_attribute("text")#
        assert_equal(el,u"1058099258@qq.com",msg=u'系统页面显示不对')
        print u"群内成员邮箱【%s】显示正确"%el
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button1").click()#点击取消
        #验证修改邮箱后电话是否变化
        driver.find_element_by_name(u"电话").click()#点击
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/sendrequest_content").get_attribute("text")#
        assert_equal(el,u"13311267857",msg=u'系统页面显示不对')
        print u"群内成员电话【%s】显示正确"%el
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button1").click()#点击取消      

        #设置群成员名片备注
        driver.find_element_by_name(u"备注").click()#点击添加成员
        driver.find_element_by_id(u"com.yuntongxun.eckuailiao:id/sendrequest_content").clear()#改名
        driver.find_element_by_id(u"com.yuntongxun.eckuailiao:id/sendrequest_content").send_keys(u"我是群组个人名片的备注")#改名
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button3").click()#点击确认
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击确定
        driver.find_element_by_name(u"群组个人名片").click()#点击设置群族个人
        driver.find_element_by_name(u"备注").click()#点击
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/sendrequest_content").get_attribute("text")#
        assert_equal(el,u"我是群组个人名片的备注",msg=u'系统页面显示不对')
        print u"群内成员备注【%s】显示正确"%el      
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button1").click()#点击取消
        #验证修改备注后邮箱是否变化
        driver.find_element_by_name(u"邮箱").click()#点击
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/sendrequest_content").get_attribute("text")#
        assert_equal(el,u"1058099258@qq.com",msg=u'系统页面显示不对')
        print u"群内成员邮箱【%s】显示正确"%el    
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button1").click()#点击取消        

        #设置群成员群内昵称汉字字母符号数字组合，最大16字符
        driver.find_element_by_name(u"昵称").click()#点击添加成员
        driver.find_element_by_id(u"com.yuntongxun.eckuailiao:id/sendrequest_content").clear()#改名
        driver.find_element_by_id(u"com.yuntongxun.eckuailiao:id/sendrequest_content").send_keys(u"qiuqiu")#改名
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button3").click()#点击确认
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击确定
        driver.press_keycode('4')
        time.sleep(1)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理         
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_bo").get_attribute("text")#点击
        assert_equal(el,u"qiuq",msg=u'系统通知消息显示不对')
        print u"群内成员昵称【%s】显示正确"%el
        #设置群成员名片邮箱中文英文数字组合
        driver.find_element_by_name(u"群组个人名片").click()#点击设置群族个人
        driver.find_element_by_name(u"邮箱").click()#点击添加成员
        driver.find_element_by_id(u"com.yuntongxun.eckuailiao:id/sendrequest_content").clear()#改名
        driver.find_element_by_id(u"com.yuntongxun.eckuailiao:id/sendrequest_content").send_keys(u"中文ww9@qq.com")#改名
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button3").click()#点击确认
        time.sleep(1)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击确定
        driver.find_element_by_name(u"群组个人名片").click()#点击设置群族个人
        driver.find_element_by_name(u"邮箱").click()#点击
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/sendrequest_content").get_attribute("text")#
        assert_equal(el,u"中文ww9@qq.com",msg=u'系统页面显示不对')
        print u"群内成员邮箱【%s】显示正确"%el      
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button1").click()#点击取消
        #设置群成员名片备注中文英文数字组合
        driver.find_element_by_name(u"备注").click()#点击添加成员
        driver.find_element_by_id(u"com.yuntongxun.eckuailiao:id/sendrequest_content").clear()#改名
        driver.find_element_by_id(u"com.yuntongxun.eckuailiao:id/sendrequest_content").send_keys(u"我是群组个人名片的备注，16aaaaaa")#改名
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button3").click()#点击确认
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击确定
        driver.find_element_by_name(u"群组个人名片").click()#点击设置群族个人
        driver.find_element_by_name(u"备注").click()#点击
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/sendrequest_content").get_attribute("text")#
        assert_equal(el,u"我是群组个人名片的备注，16aaaaaa",msg=u'系统页面显示不对')
        print u"群内成员备注【%s】显示正确"%el      
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/dilaog_button1").click()#点击取消
       
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_group_ban"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      