#coding:utf-8
import os
import time
import datetime 
import unittest
from robot.utils.asserts import *
from appium import webdriver
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S") 
class Imtest(unittest.TestCase):    
    def setUp(self):    
        desired_caps = {}
        desired_caps['deviceName'] = '3a11d697'  
        desired_caps['platformName'] = 'Android'   
        desired_caps['platformVersion'] = '5.1.1'   
        desired_caps['appPackage'] = 'com.yuntongxun.yuya'  
        desired_caps['appActivity'] = 'com.yuntongxun.yuya.ui.guilder.SplashActivity' 
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.verificationErrors = []
        self.driver.implicitly_wait(30)

        #获得机器屏幕大小x,y
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        l=[x,y]
        print l
        with open('F:\Appium\size\size.txt','w') as f:
            for i in range(len(l)):
                f.write(str(l[i])+'\n')                         
                print l[i]
            f.close()
              
    #屏幕向上滑动
    def swipeUp(self,t):
        with open('F:\Appium\size\size.txt','r') as f:
            l = f.readlines()
            for i in range(len(l)):
                l[i] = int(l[i][:len(l[i])-1])
            print l
        x1=int(l[0]*0.5)    #x坐标
        y1=int(l[1]*0.75)   #起始y坐标
        y2=int(l[1]*0.25)   #终点y坐标
        print [x1,y1,x1,y2]
        self.driver.swipe(x1,y1,x1,y2,t)
    
           
    def test_login(self):   
        '''国际成品卡热门国家入口''' 
        time.sleep(5)
        self.swipeUp(500)
        time.sleep(2)      
        self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[2]/android.widget.LinearLayout").click()#点击第一个热门国家
        
        time.sleep(2)
        self.driver.find_element_by_id("tv_name").click()
        el=self.driver.find_element_by_name("成品卡详情").get_attribute("text")#获取国际流量详情
        assert_equal(el, u"成品卡详情", msg=u"成品卡详情展示失败")
        el=self.driver.find_element_by_id("tv_address_get_notice").get_attribute("text")#获取国际流量详情
        assert_equal(el, u"物流地址", msg=u"物流地址展示失败")            
        self.driver.press_keycode('4')#点击返回
        time.sleep(2)        
        self.driver.press_keycode('4')#点击返回   

                      
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_login"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)   