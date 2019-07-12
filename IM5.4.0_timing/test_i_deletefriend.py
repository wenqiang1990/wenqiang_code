#coding:utf-8
import time
import datetime 
import unittest
from appium.webdriver.common.touch_action import TouchAction
from robot.utils.asserts import *
from appium import webdriver
from public import login
from public import logout
timecode = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
from set_driver import set_driver
from clear_massage import clear_massage 
class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)        

    def test_addfriend(self):  
        '''删除好友''' 
        driver = self.driver
        time.sleep(2)
        member = "13366778604"  #要删除的好友
        time.sleep(2) 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys("13366778604")
        self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/account").click()#点击账号
        driver.find_element_by_xpath("//android.view.ViewGroup//android.widget.ImageButton[2]").click()#点击右上角设置
        driver.find_element_by_name(u"删除好友").click()#删除好友    
        print "delete friend success "           
          
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_addfriend"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      