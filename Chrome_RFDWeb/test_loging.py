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
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.rufengda.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_gselect(self):
        u'''收送范围查询'''
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.find_element_by_xpath("//div[@id='imgCont']/div/div/div[4]/div/img").click()
        driver.find_element_by_id("txt_area").click()
        driver.find_element_by_id("120100").click()
        driver.find_element_by_id("120106").click()
        driver.find_element_by_id("submit").click()
        time.sleep(2)#此处添加等待时间否则找不到元素
        #检查点
        #a=driver.find_element_by_class_name("bottom_fu").text
        #print a
        wq = driver.find_element_by_id("ssfw_addres").text
        print wq
        self.assertEqual(wq,u'天津市-天津市-红桥区')
        wq1 = driver.find_element_by_id("resultContent").text
        print wq1
        self.assertEqual(wq1,u'全境提供服务')
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WebLogin("test_gselect"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)


    
