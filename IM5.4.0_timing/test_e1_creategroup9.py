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
        '''创建私有群组名称中英文数字字符，类型粉丝，公告汉字，省份城市汉字'''
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
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_province").send_keys(u"黑龙江省")
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_city").send_keys(u"哈尔滨市")
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_notice_select").click()#点击公告
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_notice").send_keys(u"请文明发言")#输入公告      
        driver.find_element_by_xpath("//android.widget.TextView[@text='保存']").click()#点击保存
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_group_type").click()#群组类型
        driver.find_element_by_name(u"粉丝").click()#群组类型
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
        driver.find_element_by_name(u"群组个人名片").click()#点击群名片
        #将群组id保存到本地
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/accessory_checked").get_attribute("text")
        with open('F:\Appium\group\groupID.txt','w') as f:
            f.write(el)
        print "群组ID    "+el
        driver.press_keycode('4')#点击返回
        time.sleep(1)
        driver.press_keycode('4')#点击返回
        time.sleep(1)
        driver.press_keycode('4')#点击返回
        time.sleep(1)
        driver.press_keycode('4')#点击返回 
        time.sleep(1)
        driver.press_keycode('4')#点击返回             
        logout.test_logout(self)#退出登录
        login.test_login(self,phoneid="13366778604")
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_search").click()#点击搜索群组
        driver.find_element_by_name(u"按群组ID精确查询").click()#点击按群组id
        with open('F:\Appium\group\groupID.txt','r') as f:
            el=f.read()
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search_flite").send_keys(el)#点击按群组id
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击确定
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/empty_search_tv").get_attribute("text")#点击按群组id
        assert_equal(el,u'暂无结果',msg=u'群组聊天页面群组名称显示不对')
        print u"通过id查询非公开群组显示%s"%el

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