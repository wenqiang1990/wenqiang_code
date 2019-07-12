#coding:utf-8
from PIL import Image
import matplotlib.pyplot as plt
from pytesseract import *
#from fnmatch import fnmatch
#import matplotlib.pyplot as plt
#import svm
import time
import os
from libsvm.python.svmutil import *
from libsvm.python.svm import *
from libsvm.tools import grid
from libsvm.tools import *
#import matplotlib.pyplot as plt
#from sphinx.ext import imgconverter
'''
filedir='f:\\screen\\'
img_name='11.png'
image = Image.open('f:\\screen\\11.png')
code = pytesseract.image_to_string(image, lang ='eng', config='-pms 10')
print(code)
print(111)
#get_dynamic_binary_image(filedir, img_name)
'''
threshold = 80    #数值越小，越会忽略颜色较淡的地方
table = []    
for i in range(256):    
    if i < threshold:    
        table.append(0)    
    else:    
        table.append(1)

'''          
def  getverify1(name):          
    #打开图片    
    im = Image.open(name)    
    #转化到灰度图  
    imgry = im.convert('L')  
    #保存图像  
    imgry.save('f:\\screen\\1234567.png')    
    #二值化，采用阈值分割法，threshold为分割点   
    out = imgry.point(table,'1')    
    out.save('f:\\screen\\12345678.png')    
    #识别    
    #text = image_to_string(out)    
    #识别对吗    
    #text = text.strip()
    #print (text)   
    #text = text.upper();
    #print (text)          
    #out.save(text+'.jpg')    
    #print (text)    
    #return text    
getverify1('f:\\screen\\20181116110510.png')  #注意这里的图片要和此文件在同一个目录，要不就传绝对路径也行  

img = Image.open('f:\\screen\\12345678.png')
img1 = Image.open('f:\\screen\\image1111111.png')
def get_crop_imgs(img):
    """
    按照图片的特点,进行切割,这个要根据具体的验证码来进行工作. # 见原理图
    :param img:
    :return:
    """
    child_img_list = []
    for i in range(4):
        x = 25 + i * (50 + 5)  # 见原理图
        y = 20
        child_img = img.crop((x, y, x + 50, y + 95))
        child_img_list.append(child_img)
        plt.imshow(child_img)
        plt.show(child_img)
        child_img.save('f:\\screen\\image1111111.png')
    return child_img_list
    #print(child_img_list)
    #plt.imshow(child_img_list)
    #plt.show(child_img_list)
#get_crop_imgs(img)

def get_feature(img1):
    """
    获取指定图片的特征值,
    1. 按照每排的像素点,高度为10,则有10个维度,然后为6列,总共16个维度
    :param img_path:
    :return:一个维度为95（高度）的列表
    """
    width, height = img1.size
    pixel_cnt_list = []
    height = 95
    for y in range(height):
        pix_cnt_x = 0
        for x in range(width):
            if img1.getpixel((x, y)) == 0:  # 黑色点
                pix_cnt_x += 1
                #print(pix_cnt_x)
        pixel_cnt_list.append(pix_cnt_x)
        #print(pixel_cnt_list)

    for x in range(width):
        pix_cnt_y = 0
        for y in range(height):
            if img1.getpixel((x, y)) == 0:  # 黑色点
                pix_cnt_y += 1
                #print(pix_cnt_x)
        pixel_cnt_list.append(pix_cnt_y)
        #print(pixel_cnt_list)
    return pixel_cnt_list
#get_feature(img1)
'''
Directory=['1','2','3','4','5','6','7','8','a','b','c','d','e','f','m','n','p','w','x','y']
def modetxt():   # 生成特征文件及识别模型文件
    for i in Directory:  # 0到9的目录
        for u in range(1, 91):  # 目录里名字1到50张图
            b = ''
            b = "F:\\screen\w\\" + str(i) + "\\" + str(u) + '.png'
            img = Image.open(b)
            width, height = img.size
            pixel_cnt_list = []
            for y in range(height):
                pix_cnt_x = 0
                for x in range(width):
                    if img.getpixel((x, y)) == 0:  # 黑色像素点
                        pix_cnt_x += 1
                pixel_cnt_list.append(pix_cnt_x)
            for x in range(width):
                pix_cnt_y = 0
                for y in range(height):
                    if img.getpixel((x, y)) == 0:  # 黑色像素点
                        pix_cnt_y += 1
                pixel_cnt_list.append(pix_cnt_y)
            f = open('F:\\screen\w\\mode.txt', 'a')
            list1 = []
            for q in range(0, len(pixel_cnt_list)):
                a = ''
                a = str(q + 1) + ':' + str(pixel_cnt_list[q])
                list1.append(a)
            f.write(str(ord(i)) + ' ' + " ".join(list1) + '\n')#将字母转换为数字写入mode文件 便于findparam
            f.close
