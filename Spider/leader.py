# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re,time
import copy
import string
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
from collections import Counter
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
'''
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
'''
url = "http://192.168.178.12:8060/redmine/login"
driver.get(url)
driver.maximize_window()
wait = WebDriverWait(driver, timeout=10)
driver.find_element_by_id("username").send_keys("wenqiang")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_name("login").click()
driver.find_element_by_link_text(u"指派给我的问题").click()
driver.find_element_by_id("add_filter_select").click()
s1 = Select(driver.find_element_by_id("add_filter_select"))# 实例化Select
s1.select_by_value("tracker_id")#选择value="tracker_id"的项
s1.select_by_value("member_of_group")
s1.select_by_value("created_on")
driver.find_element_by_id("cb_assigned_to_id").click()#取消勾选
s2 = Select(driver.find_element_by_id("operators_status_id"))# 实例化Select
s2.select_by_value("*")#选择value="跟踪"的项
s3 = Select(driver.find_element_by_id("values_tracker_id_1"))# 实例化Select
s3.select_by_value("13")#选择value="跟踪"的项
s4 = Select(driver.find_element_by_id("values_member_of_group_1"))# 实例化Select
s4.select_by_value("321")#选择value="跟踪"的项
s5 = Select(driver.find_element_by_id("operators_created_on"))# 实例化Select
s5.select_by_value("m")#选择value="跟踪"的项
driver.find_element_by_link_text(u"应用").click()
driver.find_element_by_class_name("csv").click()
driver.find_element_by_id("csv_columns_all").click()#勾选
driver.find_element_by_css_selector('#csv-export-form > p.buttons > input[type="submit"]:nth-child(1)').click()#勾选







'''
#开始获取页面数据
html=driver.page_source
soup = BeautifulSoup(html,'lxml')
print("*********************************************************************************************************")

html=driver.page_source
soup = BeautifulSoup(html,'lxml')
text=soup.select('.subject h3')
text=''.join('%s' %id for id in text)#st包含数字，不能直接转化成字符串,即遍历list的元素，把他转化成字符串
pattern = re.compile('(?<=\>).*?(?=\<)')
r=''.join(pattern.findall(text))#.jion转字符串
print('*******************测试任务是:'+r+'*******************')
test=soup.find_all('div',class_="value")
test='---'.join('%s' %id for id in test)#st包含数字，不能直接转化成字符串,即遍历list的元素，把他转化成字符串
#print(test)
pat = re.compile('(?<=\>).*?(?=\<)')
#print(''.join(pat.findall(test)))
t=''.join(pat.findall(test))
pat = re.compile(r'---')
l=re.split(pat,t)
l1=l[0]+' '+l[4]+' '+l[12]+' '+l[13]
#words.append(l[j])
print(l[0],l[4],l[12],l[13])
with open('C:\\Users\\dodo\\Desktop\\test.txt','a',encoding='utf-8') as f:  #如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
    f.write(l1+'\r\n')               
print('over')
driver.quit()  
'''  