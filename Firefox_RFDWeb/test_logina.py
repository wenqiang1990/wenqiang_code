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
    #def failrun(n=3):  
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
    def test_ainformation(self):
        u'''会员信息验证'''
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        testreport = 'D:/selenium_test/test_page_date/'
        wq=testreport+now+'screenshot_error.jpg'        
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.find_element_by_link_text(u"个人中心").click()
        login.login(self)
        try:
            driver.find_element_by_id("top").click()
        except: 
            img = ImageGrab.grab()
            img.save(wq,'JPEG')
        try:        
            driver.find_element_by_id("grMessage").click()
        except: 
            img = ImageGrab.grab()
            img.save(wq,'JPEG')
        #验证个人信息正确性
        with open('D:\selenium_test\web.nickname.txt','r') as f:
            b1 = f.read()
        nickname = driver.find_element_by_id("nickname").text                                      #昵称显示            
        self.assertEqual(nickname,b1)
        sex = driver.find_element_by_id("sex").text                                                #性别显示           
        self.assertEqual(sex,'男'.decode('utf-8'))         
        birthday = driver.find_element_by_id("date").text
        #self.assertEqual(birthday,'1990年1月1日'.decode('utf-8'))                                      #页面生日显示
        try:
            self.assertEqual(birthday,'1990年1月1日'.decode('utf-8'))
        except AssertionError as err:
            print '用例失败原因:%s'%err
            img = ImageGrab.grab()
            img.save(wq,'JPEG')
            raise AssertionError
        driver.find_element_by_class_name("login_out_bottom_count").click()

  
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







    
