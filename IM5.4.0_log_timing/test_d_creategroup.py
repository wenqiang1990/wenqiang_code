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


    def test_creategroup(self):  
        '''创建群组设置省市区、类型、公告''' 
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
        groupname = "groupname1"
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_group_name").send_keys(groupname)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_province").send_keys("province")
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_city").send_keys("groupcity")
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_notice_select").click()#点击公告
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_notice").send_keys("Announcement of the group")#输入公告
        driver.find_element_by_xpath("//android.widget.TextView[@text='保存']").click()#点击保存
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_group_type").click()#群组类型
        driver.find_element_by_name(u"朋友").click()#群组类型
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/accessory_checked").click()#公开
        driver.find_element_by_name(u"下一步").click()#下一步
        number="13366778604"#要搜索的好友
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys(number)#搜索
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").get_attribute("text")
        assert_equal(el,number,msg=u'搜索结果不对')
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/avatar_iv").click()#点击成员
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").clear()#清空搜索框
        
        driver.find_element_by_name(u"修月").click()#点击成员 
        driver.find_element_by_name(u"温强").click()#点击成员
        driver.press_keycode('4')
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_count").get_attribute("text")
        assert_equal(el,u"已选择：2人",msg=u'邀请人数不对')
        print "邀请人数显示正确"+el
        #driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_count").click()
        #driver.find_element_by_name(u"邀请").click()#点击邀请
        #driver.tap([(900,1850)], )#点击创建群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_invite").click()#点击邀请
        time.sleep(2)
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_middle").get_attribute("text")
        assert_equal(el,groupname,msg=u'群组聊天页面群组名称显示不对')
        print "群组聊天页面群组名称是 "+groupname+" 显示正确"
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理  
        driver.find_element_by_name(u"群名片").click()#点击群名片
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
        '''
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_unread_msg_number").get_attribute("text")
        assert_equal(el,"2",msg=u'总未读消息数显示不对')
        print "总未读消息数"+el+"显示正确"
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tipcnt_tv").get_attribute("text")
        assert_equal(el,"2",msg=u'系统通知未读消息数显示不对')
        print "系统通知未读消息数显示正确"
        '''
        driver.find_element_by_name(u"系统通知").click()#点击系统通知消息
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击清空
        
        '''
        #解散群组
        self.driver.press_keycode('4')#点击返回
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        print "Stop : %s" % time.ctime()#输出当前时间
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表      
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组id,以后改为读取上一条用例创建群组的id 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理
        driver.find_element_by_name(u"解散该群").click()#点击群组管理
        self.driver.press_keycode('4')#点击返回
        time.sleep(2)
        self.driver.press_keycode('4')#点击返回
        logout.test_logout(self)#退出登录
        '''
           

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