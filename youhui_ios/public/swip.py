#coding:utf-8

    #屏幕向上滑动
def swipeUp(self,t):#时间t传入单位为毫秒
    l=[1080,1980]
    x1=int(l[0]*0.5)  #x坐标
    y1=int(l[1]*0.75)   #起始y坐标
    y2=int(l[1]*0.25)   #终点y坐标
    self.driver.swipe(x1,y1,x1,y2,t)
    #屏幕向下滑动
def swipeDown(self,t):
    l=[1080,1980]
    x1=int(l[0]*0.5)  #x坐标
    y1=int(l[1]*0.35)  #起始y坐标
    y2=int(l[1]*0.75)   #终点y坐标
    print [x1,y1,x1,y2]
    self.driver.swipe(x1,y1,x1,y2,t)
    #屏幕向左滑动
def swipLeft(self,t):
    l=[1080,1980]
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    print [x1,y1,x2,y1]
    self.driver.swipe(x1,y1,x2,y1,t)
        #屏幕向右滑动
def swipRight(self,t):
    l=self.driver.get_window_size()
    print("l : %s" %l)
    x1=int(l[0]*0.05)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.75)
    self.driver.swipe(x1,y1,x2,y1,t)
        





    