# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os, xlrd


class V2(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Ie()
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://login.wltest.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
  
    def test_v2(self):    
        driver = self.driver
        driver.get(self.base_url + "/?source=")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("0000034927")
        driver.find_element_by_id("loginPasswd").clear()
        driver.find_element_by_id("loginPasswd").send_keys("i#3ml%Kv$2M@V*r")
        #driver.find_element_by_id("VerificationCode").clear()
        #driver.find_element_by_id("VerificationCode").send_keys("hhhh")
        driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/form/button").click()
        time.sleep(12)   
        driver.find_element_by_link_text("客户").click()
        driver.find_element_by_link_text(u"快递").click()
        driver.find_element_by_link_text(u"受理单录入").click()
        time.sleep(2)
        frame=driver.find_element_by_xpath("/html/body/form/div[1]/div/table/tbody/tr[4]/td[2]/a/button")
        driver.switch_to_frame(frame)
        for i in range(1,30):
            driver.find_element_by_xpath("/html/body/form/div[1]/div/table/tbody/tr[2]/td[6]/a/button").click()#点击新增  
            driver.find_element_by_id("sendby").send_keys(u"温强")
            driver.find_element_by_id("mobilephone").clear()
            driver.find_element_by_id("mobilephone").send_keys("1336778604")
            driver.find_element_by_id("telephone").clear()
            driver.find_element_by_id("telephone").send_keys("01088888888")
            driver.find_element_by_id("mobilephone").clear()
            driver.find_element_by_id("mobilephone").send_keys("13366778604")
            Select(driver.find_element_by_id("sendprovince")).select_by_visible_text(u"北京")
            driver.find_element_by_css_selector(u"option[value=\"110000-北京\"]").click()
            Select(driver.find_element_by_id("sendcity")).select_by_visible_text(u"北京市")
            driver.find_element_by_css_selector(u"option[value=\"110100-北京市\"]").click()
            Select(driver.find_element_by_id("sendarea")).select_by_visible_text(u"大兴区")
            driver.find_element_by_id("sendaddress").clear()
            driver.find_element_by_id("sendaddress").send_keys(u"地盛北街1号")
            driver.find_element_by_id("toname").clear()
            driver.find_element_by_id("toname").send_keys(u"名字")
            driver.find_element_by_id("tomobile").clear()
            driver.find_element_by_id("tomobile").send_keys("13366778605")
            driver.find_element_by_id("tophone").clear()
            driver.find_element_by_id("tophone").send_keys("01055555555")
            Select(driver.find_element_by_id("toprovince")).select_by_visible_text(u"北京")
            driver.find_element_by_css_selector("option[value=\"110000\"]").click()
            Select(driver.find_element_by_id("tocity")).select_by_visible_text(u"北京市")
            driver.find_element_by_css_selector("option[value=\"110100\"]").click()
            Select(driver.find_element_by_id("toarea")).select_by_visible_text(u"海淀区")
            driver.find_element_by_id("toaddress").clear()
            driver.find_element_by_id("toaddress").send_keys(u"中国人民大学人大天文馆")
            driver.find_element_by_id("productname").clear()
            driver.find_element_by_id("productname").send_keys(u"我是物品名称")
            driver.find_element_by_id("select2-chosen-1").click()
            driver.find_element_by_id("s2id_autogen1_search").send_keys(u"菜鸟裹裹快件")
            driver.find_element_by_id("s2id_autogen1_search").send_keys(Keys.ENTER)
            driver.find_element_by_id("remark").clear()
            driver.find_element_by_id("remark").send_keys(u"温强备注哈哈哈哈哈")
            driver.find_element_by_id("ph").click()
            driver.find_element_by_id("totalweight").send_keys("1")
            driver.find_element_by_id("requirefetchtime").send_keys("2016-12-27 09:31:52")
            driver.find_element_by_id("submit").click()
            time.sleep(2)
            driver.switch_to_alert().accept()
            time.sleep(2)
      
    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(V2("test_v2"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)