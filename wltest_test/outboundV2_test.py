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
        time.sleep(6)
        driver.find_element_by_link_text(u"分拣").click()
        driver.find_element_by_link_text(u"分拣管理").click()
        driver.find_element_by_link_text(u"外阜编号维护(新)").send_keys(Keys.TAB)
        #driver.find_element_by_link_text(u"城际装车").send_keys(Keys.TAB)
        driver.find_element_by_link_text(u"城际卸车").send_keys(Keys.TAB)
        driver.find_element_by_link_text(u"散件扫描").send_keys(Keys.TAB)
        driver.find_element_by_link_text(u"同城单量统计(新)").send_keys(Keys.TAB)
        driver.find_element_by_link_text(u"同城单量扫描(新)").send_keys(Keys.TAB)
        driver.find_element_by_link_text(u"同城卸车").send_keys(Keys.TAB)
        driver.find_element_by_link_text(u"逐单入库(新)").send_keys(Keys.TAB)
        driver.find_element_by_link_text(u"批量入库(新)").send_keys(Keys.TAB)
        driver.find_element_by_link_text(u"出库交接表").click()
        time.sleep(5)
        frame=driver.find_element_by_xpath("/html/body/div/div[1]/div[3]/div/iframe[2]")
        driver.switch_to_frame(frame)
        driver.find_element_by_id("userId").send_keys("0000034927")
        driver.find_element_by_id("unbatchSeach").click()
        driver.find_element_by_xpath("/html/body/div/div/div[4]/div[2]/div[2]/table/thead/tr/th[1]/div[1]/input").click()
        driver.find_element_by_id("onbatch").click()
        time.sleep(2)
        driver.find_element_by_id("onbatchSeach").click()
        driver.find_element_by_xpath("/html/body/div/div/div[4]/div[2]/div[2]/table/thead/tr/th[8]/div[1]").click()
        #driver.find_element_by_id("jqgh_jqGrid_batchNo").click()
        time.sleep(2)  
        outboundBatch=driver.find_element_by_xpath("/html/body/div/div/div[4]/div[2]/div[2]/table/tbody/tr/td[8]").text#获取title的值
        print outboundBatch
        txt=open("D:\\selenium_test\\Batch1.txt","w")
        txt.truncate()
        txt.write(outboundBatch)
        txt.close()
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