#modetxt()

def train_svm_model():
    """训练并生成model文件:return:"""
    os.system('C:\\Users\\dodo\\Anaconda3\\Lib\\site-packages\\libsvm\\windows\\svm-scale.exe -l -1 -u 1 F:\\screen\\w\\mode.txt>F:\\screen\\w\\mode_scale.txt')
    #将特征文件中的值进行尺寸变换
    y, x = svm_read_problem('F:\\screen\w\\mode.txt')
    model = svm_train(y, x,'-c 16.0 -g 0.000006103515625')
    #c 和 g 的最佳参数可以通过调用findparam（）获得
    svm_save_model('F:\\screen\\w\\svm_mode_file', model)
    #生成最终模型文件
#train_svm_model()


def findparam():#寻找最佳参数   C G 参数设置越大越耗费时间，准确度越高
    rate,param = grid.find_parameters('F:\\screen\\w\\mode.txt', '-log2c -16,16,1 -log2g -16,16,1 -svmtrain C:\\Users\\dodo\\Anaconda3\\Lib\\site-packages\\libsvm\\windows\\svm-train.exe')
    print('rate: ',rate)
    print('param: ',param)
#findparam()



def getverify2(name):#处理待识别的验证码图片
    name1='f:\\screen\\'+str(name)+'.png'     
    #打开图片    
    im = Image.open(name1)    
    #转化到灰度图  
    imgry = im.convert('L')  
    #保存图像  
    #imgry.save('f:\\screen\\1234567.png')    
    #二值化，采用阈值分割法，threshold为分割点   
    out = imgry.point(table,'1')    
    #out.save('f:\\screen\\'+str(name)+'A.png')    
    #getverify1('f:\\screen\\20181116110510.png')  #注意这里的图片要和此文件在同一个目录，要不就传绝对路径也行  
    os.makedirs('f:\\screen\\q\\'+name+'\\')#创建多级目录    
    child_img_list = []
    for i in range(4):
        x = 25 + i * (50 + 5)  # 见原理图
        y = 20
        child_img = out.crop((x, y, x + 50, y + 95))
        child_img_list.append(child_img)
        #plt.imshow(child_img)
        #plt.show(child_img)
        child_img.save('f:\\screen\\q\\'+name+'\\'+str(name)+str(i)+'.png')  
#getverify2('2')            

def testtxt(num):   # 生成待识别验证码特征文件
    dy='F:\\screen\\q\\'+num+'\\'+'ptest.txt'
    dy1='F:\\screen\\q\\'+num+'\\'+'ptest_scale.txt'
    file_path='F:\\screen\\q\\'+num+'\\'
    f=open(dy,'w')
    f.truncate()#清空txt文件
    f.close
    for i in range(0, 4):  # 目录里的4张图
        img = Image.open(file_path + '\\%d%d.png' % (int(num),i))
        width, height = img.size
        pixel_cnt_list = []
        for y in range(height):
            pix_cnt_x = 0
            for x in range(width):
                if img.getpixel((x, y)) == 0:  # 黑色像素点
                    pix_cnt_x += 1
            pixel_cnt_list.append(pix_cnt_x)
        for x in range(width):
            pix_cnt_y = 0
            for y in range(height):
                if img.getpixel((x, y)) == 0:  # 黑色像素点
                    pix_cnt_y += 1
            pixel_cnt_list.append(pix_cnt_y)
        f = open(dy, 'a')
        list1 = []
        for q in range(0, len(pixel_cnt_list)):
            a = ''
            a = str(q + 1) + ':' + str(pixel_cnt_list[q])
            list1.append(a)
        f.write('0' + ' ' + " ".join(list1) + '\n')
        f.close
    os.system('C:\\Users\\dodo\\Anaconda3\\Lib\\site-packages\\libsvm\\windows\\svm-scale.exe -l -1 -u 1 %s > %s' % (dy,dy1))
#testtxt(2,'F:\\screen\\q\\2')

            
def verify(time1):   #识别验证码调用此函数，将新下载验证处理并保存，与已经存在的特征码进行对比
    getverify2(time1)
    testtxt(time1)
    yt ,xt = svm_read_problem('F:\\screen\\q\\'+time1+'\\ptest.txt')
    m = svm_load_model('F:\\screen\w\\svm_mode_file')
    p_label,p_acc,p_vals = svm_predict(yt,xt,m)
    wq='F:\\screen\\q\\'+time1+'\\presult.txt'
    f = open(wq, 'w')
    f.truncate()  #清空txt文件
    f.close
    for item in p_label:
        #print(item)
        #print(chr(int(item)))
        f = open(wq, 'a')    #存放识别结果
        f.write(chr(int(item)))
        f.close
#verify('7')