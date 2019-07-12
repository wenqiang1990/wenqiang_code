#coding:utf-8

def test_login(self,phoneid="13311267857"):#13366778606
    '''登陆''' 
    self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_name").set_text(phoneid)#timecode
    self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/ed_pwd").set_text("111111")
    self.driver.find_element_by_id("com.yuntongxun.eckuailiao:id/phone_login").click()#点击登陆                     
    print u"成功点击登陆" 
         
#test_login(13366778604)

