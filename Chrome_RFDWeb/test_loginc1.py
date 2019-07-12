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
#import win32com.server.util, win32com.client

class WebLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.rufengda.com/")
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.rufengda.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    
            
    def test_c2update_adress(self):
        u'''修改地址'''
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.find_element_by_link_text(u"个人中心").click()
        login.login(self)
        driver.find_element_by_id("middle").click()
        driver.find_element_by_css_selector("button.button_blackbuttons.ulpdate_css").click()
        time.sleep(2)

        driver.find_element_by_css_selector(".item-address.bg_fuzzy_content")
        driver.find_element_by_css_selector("label").click()
        #driver.get("http://www.rufengda.com/auth/user.jsp")
        time.sleep(2)
        #driver.implicitly_wait(5)
        js="var x=document.getElementById(\"tagName\");x.value=\"My\";"  
        driver.execute_script(js)
        driver.find_element_by_css_selector(".fom").click()
        driver.find_element_by_css_selector("#contact").click()
        driver.execute_script("var x=document.getElementById(\"contact\");x.value=\"ZTZ\";")
        driver.execute_script("var x=document.getElementById(\"mobile\");x.value=\"13311267857\";")
        driver.execute_script("var x=document.getElementById(\"contactAddress\");x.value=\"\";")
        driver.execute_script("var x=document.getElementById(\"address\");x.value=\"address\";")
        
        #driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[1]/form/div[2]/span[1]/input").clear()
        #driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[1]/form/div[2]/span[1]/input").send_keys(u"赵铁柱")
        #driver.find_element_by_id("mobile").clear()
        #driver.find_element_by_id("mobile").send_keys("13311267857")
        #driver.find_element_by_id("contactAddress").clear()
        #driver.find_element_by_id("contactAddress").send_keys("")
        #driver.find_element_by_id("address").clear()
        #driver.find_element_by_id("address").send_keys(u"测试详细地址1")
        driver.find_element_by_css_selector("button.button_blackbuttons.save_btn").click()
        time.sleep(2)       
        #获取信息进行断言
        name1 = driver.find_element_by_id("s_contact").text #姓名
        self.assertEqual(name1,'ZTZ'.decode('utf-8'))
        mobile = driver.find_element_by_id("s_mobile").text #手机号
        self.assertEqual(mobile,'13311267857')
        contactAddress = driver.find_element_by_id("s_contactAddress").text #电话
        self.assertEqual(contactAddress,'')
        adreess = driver.find_element_by_id("s_address").text #详细地址
        self.assertEqual(adreess,'address'.decode('utf-8'))
        
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WebLogin("test_c2update_adress"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)







    
