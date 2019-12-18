#coding:utf-8
from appium.webdriver.common.touch_action import TouchAction

def clear_massage(self,name=u"容联幼稚园"):#13366778606
    '''进入消息页面，判定特定账号下是否存在历史消息，存在则清除历史消息''' 
    action1 = TouchAction(self.driver)
    try:
        wq=str(self.driver.find_element_by_name(name))#名字
        #itv=str(self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/chatting_content_itv"))#文字表情图片等
        #filesize=str(self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/tv_filesize"))#视频大小等
        while wq:
            el=self.driver.find_element_by_name(name)#定位名字
            action1.long_press(el,duration=5000).perform()
            self.driver.find_element_by_name(u"删除该聊天").click()
            #self.driver.find_element_by_id("dilaog_button3").click()          
    except:
        print ("已经删除对话名称为“%s”的历史消息" %name)
        
def clear_allmassage(self,accountnumber='com.yuntongxun.rongxin.lite:id/nickname_tv'):#13366778606
    '''进入消息页面，判定特定账号下是否存在历史消息，存在则清除历史消息''' 
    action1 = TouchAction(self.driver)
    try:
        wq=str(self.driver.find_element_by_id(accountnumber))#名字
        #itv=str(self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/chatting_content_itv"))#文字表情图片等
        #filesize=str(self.driver.find_element_by_id("com.yuntongxun.ecdemo:id/tv_filesize"))#视频大小等
        while wq:
            el=self.driver.find_element_by_id(accountnumber)#定位名字
            action1.long_press(el,duration=5000).perform()
            self.driver.find_element_by_name(u"删除该聊天").click()
            #self.driver.find_element_by_id("dilaog_button3").click()          
    except:
        print ("已经删除对话历史消息")   
        