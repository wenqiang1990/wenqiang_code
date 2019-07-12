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
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.rufengda.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    
            
    def test_balter(self):
        u'''修改昵称'''
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.find_element_by_link_text(u"个人中心").click()
        login.login(self)
        driver.find_element_by_id("top").click()
        driver.find_element_by_id("grMessage").click()
        #修改昵称
        b = random.choice(["JGood", "is", "a", "handsome", "boy"])#从list中随机获取1个元素，返回
        driver.find_element_by_id("edit").click()
        driver.find_element_by_id("nname").clear()
        driver.find_element_by_id("nname").send_keys(b)
        driver.find_element_by_id("save").click()
        nickname = driver.find_element_by_id("nickname").text                                      #昵称显示
        self.assertEqual(nickname,b)
        with open('D:\selenium_test\web.nickname.txt','w') as f:
            f.write(b)

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







    
