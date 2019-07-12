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
    
            
    def test_c3delete_adress(self):
        u'''删除地址'''
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.find_element_by_link_text(u"个人中心").click()
        login.login(self)
        driver.find_element_by_id("middle").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[3]/div/div[1]/span/button[2]").click()
        time.sleep(5)
        driver.switch_to_alert().accept()
        time.sleep(3)
        driver.find_element_by_id("middle").click()
        #获取信息进行断言
        name1 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[3]/div/span").text
        print name1
        self.assertIn('您还没有任何地址，赶紧去 '.decode('utf-8'),name1)
        print u'删除成功'
        
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WebLogin("test_c3delete_adress"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)







    
