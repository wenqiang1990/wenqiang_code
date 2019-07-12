#coding:utf-8
import time
import datetime 
import unittest
from robot.utils.asserts import *
from appium import webdriver
from public import swip
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {}
        desired_caps['deviceName'] = '3a11d697'  
        desired_caps['platformName'] = 'Android'   
        desired_caps['platformVersion'] = '5.1.1'   
        desired_caps['appPackage'] = 'com.yuntongxun.ecdemo'  
        desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.LauncherActivity' 
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(30)
        '''
        IME_LISE = self.driver.available_ime_engines
        print(IME_LISE)
        self.driver.deactivate_ime_engine()#g关闭当前输入法
        self.driver.activate_ime_engine(IME_LISE[-1])
        '''
    def test_send_txt(self):
        '''查找联系人，发送文本消息''' 
        #查找联系人
        time.sleep(5) 
        swip.swipLeft(self,500)#左划
        time.sleep(2)
        swip.swipLeft(self,500)#左划
        self.driver.find_element_by_id("group_name").click()
        self.driver.find_element_by_id("chatting_content_et").send_keys("https://www.baidu.com")
        self.driver.find_element_by_id("chatting_send_btn").click()
        time.sleep(2)
        #发送文本消息
        sendoutcontent = self.driver.find_element_by_id("chatting_content_itv").get_attribute("text")
        print sendoutcontent
        receivecontent = self.driver.find_element_by_id("tv_read_unread").get_attribute("text")
        
        #验证发送消息
        assert_equal(sendoutcontent,"hello tester",msg=u'发送的消息验证失败')
        assert_equal(receivecontent,u"未读",msg=u'消息状态验证失败')
  
  
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