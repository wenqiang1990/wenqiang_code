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
        driver.find_element_by_link_text(u"出库交接表").send_keys(Keys.TAB)
        driver.find_element_by_link_text(u"逐单出库(新)").send_keys(Keys.TAB)      
        driver.find_element_by_link_text(u"批量出库(新)").click()
           

        time.sleep(5)
        frame=driver.find_element_by_xpath("/html/body/div/div[1]/div[3]/div/iframe[2]")
        driver.switch_to_frame(frame)
        driver.find_element_by_id("select2-selectedtationValue-container").click()
        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys(u"北京亦庄站")
        driver.find_element_by_xpath("/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
        driver.find_element_by_id("scanNos").click()#定位单号输入框
        data = xlrd.open_workbook('C:\\Users\\wenqiang.RFDOA\\Desktop\\zhuoyue.xlsx') # 打开xls文件
        table = data.sheets()[0] # 打开第一张表
        nrows = table.nrows # 获取表的行数
        list =[]
        for i in range(nrows): # 循环逐行打印
            if i == 0: # 跳过第一行
                continue
            list.append(int(table.row_values(i)[1]))
            list.append('\n') #添加换行符
        driver.find_element_by_id("scanNos").send_keys(list)
        driver.find_element_by_id("btnStartOutbound").click()
        time.sleep(10)
      
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