# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random
import HTMLTestRunner


class WebLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.rufengda.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    
            
    def test_ainformation(self):
        u'''会员信息验证'''
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.find_element_by_link_text(u"个人中心").click()
        login.login(self)
        driver.find_element_by_id("top").click()
        driver.find_element_by_id("grMessage").click()
        #验证个人信息正确性
        with open('D:\selenium_test\web.nickname.txt','r') as f:
            b1 = f.read()
        nickname = driver.find_element_by_id("nickname").text                                      #昵称显示            
        self.assertEqual(nickname,b1)
        sex = driver.find_element_by_id("sex").text                                                #性别显示           
        self.assertEqual(sex,'男'.decode('utf-8'))         
        birthday = driver.find_element_by_id("date").text                                      #页面生日显示
        self.assertEqual(birthday,'1990年1月1日'.decode('utf-8'))


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WebLogin("test_ainformation"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)







    
