#coding:utf-8
import time
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import swip
from extend import Appium_Extend
from clear_massage import clear_massage
 
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
        self.driver.implicitly_wait(10)        


    def test_send_photograph(self):
        '''发送拍摄照片''' 
        #clear_massage(self,name=u"球球")#删除消息页面，昵称为**的聊天记录
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys("13311267857")
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/name_tv").click()
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_chat").click()         
        #发送照片
        time.sleep(5)
        self.driver.find_element_by_id("chatting_attach_btn").click()
        time.sleep(2)
        '''
        photograph_x=self.driver.find_element_by_name(u"相册").location.get('x')
        photograph_y=self.driver.find_element_by_name(u"拍照").location.get('y')
        print photograph_x,photograph_y
        photograph_x=int(photograph_x)
        photograph_y=int(photograph_y)-100
        print photograph_x,photograph_y
        self.driver.tap([(photograph_x,photograph_y)], )#点击
        '''
        self.driver.find_element_by_name(u"拍摄").click()
        #self.driver.find_element_by_id("cameraswitchtofront").click()#切换摄像头
        time.sleep(3)
        self.driver.context#可以定位到悬浮窗口
        self.driver.find_element_by_id("com.lenovo.scg:id/shutter_button").click()#快门
        time.sleep(2)
        self.driver.context#可以定位到悬浮窗口
        self.driver.find_element_by_id("com.lenovo.scg:id/btn_done").click()#保存
        time.sleep(2)
        self.driver.find_element_by_id("text_right").click()
        print "Start : %s" % time.ctime() + u"拍照成功"#输出当前时间
        time.sleep(3)
        el=self.driver.find_element_by_id("tv_read_unread").get_attribute("text")
        assert_equal(el, u"已读", msg=u"状态验证失败")            
        print el+u" 阅读状态验证成功"
        el = self.driver.find_element_by_id("tv_read_unread")#状态
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()    
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除
         
        #删除接收到的图片
        x1=self.driver.find_element_by_id("chatting_content_iv").location.get('x')
        y1=self.driver.find_element_by_id("chatting_content_iv").location.get('y')
        print x1,y1
        x1=int(x1)+400
        y1=int(y1)+100
        print x1,y1
    
        self.driver.tap([(x1,y1)],5000)
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除

                                                          
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_photograph"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      