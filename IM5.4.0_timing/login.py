#coding:utf-8
from appium import webdriver
from public import initialize

initialize.initialize(udid='aa8af450')
driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_name").set_text(id)#timecode
driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_pwd").set_text("111111")
driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_login").click()#点击登陆                     
print (u"成功点击登陆")   
