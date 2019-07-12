#coding:utf-8
import os,time
import HTMLTestRunner
import unittest
import Image
import appium 
from robot.utils.asserts import assert_equal, assert_true
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from swip import eleB
from extend import Appium_Extend
class elementA(unittest.TestCase):
    driver = webdriver 
   
    #eleB.sign_in(1331)
    eleB.swipLeft(500)
    driver.find_element_by_id("card_item_tv").click()
    driver.find_element_by_id("content").click()
    driver.find_element_by_id("content").send_keys("1331")
    driver.find_element_by_id("text_right").click()     
    driver.find_element_by_id("chatting_content_et").click()
    driver.find_element_by_id("chatting_content_et").send_keys("hello tester")
    time.sleep(5)
    driver.find_element_by_id("chatting_send_btn").click()

    driver.press_keycode('4')
              
    driver.find_element_by_id("chatting_content_itv").click()
    sendoutcontent = driver.find_element_by_id("chatting_content_itv").get_attribute("text")
    print sendoutcontent
    #receivecontent = driver.find_element_by_id("tv_read_unread").get_attribute("text")
    assert_equal(sendoutcontent,"hello tester",msg=u'发送的消息验证失败')
    #assert_equal(receivecontent,u"未读")
    driver.find_element_by_id("btn_left").click()    
    driver.find_element_by_id("btn_plus").click()#加号
    time.sleep(2)
    #driver.switch_to()
    driver.tap([(590,1190)], )
    #driver.find_element_by_id("popup_menu_item_name ").click()
    origin_el=driver.find_element_by_name("新消息声音")
    destination_el=driver.find_element_by_name("华为推送")
    driver.scroll(destination_el,origin_el)
    driver.find_element_by_name(u"退出当前账号").click()
    driver.find_element_by_id("dilaog_button3").click()
        
    number = driver.find_element_by_id("edittext")
    number.click()
    driver.find_element_by_id("edittext").send_keys("13331")
    driver.find_element_by_id("sign_in_button").click()#登陆
    '''
    time.sleep(5)
        extend = Appium_Extend(driver)
        def test_get_screen_by_element():  
            element = driver.find_element_by_id("btn_middle")  
  
            extend.get_screenshot_by_element(element).write_to_file("f:\\screen", "image")
            
            assert_true(os.path.isfile("f:\\screen\\image.jpg"))  
  
        def test_same_as():  
            element = driver.find_element_by_id("btn_middle")  
  
            load = extend.load_image("f:\\screen1\\image.jpg")  
            #要求百分百相似  
            result = extend.get_screenshot_by_element(element).same_as(load, 0)  
            assert_true(result)

        test_get_screen_by_element()
        test_same_as()   
        
        
        
        
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        

            
        
        
    '''
    time.sleep(8)
    driver.find_element_by_xpath("//LinearLayout/LinearLayout[1]/ScrollView/LinearLayout/LinearLayout[0]/EditText:昵 称").click()    
    driver.find_element_by_xpath("//LinearLayout/LinearLayout[1]/ScrollView/LinearLayout/LinearLayout[0]/EditText:昵 称").send_keys("test1")
    driver.find_element_by_xpath("com.yuntongxun.ecdemo:id/edittext[2]").send_keys("test2")
    driver.find_element_by_id("sign_in_button").click()
    driver.quit()
    '''


    '''
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(elementA("test_1"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)







    
