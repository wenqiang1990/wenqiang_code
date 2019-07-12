#coding:utf-8
import time
import datetime 
import unittest
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
from public import swip
from appium.webdriver.common.touch_action import TouchAction
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
        self.driver = webdriver.Remote()   
        self.driver.implicitly_wait(30)
        self.verificationErrors = [] 
        '''
         
    def test_send_txt(self):
        '''查找联系人，发送文本消息''' 
        #查找联系人
        time.sleep(5) 
        swip.swipLeft(self,500)#左划
        time.sleep(2)
        swip.swipLeft(self,500)#左划
        self.driver.find_element_by_id("group_name").click()
        wq = self.driver.find_element_by_id("chatting_attach_btn")
        assert_not_none(wq,u"未定位到加号按钮")
        wq.click()
        time.sleep(2)
        #发送语音
        self.driver.find_element_by_id("chatting_mode_btn").click()#左下角语音按钮
        action1 = TouchAction(self.driver)  
        el = self.driver.find_element_by_id("voice_record_imgbtn")
        action1.long_press(el,duration=5000).perform()
        #点击发送出去的语音
        self.driver.find_element_by_id("chatting_voice_play_anim_tv").click()#点击发送的语音
        time.sleep(5)
        self.driver.find_element_by_id("btn_left").click()#点击右上角返回按钮
        logout.test_logout(self)#退出登录
        login.test_login(self,el="13366778604")#使用账号13366778606登录
        self.driver.find_element_by_name("13311267857").click()
        self.driver.find_element_by_id("chatting_voice_play_anim_tv").click()
        time.sleep(5)
        self.driver.press_keycode('4')#点击返回键
        
        el = self.driver.find_element_by_id("avatar_iv")
        action1.long_press(el,duration=5000).perform()        
        self.driver.find_element_by_name(u"删除该聊天").click() 
        logout.test_logout(self)#退出登录
        time.sleep(5)
  
  
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