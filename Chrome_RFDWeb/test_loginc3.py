# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random
from public import login
import HTMLTestRunner


class WebLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.rufengda.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    
            
    def test_c1add_adress(self):
        u'''新增地址'''
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.find_element_by_link_text(u"个人中心").click()
        login.login(self)
        driver.find_element_by_id("middle").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[2]/button").click()
        time.sleep(2)        
        driver.find_element_by_id("tagName").click()
        driver.execute_script("var x=document.getElementById(\"tagName\");x.value=\"home\";")
        driver.execute_script("var x=document.getElementById(\"contact\");x.value=\"WXE\";")
        driver.execute_script("var x=document.getElementById(\"mobile\");x.value=\"13366778604\";")
        driver.execute_script("var x=document.getElementById(\"contactAddress\");x.value=\"0105899999\";")

        driver.find_element_by_id("txt_area2").click()
        time.sleep(2)
        driver.find_element_by_id("120000").click()
        driver.find_element_by_id("120100").click()
        time.sleep(1)
        driver.find_element_by_id("120101").click()
        driver.execute_script("var x=document.getElementById(\"address\");x.value=\"address\";")
        driver.find_element_by_css_selector("button.button_blackbuttons.save_btn").click()
        #driver.find_element_by_css_selector("button.button_blackbuttons.save_btn").click()
        time.sleep(2)       
        #获取信息进行断言
        name1 = driver.find_element_by_id("s_contact").text #姓名
        self.assertEqual(name1,'WXE'.decode('utf-8'))
        mobile = driver.find_element_by_id("s_mobile").text #手机号
        self.assertEqual(mobile,'13366778604')
        contactAddress = driver.find_element_by_id("s_contactAddress").text #电话
        self.assertEqual(contactAddress,'0105899999')
        area = driver.find_element_by_id("s_areaName").text #地址
        self.assertEqual(area,'天津-天津市-和平区'.decode('utf-8'))
        adreess = driver.find_element_by_id("s_address").text #详细地址
        self.assertEqual(adreess,'address'.decode('utf-8'))
        
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WebLogin("test_c1add_adress"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)







    
