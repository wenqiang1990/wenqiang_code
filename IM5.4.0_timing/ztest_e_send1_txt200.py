#coding:utf-8
import time
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
from clear_massage import clear_massage
import set
import get 
from set_driver import set_driver 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)        
  
    def test_send_txt200(self):  
        '''群成员发送文本消息''' 
        clear_massage(self,name="groupname1")
        clear_massage(self,name=u"系统通知")
        driver = self.driver
        with open('F:\Appium\group\groupID.txt','r') as f:
            el=f.read()
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        el=u"群组id:"+el
        driver.find_element_by_name(el).click()#点击群组id,以后改为读取上一条用例创建群组的id 
        #群成员发送@消息
        set.set1()
        text200=get.get()
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_et").send_keys(text200)#输入特殊字符
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_send_btn").click()#点击发送
        #验证接收消息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv").get_attribute("text")
        assert_equal(el,text200,msg=u'消息验证失败')
        print "群组内发送消息成功"     
        #删除发送消息
        el = self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv")
        action1 = TouchAction(self.driver)
        action1.long_press(el,duration=5000).perform()
        self.driver.find_element_by_name(u"删除").click()
        self.driver.find_element_by_id("dilaog_button3").click()    
        '''        
        while True:
            try:
                wq=str(self.driver.find_element_by_name(u"球球"))#名字
                while wq:
                    el = self.driver.find_element_by_id("chatting_content_itv").get_attribute("text")
                    assert_equal(el,text1,msg=u'接收的消息验证失败')
                    el=self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/chatting_content_itv")#定位
                    action1 = TouchAction(self.driver)
                    action1.long_press(el,duration=5000).perform()
                    self.driver.find_element_by_name(u"删除").click()
                    self.driver.find_element_by_id("dilaog_button3").click()
                    print u"已经删除数据" 
                             
            except:
                time.sleep(2)
                print u"已经删除数据"
                break 
    '''              
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_send_txt200"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      