# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random
from public import login
from selenium.webdriver.common.action_chains import ActionChains
import HTMLTestRunner


class WebLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.rufengda.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    
            
    def test_kproduct(self):
        u'''产品与服务'''
        driver = self.driver
        driver.get(self.base_url + "/front/articleShow.do?name=RFDDT")      
        above=driver.find_element_by_class_name("product_service_count")#定位到要悬停的元素              
        driver.find_element_by_class_name("mcate-hzsj-hd")
        ActionChains(driver).move_to_element(above).perform()
                                                             
        driver.find_element_by_link_text(u"普通快递").click()
        
        driver.find_element_by_css_selector("a.list_div_no").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'干线运输')])[6]").click()
        driver.find_element_by_link_text(u"高价值商品配..").click()
        driver.find_element_by_link_text(u"光速达（两小..").click()

             
        above=driver.find_element_by_class_name("product_service_count")#定位到要悬停的元素  
        time.sleep(2) 
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(2)
        ActionChains(driver).move_by_offset(0, 70).perform()#向下移动70个像素到电商
        #driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[1]/div[3]/div[2]/ul[2]").is_displayed()
        #ActionChains(driver).move_to_element(dri).perform()
          
        driver.find_element_by_xpath(u"(//a[contains(text(),'保价服务')])[2]").click()
        driver.find_element_by_css_selector("a.list_div_no").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'签单返回')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'代收货款')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'系统对接服务')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'定时配送服务')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'夜间配送服务')])[6]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'包装服务')])[6]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'超区转寄')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'电子账单')])[6]").click()
        driver.find_element_by_id("mone").click()
        driver.find_element_by_css_selector("li.list_li_mone > a.list_div_no").click()
        driver.find_element_by_link_text(u"收件人信息保..").click()
        driver.find_element_by_link_text(u"自寄/自取服..").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'上门取件')])[4]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'财务结算')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'短信通知服务')])[6]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'定制化服务')])[6]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'试穿试戴')])[2]").click()
        
        above=driver.find_element_by_class_name("product_service_count")#定位到要悬停的元素  
        time.sleep(2) 
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(2)
        ActionChains(driver).move_by_offset(180, 70).perform()#向下移动70个像素向右移动180像素到个人
        driver.find_element_by_xpath(u"(//a[contains(text(),'保价服务')])[3]").click()
        driver.find_element_by_css_selector("a.list_div_no").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'夜间配送服务')])[6]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'包装服务')])[6]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'超区转寄')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'电子账单')])[6]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'改派服务')])[6]").click()
        driver.find_element_by_link_text(u"收件人信息保..").click()
        driver.find_element_by_link_text(u"自寄/自取服..").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'上门取件')])[4]").click()
        driver.find_element_by_id("mone").click()
        driver.find_element_by_css_selector("li.list_li_mone > a.list_div_no").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'定制化服务')])[6]").click()
        ''' 鼠标移动路径问题导致无法定位到以下两个模块，待解决！ 
        above=driver.find_element_by_class_name("product_service_count")#定位到要悬停的元素  
        time.sleep(2) 
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(2)
        ActionChains(driver).move_by_offset(355, 70).perform()#向下移动70个像素向右移动360像素  到3C
        driver.find_element_by_xpath(u"(//a[contains(text(),'夜间配送服务')])[4]").click()           
        driver.find_element_by_css_selector("a.list_div_no").click()
        driver.find_element_by_css_selector("a.list_div_no").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'签单返回')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'代收货款')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'系统对接服务')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'定时配送服务')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'包装服务')])[6]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'超区转寄')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'电子账单')])[6]").click()
        driver.find_element_by_id("mone").click()
        driver.find_element_by_css_selector("li.list_li_mone > a.list_div_no").click()
        driver.find_element_by_link_text(u"收件人信息保..").click()
        driver.find_element_by_link_text(u"自寄/自取服..").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'上门取件')])[4]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'财务结算')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'短信通知服务')])[6]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'定制化服务')])[6]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'定制化服务')])[5]").click()
        
        above=driver.find_element_by_class_name("product_service_count")#定位到要悬停的元素  
        time.sleep(2) 
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(2)
        ActionChains(driver).move_by_offset(550, 70).perform()#向下移动70个像素向右移动360像素  到金融      
       
        driver.find_element_by_id("mone").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'短信通知服务')])[6]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'财务结算')])[5]").click()
        driver.find_element_by_link_text(u"收件人信息保..").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'改派服务')])[6]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'电子账单')])[6]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'超区转寄')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'包装服务')])[6]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'夜间配送服务')])[6]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'定时配送服务')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'系统对接服务')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'代收货款')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'签单返回')])[5]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'退、换货服务')])[5]").click()
        driver.find_element_by_css_selector("a.list_div_no").click()
        driver.find_element_by_css_selector("h3").click()
        driver.find_element_by_css_selector("a.list_div_no").click()
        driver.find_element_by_css_selector("div.rczpSublisLiMiddle_middle > div.mcate-rczp-hd_right > a").click()
        driver.find_element_by_link_text(u"企业概况").click()
        driver.find_element_by_css_selector("a.list_div_no").click()
        driver.find_element_by_link_text(u"公司荣誉").click()
        driver.find_element_by_link_text(u"如风达新闻").click()
        driver.find_element_by_link_text(u"行业动态").click()
        driver.find_element_by_link_text(u"媒体聚焦").click()
        '''
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WebLogin("test_kproduct"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)