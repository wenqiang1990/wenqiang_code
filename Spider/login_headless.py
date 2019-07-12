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
import urllib
import urllib.request#代替urllib2
import urllib.error#代替urllib2
import requests


#driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

url = "http://192.168.178.12:8060/redmine/login"
driver.get(url)
driver.maximize_window()
wait = WebDriverWait(driver, timeout=10)
driver.find_element_by_id("username").send_keys("wenqiang")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_name("login").click()
#url = "http://192.168.178.12:8060/redmine/login"
#driver.get(url + "/index.html")
html=driver.page_source
soup = BeautifulSoup(html,'lxml')
#print(soup.prettify())
print("*********************************************************************************************************")
pattern = re.compile(r'版本测试')
linklist=[]
for link in soup.find_all('a'):
    #print (link)
    if re.search(pattern,str(link)):
        linklist.append(link.get('href'))
        
linklist=list(set(linklist))       
print (linklist) 
print("*********************************************************************************************************")
p = re.compile(r'\d+')
words =[]
i=0
while i<len(linklist):
    for x in linklist:
        print(i)
        m=''.join(re.findall(p,linklist[i]))
        #print(m)
        i=i+1
        #js_set = 'document.getElementById("q").value=m;'
        #driver.execute_script(js_set)
        #wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys(m)
        #wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys(Keys.ENTER)
        url='http://192.168.178.12:8060' + x
        r= requests.get(url)
        print('wenqiang')
        print(r.text)      
        print('wenqiang')
        #driver.find_element_by_id("q").send_keys(m)
        #driver.find_element_by_id("q").send_keys(Keys.ENTER)
        #html=driver.page_source
        html=r.text
        soup = BeautifulSoup(html,'lxml')
        text=soup.select('.subject h3')
        text=''.join('%s' %id for id in text)#st包含数字，不能直接转化成字符串,即遍历list的元素，把他转化成字符串
        pattern = re.compile('(?<=\>).*?(?=\<)')
        r=''.join(pattern.findall(text))#.jion转字符串
        print('*******************测试任务是:'+m+r+'*******************')
        #print(soup.select('.subject h3'))
        pattern = re.compile(r'缺陷报告')
        buglinklist=[]
        for link in soup.find_all('a'):
            if re.search(pattern,str(link)):
                buglinklist.append(link.get('href'))                             
        buglinklist1=list(set(buglinklist))
        j=0
        while j<len(buglinklist1):
            for x in buglinklist1:
                #print(j)
                print (re.findall(p,buglinklist1[j]))
                n=re.findall(p,buglinklist1[j])
                j=1+j
                #js_set = 'document.getElementById("q").value=m;'
                #js='document.getElementsByClassName("small")[0].click();'
                #driver.execute_script(js_set)
                #wait.until(expected.visibility_of_element_located((By.ID, 'q'))).send_keys(m + Keys.ENTER)
                url='http://192.168.178.12:8060' + x
                r= requests.get(url)
                print('wenqiang1111')
                print(r.text)
                print('wenqiang1111')
                #driver.find_element_by_id("q").send_keys(n)
                #driver.find_element_by_id("q").send_keys(Keys.ENTER)#搜索缺陷报告
                #html=driver.page_source
                html=r.text
                soup = BeautifulSoup(html,'lxml')
                text=soup.select('.subject h3')
                text=''.join('%s' %id for id in text)#st包含数字，不能直接转化成字符串,即遍历list的元素，把他转化成字符串
                pattern = re.compile('(?<=\>).*?(?=\<)')
                s=''.join(pattern.findall(text))
                print(s)
                #print(soup.select('.subject h3'))
                test=soup.find_all('div',class_="value")
                test='---'.join('%s' %id for id in test)#st包含数字，不能直接转化成字符串,即遍历list的元素，把他转化成字符串
                #print(test)
                pat = re.compile('(?<=\>).*?(?=\<)')
                #print(''.join(pat.findall(test)))
                t=''.join(pat.findall(test))
                pat = re.compile(r'---')
                l=re.split(pat,t)
                l1=l[0]+' '+l[4]+' '+l[12]+' '+l[13]
                words.append(l[0])
                #words.append(l[4])
                words.append(l[12])
                words.append(l[13])
                #words.append(l[j])
                print(l[0],l[4],l[12],l[13])
                with open('C:\\Users\\dodo\\Desktop\\test.txt','a',encoding='utf-8') as f:  #如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
                    f.write(l1+'\r\n')               
        l2=('↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑工单:'+m+' '+r+',共'+str(len(buglinklist1))+'个bug↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑')
        print(l2)
        print(words)
        print(Counter(words))
        with open('C:\\Users\\dodo\\Desktop\\test.txt','a',encoding='utf-8') as f:  #如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
            f.write(l2+'\r\n') 
else:
    print('over')
    driver.quit()    
    
    
    