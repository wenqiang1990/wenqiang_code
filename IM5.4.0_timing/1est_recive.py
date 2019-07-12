#coding:utf-8
import time,os
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
from extend import Appium_Extend
import set
import get 
from clear_massage import clear_massage

class Imtest(object):
    def __init__(self,driver):   
        self.driver = driver      
      
    def test_recive(self):
        '''查找联系人，发送文本消息''' 
        #login.test_login(self,phoneid="13366778604")
        print "Start : %s" % time.ctime()
        time.sleep(5)
        print "Stop : %s" % time.ctime()
        k=0
        while k<10:
            k=k+1
            print k
            try:
                wq=str(self.driver.find_element_by_name(u"球球"))#名字
                if wq:
                    self.driver.find_element_by_name(u"球球").click()#点击球球
                    time.sleep(2)
                    try:
                        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv")
                        el=self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv")#定位
                        action1 = TouchAction(self.driver)
                        action1.long_press(el,duration=5000).perform()
                        self.driver.find_element_by_name(u"删除").click()
                        self.driver.find_element_by_id("dilaog_button3").click()
                        print u"已经删除数据"
                        self.driver.press_keycode('4')
                        self.driver.find_element_by_name(u"球球").click()#点击球球
                    except:
                        pass
                        print u"没有定位到接收文本"
                          
                    try:
                        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_voice_play_anim_tv")#删除接收语音
                        x1=self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_voice_play_anim_tv").location.get('x')
                        y1=self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_voice_play_anim_tv").location.get('y')
                        print x1,y1
                        x1=int(x1)+500
                        y1=int(y1)+100
                        print x1,y1
                        self.driver.tap([(x1,y1)],5000)
                        self.driver.find_element_by_name(u"删除").click()
                        self.driver.find_element_by_id("dilaog_button3").click()#确认删除 
                        self.driver.press_keycode('4')
                        self.driver.find_element_by_name(u"球球").click()#点击球球
                    except:
                        print u"没有定位到接收语音"       
  
                    try:
                        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_iv")
                        #删除接收的图片  
                        x1=self.driver.find_element_by_id("chatting_content_iv").location.get('x')
                        y1=self.driver.find_element_by_id("chatting_content_iv").location.get('y')
                        print x1,y1
                        x1=int(x1)+400
                        y1=int(y1)+100
                        print x1,y1
                        self.driver.tap([(x1,y1)],5000)
                        self.driver.find_element_by_name(u"删除").click()
                        self.driver.find_element_by_id("dilaog_button3").click()#确认删除 
                        self.driver.press_keycode('4')
                        self.driver.find_element_by_name(u"球球").click()#点击球球 
                    except:
                        print u"没有定位到接收图片"                         
                    try:
                        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/iv_file_mp4")
                        #删除接收的短视频   
                        action1 = TouchAction(self.driver)
                        el = self.driver.find_element_by_id("tv_filesize")
                        action1.long_press(el,duration=5000).perform()        
                        self.driver.find_element_by_name(u"删除").click()
                        self.driver.find_element_by_id("dilaog_button3").click()
                        self.driver.press_keycode('4')
                    except:
                        print u"没有定位到接收短视频" 
                    try:
                        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/re_location")  
                        #删除接收的定位信息
                        x1=self.driver.find_element_by_id("chatting_content_iv").location.get('x')
                        y1=self.driver.find_element_by_id("chatting_content_iv").location.get('y')
                        print x1,y1
                        x1=int(x1)+400
                        y1=int(y1)+100
                        print x1,y1
                        self.driver.tap([(x1,y1)],5000)
                        self.driver.find_element_by_name(u"删除").click()
                        self.driver.find_element_by_id("dilaog_button3").click()#确认删除 
                        self.driver.press_keycode('4')
                    except:
                        print u"没有定位到接收定位信息"                                                                                                        
            except:
                time.sleep(2)
                self.driver.press_keycode('4') 
                print u"完成一次尝试"
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_recive"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      