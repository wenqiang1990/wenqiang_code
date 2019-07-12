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
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.rufengda.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_eselect(self):
        u'''受理单查询'''
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.find_element_by_css_selector("div.pf_all_div_other > img.top_float_image").click()
        driver.find_element_by_id("acceptance_list").click()
        driver.find_element_by_id("sldCode").clear()
        driver.find_element_by_id("sldCode").send_keys("SL160901000018")
        time.sleep(5)
        #截取验证码
        img = ImageGrab.grab((794,466,890,501))#(left, upper, right, lower)
        #img.show()
        img.save('D:/selenium_test/test_date/001.jpg','JPEG')
        imageObject=Image.open('D:\\selenium_test\\test_date\\001.jpg')
        #print (imageObject)
        #print (pytesseract.image_to_string(imageObject))      
        number = pytesseract.image_to_string(imageObject)
        time.sleep(5)
        driver.find_element_by_id("sld_yzm").clear()
        driver.find_element_by_id("sld_yzm").send_keys(number)
        driver.find_element_by_id("code_submit_sld").click()
        #检查点
        number1 = driver.find_element_by_class_name("ydcx_js_yd").text
        self.assertEqual(number1,'受理单号：SL160901000018'.decode('utf-8'))
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WebLogin("test_eselect"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)





    
