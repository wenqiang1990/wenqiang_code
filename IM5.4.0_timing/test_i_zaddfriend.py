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
        '''添加好友''' 
        driver = self.driver
        time.sleep(2)
        member = "13366778604"  #登陆账号账号
        time.sleep(2) 
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.widget.ImageButton[1]").click()#点击新的好友
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/search").send_keys('13366778604')#点击添加
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_phone_tag2").click()#点击添加
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_add").click()#点击添加到通讯录
        time.sleep(2)
        driver.press_keycode('4')
        logout.test_logout(self)#退出登录
        login.test_login(self,phoneid="13366778604")
        time.sleep(2)
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/btn_address_list").click()#点击联系人
        el=driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_friend_num").get_attribute("text")
        assert_equal(el,"1",msg=u'邀请人数不对')
        driver.find_element_by_id("com.yuntongxun.eckuailiao:id/tv_head_newfriend").click()#点击新的好友
        driver.find_element_by_name(u"同意").click()#点击同意
        print "add friend success "           
          
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