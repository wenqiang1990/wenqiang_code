#coding:utf-8
import time
def test_login(self,phoneid="13311267857"):#13366778606
    '''登陆''' 
    k=0
    while k<2:
        k=k+1
        try:
            wq=str(self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/bu_login"))#登录标签
            if wq:
                try:        
                    self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_name").clear()
                    self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_name").send_keys(phoneid)#timecode
                    self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_pwd").send_keys("111111")
                    #self.driver.press_keycode('4')#点击返回键
                    time.sleep(2)
                    self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_login").click()#点击登陆  
                    time.sleep(2)                 
                    print "点击登陆并等待了2秒" 
                except:
                    print "已经登录"                  
        except:
            print "账号"+phoneid+"登录" 














         
#test_login(13366778604)

