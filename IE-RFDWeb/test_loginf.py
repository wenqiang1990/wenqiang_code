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
    
    def test_fselect(self):
        u'''运费查询'''
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.find_element_by_xpath("//div[@id='imgCont']/div/div/div[3]/div/img").click()
        driver.find_element_by_id("txt_area1").click()
        
        driver.find_element_by_id("110101").click()
        time.sleep(2)
        driver.find_element_by_id("txt_area2").click()
        driver.find_element_by_id("110102").click()
        driver.find_element_by_id("freight_submit").click()
        #检查点
        number1 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/table/tbody/tr[3]/td[4]").text
        print number1
        self.assertEqual(number1,'12')
        number2 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/table/tbody/tr[3]/td[1]").text
        print number2
        self.assertEqual(number2,'快递新品'.decode('utf-8'))
        
        
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WebLogin("test_fselect"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
