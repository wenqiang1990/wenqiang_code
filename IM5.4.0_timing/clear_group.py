#coding:utf-8
import time
import unittest
from robot.utils.asserts import *
from public import login
from public import logout
from clear_massage import clear_massage
from set_driver import set_driver

class Imtest(unittest.TestCase):
    
    def setUp(self):
        wq=set_driver()
        self.driver=wq.get_driver()
        self.verificationErrors = []
        self.driver.implicitly_wait(10)

    def dissolve_group(self):
        driver = self.driver 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_group").click()#点击群组
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/p_list").click()#点击群组列表
        k=0
        while k<3:
            k=k+1
            print k
            try:
                wq=str(self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name"))#群组id
                if wq:
                    self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/group_name").click()#点击群组
                    time.sleep(2)
                    try:        
                        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_right").click()#点击群组管理
                        time.sleep(2)
                        driver.swipe(600,800,600,100,500)#上划 (810,960,54,960,500)
                        driver.find_element_by_name(u"解散该群").click()#点击解散群组
                        time.sleep(2)
                        print "点击解散群组"
                        #logout.test_logout(self)#退出登录
                    except:
                        driver.find_element_by_name(u"退出该群组").click()#点击退出群组
                        print "已经退出群组"           
            except:
                print "没有发现群组"
    def test_clear_group(self):  
        '''解散群组''' 
        driver = self.driver
        try:
            logout.test_logout(self)#退出登录
        except:
            print "未登录，无需执行退出登录操作" 
        time.sleep(2)
        login.test_login(self,phoneid="13311267857")
        time.sleep(2)
        self.dissolve_group()
        time.sleep(2)
        driver.press_keycode('4')
        time.sleep(1)
        driver.press_keycode('4')
        logout.test_logout(self)#退出登录
        time.sleep(2)
        login.test_login(self,phoneid="13366778604")
        time.sleep(2)        
        self.dissolve_group()
        time.sleep(2)
        driver.press_keycode('4')
        time.sleep(1)
        driver.press_keycode('4')
        logout.test_logout(self)#退出登录
        time.sleep(2)
        login.test_login(self,phoneid="17600645696")
        time.sleep(2)        
        self.dissolve_group()       
                      
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
         
  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Imtest("test_clear_group"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)      