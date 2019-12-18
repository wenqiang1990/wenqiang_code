#coding:utf-8
from PIL import Image
import matplotlib.pyplot as plt
from pytesseract import *
#from fnmatch import fnmatch
#import matplotlib.pyplot as plt
#import svm
#import svmutil
import time
import os,sys
from libsvm.python.svmutil import *
from libsvm.python.svm import *


print(sys.platform)
#以下为生成切割图片的方法
image=(str(time.strftime("%Y%m%d%H%M%S", time.localtime())))
#imageopen=str('f:\\screen\\' + image + '.png')
threshold = 80    #数值越小，越会忽略颜色较淡的地方
table = []    
for i in range(256):    
    if i < threshold:    
        table.append(0)    
    else:    
        table.append(1) 
def getverify1():#批量处理图片二值化分割,将分割后的图片保存到W文件夹下
    for name in range(100):
        name1='f:\\screen\\'+str(name)+'.png'     
        #打开图片    
        im = Image.open(name1)    
        #转化到灰度图  
        imgry = im.convert('L')  
        #保存图像  
        #imgry.save('f:\\screen\\1234567.png')    
        #二值化，采用阈值分割法，threshold为分割点   
        out = imgry.point(table,'1')    
        out.save('f:\\screen\\'+str(name)+'A.png')    
        #getverify1('f:\\screen\\20181116110510.png')  #注意这里的图片要和此文件在同一个目录，要不就传绝对路径也行      
        child_img_list = []
        for i in range(4):
            x = 25 + i * (50 + 5)  # 见原理图
            y = 20
            child_img = out.crop((x, y, x + 50, y + 95))
            child_img_list.append(child_img)
            #plt.imshow(child_img)
            #plt.show(child_img)
            child_img.save('f:\\screen\\w\\'+str(name)+str(i)+'.png')  
#getverify1()


def rename(dir_path):#手动将文件分到对应的文件夹下后，对单一文件夹下文件批量重命名
    filelist = os.listdir(dir_path)
    i = 0
    for item in filelist:
        #set the old file name 
        oldname = dir_path + r"\\" + filelist[i]
        #set the new file name 
        newname = dir_path + r"\\" +image+"A"+str(i) + "." + "png"
        i=i+1
        #newname = dir_path + r"\\" + str(i) + "." + "png"
        #write the resolution information to the file
        #rename the file
        os.rename(oldname, newname)
    m = 0
    time.sleep(1)
    
    filelist = os.listdir(dir_path)
    for item in filelist:
        #set the old file name 
        oldname = dir_path + r"\\" + filelist[m]
        #set the new file name 
        #newname = dir_path + r"\\" + "A"+str(i) + "." + "png"
        m=m+1
        print(m)
        newname = dir_path + r"\\" + str(m) + "." + "png"
        #write the resolution information to the file
        #rename the file
        os.rename(oldname, newname)
        
if __name__ == "__main__":
    dir_path = r"F:\\screen\\w\\p"
    rename(dir_path)
  



