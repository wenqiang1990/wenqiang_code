#coding:utf-8
import time,os
from pytesseract import *
import pytesseract
from PIL import Image
from PIL import ImageGrab,ImageEnhance,ImageFilter
#from robot.utils.asserts import *
from public.extend import Appium_Extend
from appium import webdriver
from public import tast


threshold = 80    #数值越小，越会忽略颜色较淡的地方
table = []    
for i in range(256):    
    if i < threshold:    
        table.append(0)    
    else:    
        table.append(1)
        
def test_login(self,phoneid="13366778604",password=""):#
    '''登陆'''   
    k=0
    while k<2:
        k=k+1
        try:
            wq=str(self.driver.find_element_by_name(u"登录"))#登录标签
            if wq:
                self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/action_option_button").click()#切换账号
                self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/mobile").send_keys(phoneid)#timecode
                #self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/verifyProgress_hx").click()#切换刷新验证码
                element = self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/verifyCodePic")
                time1 = (str(time.strftime("%Y%m%d%H%M%S", time.localtime())))
                imageopen = str('f:\\screen\\' + time1 + '.png')
                self.extend.get_screenshot_by_element(element).write_to_file("f:\\screen", time1)
                print(imageopen)
                tast.verify(time1)#调用函数对比
                self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/password").send_keys(password)
                print("账号:{} 密码:{}".format(phoneid,password))
                f = open('F:\\screen\\q\\'+time1+'\\presult.txt', 'r')
                f=f.read()
                print(f)
                self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/verifyCodeEt").send_keys(f)#验证码
                #self.driver.press_keycode('4')#点击返回键
                self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/sign_in_button").click()#点击登陆
                time.sleep(2)
                print ("点击登陆并等待了2秒")
        except:
            print ("账号%s登录异常" %phoneid)
       
#test_login(13366778604)
