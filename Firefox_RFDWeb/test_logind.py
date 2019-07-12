# -*- coding: utf-8 -*-
import Image   
import sys    
import pytesseract
from ctypes import *
import ctypes
from PIL import Image
from PIL import ImageGrab,ImageEnhance,ImageFilter
from selenium import webdriver
import os
import time
import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random
from public import login
class WebLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.rufengda.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    '''def decorator(func):  
        def wrapper(*args,**kw):  
            for i in range(3):  
                try:  
                    r=func(*args,**kw)
                    return r  
                except AssertionError as err:  
                    print '用例失败原因:%s'%err  
            raise AssertionError  
        return wrapper  
    #return decorator

    #test_ainformation=decorator()
    @decorator'''   
    def test_dselect(self):
        u'''运单查询'''
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        testreport = 'D:/selenium_test/test_page_date/'
        wq=testreport+now+'screenshot_error.jpg'
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/img").click()
        driver.find_element_by_id("waybill").clear()
        driver.find_element_by_id("waybill").send_keys("11607161480198")
        time.sleep(5)
        img = ImageGrab.grab((794,464,890,499))#(left, upper, right, lower)
        #img.show()
        img.save('D:/selenium_test/test_date/004.jpg','JPEG')
        imageObject=Image.open('D:\\selenium_test\\test_date\\004.jpg')
        #print (imageObject)
        #print (pytesseract.image_to_string(imageObject))      
        number = pytesseract.image_to_string(imageObject)
        time.sleep(5)
        driver.find_element_by_id("code_yzm").clear()
        driver.find_element_by_id("code_yzm").send_keys(number)
        driver.find_element_by_id("code_submit_waybill").click()
        time.sleep(3)
        numbera = driver.find_element_by_class_name("ydcx_js_yd").text
        print numbera
        try:
            self.assertEqual(numbera,'运单号：11607161480198'.decode('utf-8'))
        except AssertionError as err1:
            print '校验失败:%s'%err1
            img = ImageGrab.grab()
            img.save(wq,'JPEG')
            raise AssertionError
            
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WebLogin("test_dselect"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)





    



