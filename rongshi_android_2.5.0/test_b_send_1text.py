#coding:utf-8
import time,os
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from public import login
from public import logout
from public.extend import Appium_Extend 
from public.clear_massage import clear_massage
from public.clear_massage import clear_allmassage
from public.set_driver import set_driver
from public import set
from public import get
 
class Imtest(unittest.TestCase):
    #def __init__(self,driver):
        #self.driver = driver     
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver('192.168.1.103:5555','4723')#三星
        self.verificationErrors = []
        self.driver.implicitly_wait(10)                  
        self.extend = Appium_Extend(self.driver)
              
    def test_send_txt(self):
        '''查找联系人，发送各种文本消息'''
        try:
            time.sleep(2)
            self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_negative_btn").click()#点击取消下载
            logout.test_logout(self)#退出登录
        except:
            print ("未登录，无需执行退出登录操作") 
        #time.sleep(2)
        login.test_login(self,phoneid="13366778604",password="Abc123456")
        try:
            self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_negative_btn").click()#点击取消下载
        except:
            print (u"未弹出更新页")         
        #time.sleep(2)
        #clear_massage(self,name=u"容联幼稚园")
        clear_allmassage(self,accountnumber="com.yuntongxun.rongxin.lite:id/nickname_tv")
        #self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_search_et").click()#com.yuntongxun.rongxin.lite:id/input_search_et
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/input_search_et").send_keys("13671378634")
        #self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_my").click()#点击搜索 中文输入时无需收回键盘
        self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/name_tv").click()#点击账号
        #print "Start : %s" % time.ctime()
        time.sleep(2)
        try:
            self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_negative_btn").click()#点击取消下载
        except:
            print (u"未弹出更新页") 
        #发送文本消息 
        set.set1()
        text=get.get()
        text1=get.get1()
        text2=get.get2()
        text3=get.get3()
        text4=get.get4()
        text5=get.get5()
        text6=get.get6()
        text7=get.get7()

        list1=[text1,text2,text3,text4,text5,text6,text7]#   ,text2,text3,text4,text5,text6,text7
        for i in list1:
            self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_content_et").send_keys(i)#hello tester
            self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/chatting_send_btn").click()#发送
            time.sleep(2)
            #验证发送消息
            sendoutcontent = self.driver.find_element_by_id("chatting_content_itv").get_attribute("text")
            #print sendoutcontent
            self.assertEqual(sendoutcontent,i,msg=u"显示与输入不一致")
            #删除发送消息
            el = self.driver.find_element_by_id("chatting_content_itv")
            action1 = TouchAction(self.driver)
            action1.long_press(el,duration=5000).perform()
            self.driver.find_element_by_name(u"删除").click()
            self.driver.find_element_by_id("com.yuntongxun.rongxin.lite:id/ytx_positive_btn").click()
            print(u'发送消息'+ i)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_txt"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      