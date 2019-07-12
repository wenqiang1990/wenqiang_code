#coding=utf-8
from selenium import webdriver
import unittest, time, re, random, os
import pytesseract
from PIL import ImageGrab
import Image
from selenium.webdriver.remote.switch_to import SwitchTo

class WebLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://123.57.140.180:9060/login"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def screen(self):
        for i in range(1,10):
            self.driver.find_element_by_id("img").click()
            img = ImageGrab.grab((832,422,920,463))#(left, upper, right, lower)
            img.save('F:\\screen\\website\\001.jpg','JPEG') 
            time.sleep(2)
            imageObject=Image.open('F:\\screen\\website\\001.jpg')        
            number = pytesseract.image_to_string(imageObject)
            if number == '':
                pass
            else:
                break
        return number
        
            
    def test_balter(self):
        u'''登录'''
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.find_element_by_id("username").send_keys("wq")
        driver.find_element_by_id("password").send_keys("wq123456")
        driver.find_element_by_id("code").click()
        '''
        img = ImageGrab.grab((832,422,920,463))#(left, upper, right, lower)
        #img.show()
        img.save('F:\\screen\\website\\001.jpg','JPEG') 
        time.sleep(2)
        imageObject=Image.open('F:\\screen\\website\\001.jpg')
        #print (imageObject)
        #print (pytesseract.image_to_string(imageObject))      
        number = pytesseract.image_to_string(imageObject)
        if number == '':
            print u"验证码是"+number
            driver.find_element_by_id("img").click()     
        '''      
        NO=self.screen()
        print NO
        driver.find_element_by_id("code").send_keys(NO)
        driver.find_element_by_id("subBtn").click()
        
        #
        driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div[1]/ul/li[3]/a/span").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div[1]/ul/li[3]/ul/li[2]/a").click()
        #driver.switch_to_frame(frame_reference)
        
        
        driver.find_element_by_id("queryGoodsKeyWord").send_keys(u"香港")
        driver.find_element_by_class_name("btn btn-default waves-effect waves-light").click()
        driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div[1]/div/div[2]/div/div/div[2]/table/tbody/tr/td[10]/div[2]/i").click()
        driver.find_element_by_id("status").click()
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div[2]/div/div/div[2]/form/div[8]/div[1]/select/option[3]").click()
        driver.find_element_by_id("saveBtn").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WebLogin("test_balter"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)