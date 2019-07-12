#coding:utf-8
from appium import webdriver
from robot.utils.asserts import * 
import time

desired_caps = {}
desired_caps['deviceName'] = '3a11d697'# 3a11d697 ：红米note3
desired_caps['platformName'] = 'Android'   
desired_caps['platformVersion'] = '5.1.1'   
desired_caps['appPackage'] = 'com.yuntongxun.ecdemo'  
desired_caps['appActivity'] = 'com.yuntongxun.ecdemo.ui.LauncherActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
verificationErrors = []
driver.implicitly_wait(10) 

'''登陆''' 
driver.find_element_by_id("edittext").set_text("13366778604")#timecode
driver.find_element_by_id("sign_in_button").click()#点击登陆                       
el=driver.find_element_by_id("com.yuntongxun.ecdemo:id/empty_conversation_tv").get_attribute("text")#页面文字
time.sleep(2)
assert_equal(el,u"暂无聊天信息",msg=u"登录失败")
print u"登陆成功------"+el
