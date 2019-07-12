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
    
            
    def test_cpassword(self):
        u'''修改密码'''
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.find_element_by_link_text(u"个人中心").click()
        login.login(self)
        driver.find_element_by_id("top").click()
        #修改密码功能
        ps2 = random.choice(['100000','100001','100002','100003','100004','100005','100006','100007','100008','100009','100010','100011','100012','100013','100014','100015','100016','100017','100018','100019','100020','100021','100022','100023','100024','100025','100026','100027','100028','100029','100030','100031'])
        time.sleep(3)
        driver.find_element_by_id("editPassword").click()
        with open('D:\selenium_test\web.password.txt','r') as f:
            ps1 = f.read()
        driver.find_element_by_id("oldPassword").clear()
        driver.find_element_by_id("oldPassword").send_keys(ps1)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(ps2)
        driver.find_element_by_id("tpassword").clear()
        driver.find_element_by_id("tpassword").send_keys(ps2)
        driver.find_element_by_id("confirm").click()
        time.sleep(2)
        #将修改后的新密码保存
        with open('D:\selenium_test\web.password.txt','w') as f:
            f.write(ps2)
        print 'new password is '+ps2  
        driver.find_element_by_class_name("login_out_bottom_count").click()#退出
        time.sleep(2)
        driver.find_element_by_link_text(u"个人中心").click()
        login.login(self)
        #获取信息进行断言
        name1 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/span[1]").text #右上角登录昵称
        with open('D:\selenium_test\web.nickname.txt','r') as f:
            b1 = f.read()
        self.assertEqual(name1,('\xe6\xac\xa2\xe8\xbf\x8e\xef\xbc\x9a'+b1).decode('utf-8'))
            
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WebLogin("test_cpassword"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)







    
