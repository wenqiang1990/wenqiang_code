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
    
    def test_hmail(self):
        u'''我要寄件'''
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.find_element_by_css_selector("img.top_float_image").click()
        driver.find_element_by_id("SendBy").clear()
        driver.find_element_by_id("SendBy").send_keys(u"测试")
        time.sleep(2)
        driver.find_element_by_id("txt_area1").click()
        time.sleep(2)
        driver.find_element_by_id("110000").click()
        driver.find_element_by_id("110100").click()
        driver.find_element_by_id("110101").click()
        driver.find_element_by_id("ToAddress").clear()
        driver.find_element_by_id("ToAddress").send_keys(u"详细地址")
        driver.find_element_by_id("MobilePhone").clear()
        driver.find_element_by_id("MobilePhone").send_keys("13366778604")
        driver.find_element_by_id("Remark").clear()
        driver.find_element_by_id("Remark").send_keys(u"测试备注")
        driver.find_element_by_id("submit").click()   
        time.sleep(6)
        #检查点
        wq = driver.find_element_by_class_name("font_notice").text
        print wq
        self.assertEqual(wq,u'提供您的寄件信息，即刻预约配送员上门为您取件')
        time.sleep(5)
        code = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[4]/div").text
        print code
        self.assertIn(u'受理单号是',code)

        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WebLogin("test_hmail"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)


    
