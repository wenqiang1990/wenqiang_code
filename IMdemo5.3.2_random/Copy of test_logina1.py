#coding:utf-8
import os
import time 
#from sys import stdout
import datetime 
import unittest
import Image
from robot.utils.asserts import *
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from extend import Appium_Extend
from robot.result.keywordremover import WaitUntilKeywordSucceedsRemover
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S") 
class elementA(unittest.TestCase):    
    def setUp(self):    
        driver.implicitly_wait(30) #设置全局最大等待时间       
    def swipeUp(t):
        l=[1080,1980]
        x1=int(l[0]*0.5)  #x坐标
        y1=int(l[1]*0.75)   #起始y坐标
        y2=int(l[1]*0.25)   #终点y坐标
        driver.swipe(x1,y1,x1,y2,t)
        #屏幕向下滑动
    def swipeDown(t):
        l=[1080,1980]
        x1=int(l[0]*0.5)  #x坐标
        y1=int(l[1]*0.35)  #起始y坐标
        y2=int(l[1]*0.75)   #终点y坐标
        print [x1,y1,x1,y2]
        driver.swipe(x1,y1,x1,y2,t)
        #屏幕向左滑动
    def swipLeft(self,t):
        l=[1080,1980]
        x1=int(l[0]*0.75)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.05)
        print [x1,y1,x2,y1]
        driver.swipe(x1,y1,x2,y1,t)
        #屏幕向右滑动
    def swipRight(t):
        l=[1080,1980]
        x1=int(l[0]*0.05)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.75)
        driver.swipe(x1,y1,x2,y1,t)

           
         
        
        number = driver.find_element_by_id("edittext")
        self.assertIsNotNone(number)
        number.click()
        #driver.find_element_by_id("edittext").send_keys("13392")
        driver.find_element_by_id("edittext").set_text(timecode)
        driver.find_element_by_id("sign_in_button").click()#登陆
        
        print "Start : %s" % time.ctime()
        time.sleep(15)
        print "End : %s" % time.ctime()

        
        driver.find_element_by_xpath("//android.widget.EditText[@text='昵 称']").set_text("我是昵称")
        driver.find_element_by_xpath("//android.widget.EditText[@text='签 名']").set_text("I am signature")
        driver.find_element_by_id("sign_in_button").click()      
        
    def test_1(self):
        driver = elementA       
        time.sleep(5)   
        self.swipLeft(500)#左划
    
        #查找联系人
        driver.find_element_by_id("card_item_tv").click()
        driver.find_element_by_id("content").click()
        driver.find_element_by_id("content").send_keys("9999")
        driver.find_element_by_id("text_right").click()
        '''  
        #发送文本消息   
        driver.find_element_by_id("chatting_content_et").click()
        driver.find_element_by_id("chatting_content_et").send_keys("hello tester")
        time.sleep(5)
        driver.find_element_by_id("chatting_send_btn").click()
        #driver.press_keycode('66')
        driver.press_keycode('4')#按下返回键    
        driver.find_element_by_id("chatting_content_itv").click()
        time.sleep(2)
        sendoutcontent = driver.find_element_by_id("chatting_content_itv").get_attribute("text")
        print sendoutcontent
        receivecontent = driver.find_element_by_id("tv_read_unread").get_attribute("text")
        assert_equal(sendoutcontent,"hello tester",msg=u'发送的消息验证失败')
        assert_equal(receivecontent,u"未读")
        #driver.find_element_by_id("chatting_content_et").click()
        driver.find_element_by_id("chatting_mode_btn").click()
        time.sleep(2)

        #发送语音
        action1 = TouchAction(driver)  
        el = driver.find_element_by_id("voice_record_imgbtn")
        action1.long_press(el,duration=5000).perform()

        #发送图片
        driver.find_element_by_id("chatting_attach_btn").click()
        driver.find_element_by_id("app_grid_item_icon_mask").click()
        driver.find_element_by_id("imageview_photo").click()
        driver.find_element_by_id("text_right").click()
        time.sleep(5)
        '''
        #视频通话
        driver.find_element_by_id("chatting_attach_btn").click()
        driver.tap([(400,1660)], )#点击
        time.sleep(2)   
        test_get_screen_by_element()
        test_same_as()
        time.sleep(2)
        driver.find_element_by_id("video_botton_cancle").click()
        #image1=driver.find_element_by_xpath("//android.widget.RelativeLayout[last()]/LinearLayout/LinearLayout/LinearLayout/LinearLayout/ImageView")  
      
        #退出
        driver.find_element_by_id("btn_left").click()    
        driver.find_element_by_id("btn_plus").click()#加号
        time.sleep(2)
        driver.tap([(590,1190)], )#点击设置
        time.sleep(5)
        '''
        origin_el=driver.find_element_by_name("新消息声音")
        destination_el=driver.find_element_by_name("华为推送")
        driver.scroll(destination_el,origin_el)
        '''
        swipeUp(500)#上滑    
        driver.find_element_by_name(u"退出当前账号").click()
        driver.find_element_by_id("dilaog_button3").click()

        
        
        
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
              
          
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(elementA("test_1"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)







    
