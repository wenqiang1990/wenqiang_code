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
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.rufengda.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    '''def decorator(func):  
        def wrapper(*args,**kw):  
            for i in range(3):  
                try:  
                    r=func(*args,**kw)
                    return r  
                except AssertionError as err:  
                    print '用例失败原因:%s'%err  
            raise AssertionError  
        return wrapper  
    #return decorator

    #test_ainformation=decorator()
    @decorator'''
   
    def test_kproduct1(self):
        u'''招商加盟'''
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        above=driver.find_element_by_class_name("business_join_count")#定位到要悬停的元素              
        ActionChains(driver).move_to_element(above).perform()        
        driver.find_element_by_css_selector("h3").click()
        middle_top=driver.find_element_by_class_name("middle_top").text
        self.assertEqual(middle_top,u"招商")
        driver.find_element_by_css_selector("a.list_div_no").click()
        middle_top=driver.find_element_by_class_name("middle_top").text
        self.assertEqual(middle_top,u"加盟")        
    
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
