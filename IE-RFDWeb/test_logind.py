# -*- coding: utf-8 -*-
import Image    
import ImageEnhance    
import ImageFilter    
import sys    
import pytesseract
from ctypes import *
import ctypes
from PIL import ImageGrab
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
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.rufengda.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_dselect(self):
        u'''运单查询'''
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/img").click()
        driver.find_element_by_id("waybill").clear()
        driver.find_element_by_id("waybill").send_keys("11607161480198")
        time.sleep(5)
        img = ImageGrab.grab((825,371,907,399))#(left, upper, right, lower)
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
        self.assertEqual(numbera,'运单号：11607161480198'.decode('utf-8'))

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





    



