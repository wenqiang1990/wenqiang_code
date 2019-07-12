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
        y1=int(l[1]*0.55)   #起始y坐标
        y2=int(l[1]*0.50)   #终点y坐标
        print [x1,y1,x1,y2]
        self.driver.swipe(x1,y1,x1,y2,t)
    
           
    def test_f_internationalflowmore(self):   
        '''国际流量更多''' 
        time.sleep(2)
        self.swipeUp(500)
        self.driver.find_element_by_id("tv_esim_more").click()#点击更多
        self.driver.find_element_by_id("iv_country").click()#点击国家 
        time.sleep(2)
        self.driver.context
        self.driver.find_element_by_id("tv_price").click()#点击套餐
        '''
        el=self.driver.find_element_by_id("tv_product_name").get_attribute("text")#获取套餐
        assert_equal(el, u"香港5日套餐", msg=u"点击流量套餐失败") 
        print u"国际流量列表更多入口验证通过"
        '''      
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_f_internationalflowmore"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)   