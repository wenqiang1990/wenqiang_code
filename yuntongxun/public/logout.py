#coding:utf-8
import time
from robot.utils.asserts import *
from appium import webdriver

# 屏幕向上滑动
def swipeUp( self,t):
    l = [1080, 1980]
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    self.driver.swipe(x1, y1, x1, y2, t)
def test_logout(self):
    '''退出当前账号'''
    self.driver.find_element_by_id("btn_plus").click()#加号
    time.sleep(2)
    self.driver.context#可以定位到悬浮窗口
    self.driver.find_element_by_name(u"设置").click()
    #driver.tap([(590,1190)], )#点击设置
    time.sleep(2)
    self.swipeUp(500)#上滑
    time.sleep(2)
    self.driver.find_element_by_name(u"退出当前账号").click()
    self.driver.find_element_by_id("dilaog_button3").click()

