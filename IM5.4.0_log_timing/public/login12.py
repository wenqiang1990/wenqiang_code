#coding:utf-8

def test_login(self,phoneid="13311267857"):#13366778606
    '''登陆''' 
    self.driver.find_element_by_id("edittext").set_text(phoneid)#timecode
    self.driver.find_element_by_id("sign_in_button").click()#点击登陆                     
    print u"成功点击登陆" 
         


#test_login(13366778604)

