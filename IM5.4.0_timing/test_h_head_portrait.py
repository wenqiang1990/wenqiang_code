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
from clear_massage import clear_massage 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)        

    def test_revocation(self):  
        '''拍照选择设置头像''' 
        driver = self.driver
        time.sleep(2)
        member = "17600645696"  #被@成员账号
        time.sleep(2) 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_my").click()#点击我的
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/self_info").click()#点击个人信息
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/iv_my_header").click()#点击头像
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_take_photo").click()#点击拍照
        time.sleep(2)
        self.driver.press_keycode('27')#点击拍照键  
        #self.driver.find_element_by_id("com.lenovo.scg:id/shutter_button").click()#联想快门
        time.sleep(3)
        self.driver.find_element_by_id("com.sec.android.app.camera:id/okay").click()#三星s5点击确定
        time.sleep(3)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/menu_crop").click()#三星s5点击对勾
        time.sleep(2)
        print "set head portrait success"           
          
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_revocation"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      