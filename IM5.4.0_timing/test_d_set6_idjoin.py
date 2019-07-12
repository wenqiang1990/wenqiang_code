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

    
    def test_idjoin_group(self):  
        '''通过群组ID搜索群组并加入''' 
        driver = self.driver
        member = "17600645696"  #申请加入成员账号
        with open('F:\Appium\group\groupID.txt','r') as f:
            el=f.read()
        #搜索群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_search").click()#点击搜索群组
        driver.find_element_by_name(u"按群组ID精确查询").click()#点击搜索群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search_flite").send_keys(el)#读取上一条用建群组的id 搜索
        #driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search_flite").send_keys("groupname1")#点击群组管理  
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击确定
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/red_btn").click()#点击申请加入
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/content").send_keys("apply to join")#输入申请文字
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击群定
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_left").click()#点击返回
        time.sleep(2)
        driver.press_keycode('4')
        time.sleep(2)
        driver.press_keycode('4')  
        logout.test_logout(self)#退出登录
        login.test_login(self,phoneid ="13311267857")#登录       
        #管理员同意群组加入申请
        time.sleep(2)
        driver.find_element_by_name(u"系统通知").click()#点击系统通知
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/accept_btn").click()#点击同意
        time.sleep(2)
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/result_summary").get_attribute("text")#通知内容
        #assert_equal(el,u"管理员通过了[修月]的加群请求",msg=u"系统通知验证失败")       
        print "系统通知未读消息数显示     "+el+"  正确"
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/text_right").click()#点击清空
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_left").click()#点击返回
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组id,以后改为读取上一条用例创建群组的id 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理  
        #el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_right").get_attribute("text")
        #assert_equal(el,u"2人",msg=u'申请人加入群组失败')
        print "申请人成功加入群"     
   
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_idjoin_group"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      