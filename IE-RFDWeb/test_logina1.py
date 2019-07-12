# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re


class WebLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.rufengda.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_kproduct1(self):
        u'''企业介绍及招聘'''
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        '''above=driver.find_element_by_class_name("business_join_count")#定位到要悬停的元素              
        ActionChains(driver).move_to_element(above).perform()        
        driver.find_element_by_css_selector("h3").click()
        middle_top=driver.find_element_by_class_name("middle_top").text
        self.assertEqual(middle_top,u"招商")
        driver.find_element_by_css_selector("a.list_div_no").click()
        middle_top=driver.find_element_by_class_name("middle_top").text
        self.assertEqual(middle_top,u"加盟")   '''      
        above=driver.find_element_by_class_name("talent_recruit_count")#定位到要悬停的元素             
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_css_selector("div.rczpSublisLiMiddle_middle > div.mcate-rczp-hd_right > a").click()
        middle_top=driver.find_element_by_class_name("middle_top").text
        self.assertEqual(middle_top,u"快递员")
        driver.find_element_by_link_text(u"系统工程师").click()
        driver.find_element_by_link_text(u"审计主管").click()
        driver.find_element_by_link_text(u"品牌推广专员").click()
        driver.find_element_by_link_text(u"培训主管").click()
        driver.find_element_by_link_text(u"稽查总监").click()
        above=driver.find_element_by_class_name("about_us_count")#定位到要悬停的元素              
        ActionChains(driver).move_to_element(above).perform()        
        driver.find_element_by_link_text(u"企业概况").click()
        middle_top=driver.find_element_by_class_name("middle_top").text
        self.assertEqual(middle_top,u"企业概况")     
        driver.find_element_by_css_selector("a.list_div_no").click()
        above=driver.find_element_by_class_name("about_us_count")#定位到要悬停的元素              
        ActionChains(driver).move_to_element(above).perform()        
        driver.find_element_by_link_text(u"公司荣誉").click()
        middle_top=driver.find_element_by_class_name("middle_top").text
        self.assertEqual(middle_top,u"公司荣誉")       
        above=driver.find_element_by_class_name("about_us_count")#定位到要悬停的元素              
        ActionChains(driver).move_to_element(above).perform()        
        driver.find_element_by_link_text(u"如风达新闻").click()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WebLogin("test_kproduct1"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)