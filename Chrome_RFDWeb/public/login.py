#coding=utf-8
#登录
import time
def login(self):
    driver = self.driver
    #driver.find_element_by_link_text(u"个人中心").click()
    with open('D:\selenium_test\web.password.txt','r') as f:
        ps1 = f.read()
    driver.find_element_by_id("account").clear()
    driver.find_element_by_id("account").send_keys('13366778604')
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(ps1)
    driver.find_element_by_id("login_button").click()
    #退出
#def logout(self):
   # driver = self.driver
    #driver.find_element_by_class_name("login_out_bottom_count").click()#退出
   
