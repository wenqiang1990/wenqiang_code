#coding:utf-8
import time
#from robot.utils.asserts import *

# 屏幕向上滑动
def swipeUp( self,t):
    l = [1080, 1980]
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    self.driver.swipe(x1, y1, x1, y2, t)
def test_logout(self):
    '''退出当前账号'''
    self.driver.find_element_by_name(u"个人中心").click()#点击
    time.sleep(2)
    self.driver.context#可以定位到悬浮窗口
    self.driver.find_element_by_name(u"系统设置").click()#点击
    self.driver.find_element_by_accessibility_id(u"退出登录").click()
    self.driver.find_element_by_accessibility_id(u"确定").click()
    print ("退出登录")

