#coding:utf-8
import time
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
from public import swip
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {}
        desired_caps['deviceName'] = 'a2c3e2d9'  
        desired_caps['platformName'] = 'Android'   
        desired_caps['platformVersion'] = '5.1.1'   
        desired_caps['appPackage'] = 'com.yuntongxun.ecdemo'  
        desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.LauncherActivity' 
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(30)        

    
    def test_send_voicemessage(self):
        '''发送萝莉变声语音消息''' 
        time.sleep(5)
        swip.swipLeft(self,500)#左划
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/card_item_tv").click()
        self.driver.find_element_by_id("content").click()
        self.driver.find_element_by_id("content").send_keys("13311267857")
        self.driver.find_element_by_id("text_right").click()   
                  
        #发送变声语音
        self.driver.find_element_by_id("chatting_mode_btn").click()#左下角语音按钮
        time.sleep(2)
        self.driver.swipe(810,1600,54,1600,500)
        action1 = TouchAction(self.driver)  
        el = self.driver.find_element_by_id("voice_record_imgbtn_biansheng")
        action1.long_press(el,duration=10000).perform()
        self.driver.find_element_by_name(u"萝莉").click()
        self.driver.find_element_by_id("layout_send_changevoice").click()
        #删除
        el=self.driver.find_element_by_id("tv_read_unread").get_attribute("text")
        assert_equal(el, u"已读", msg=u"状态验证失败")            
        print el+u" 阅读状态验证成功"
        el = self.driver.find_element_by_id("tv_read_unread")#状态
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()    
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除 

        self.driver.find_element_by_id("chatting_voice_play_anim_tv").click()
        time.sleep(5)
        #删除接收语音
        el = self.driver.find_element_by_id("chatting_content_itv")#时间
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()    
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()#确认删除    
        
  
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_voicemessage"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      