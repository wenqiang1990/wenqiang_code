#coding:utf-8
import time
from robot.utils.asserts import *
from appium import webdriver
         
def test_login(self,el="13311267857"):   
    '''登陆，设置用户信息''' 
    try:
        number = self.driver.find_element_by_id("phone__login")
        self.assertIsNotNone(number)
        number.click()
        self.driver.find_element_by_id("edittext").set_text(el)#timecode
        self.driver.find_element_by_name(u"请输入密码").set_text('111111')
        self.driver.find_element_by_id("phone_sign_in_button").click()#点击登陆                     
        print u"成功点击登陆" 
    except:
        print u"可能已经登录或者需要设置"            
                     
    #强制等待
    print "Start : %s" % time.ctime()
    time.sleep(2)
    print "End : %s" % time.ctime()
    try: 
        #设置个人信息
        #self.driver.find_element_by_xpath("//android.widget.EditText[@text='昵 称']").set_text(el)
        #self.driver.find_element_by_xpath("//android.widget.EditText[@text='I am signature']").set_text("I am signature")
        self.driver.find_element_by_id("sign_in_button").click()
        el=self.driver.find_element_by_name(u"沟通").get_attribute("text")
        assert_equal(el, u"沟通", msg=u"登陆失败")            
        print u"完成个人信息设置，进入主页面" 
    except:
        print u"已经登录，或者是老账号登陆，不需要设置"


#test_login(13366778604)

