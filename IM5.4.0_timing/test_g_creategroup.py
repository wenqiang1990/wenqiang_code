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
from clear_massage import clear_allmassage 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)      


    def test_creategroup(self):  
        '''创建讨论组'''
        try:
            logout.test_logout(self)#退出登录
        except:
            print "未登录，无需执行退出登录操作"   
        login.test_login(self,phoneid="13311267857") 
        driver = self.driver
        clear_allmassage(self,id="com.yuntongxun.eckuailiao:id/nickname_tv")
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_discussion").click()#点击讨论组
        driver.find_element_by_xpath("//android.widget.ImageButton[2]").click()#点击加号
        time.sleep(2)
        driver.find_element_by_name(u"联通").click()#点击成员 
        driver.find_element_by_name("温强").click()#点击成员
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_invite").click()#点击邀请
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理  
        driver.find_element_by_name(u"讨论组个人名片").click()#点击讨论组名片
        #将群组id保存到本地
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/accessory_checked").get_attribute("text")
        with open('F:\Appium\group\groupID.txt','w') as f:
            f.write(el)
        print "讨论组ID为    "+el

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