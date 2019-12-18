#coding:utf-8
import time,os
import datetime 
from PIL import Image
import matplotlib.pyplot as plt
import unittest
from appium.webdriver.common.touch_action import TouchAction
from PIL import Image

from rongxin.public.extend import Appium_Extend
from rongxin.public.set_driver import set_driver
       
class Imtest(unittest.TestCase):
    #def __init__(self,driver):
        #self.driver = driver     
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver('e52f9b61','4723')
        self.verificationErrors = []
        self.driver.implicitly_wait(10)                  
        self.extend = Appium_Extend(self.driver)

                
    def test_send_txtB(self):#下载验证码图片
        for i in range(100):
            image = str(i)
            print(i)
            self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/verifyProgress_hx").click()#切换刷新验证码
            #self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/password").send_keys("Abc123456")
            time.sleep(1)
            element = self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/verifyCodePic")  
            self.extend.get_screenshot_by_element(element).write_to_file("f:\\screen", image)  
                        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_txtB"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)  
    
   
    
        