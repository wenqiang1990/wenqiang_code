# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 09:22:12 2017
@author: JClian
"""
import os
import re
import time
import datetime 
from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.keys import Keys  #导入Keys
from selenium.webdriver.common.action_chains import ActionChains
#导入selenium的异常
from selenium.common.exceptions import TimeoutException,NoSuchElementException,WebDriverException
chrome_driver="D:\chromedriver\chromedriver.exe"
def getSong(songer):
    chrome_options = webdriver.ChromeOptions()
    # 不加载图片(提升加载速度)；设置默认保存文件路径
    prefs = {"profile.managed_default_content_settings.images":2,\
             "download.default_directory": 'D:\\download_music\%s' %songer}
    chrome_options.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome(executable_path = chrome_driver,options=chrome_options) #启动浏览器
    browser.maximize_window() #最大化
    #设置网页加载等待时间为20s,超过20s后则停止加载
    browser.set_page_load_timeout(20) 
    try:
        browser.get('https://www.baidu.com/') #获取百度网页
    except TimeoutException:
        browser.execute_script('window.stop()')
    #在百度搜索栏搜索“歌手 微盘”，并点击“百度一下”按钮
    browser.find_element_by_id("kw").send_keys('%s 微盘'% songer)
    browser.find_element_by_id("su").click()
    time.sleep(5)
    #对每一页的搜索记录进行处理
    def each_page(j):
        for i in range(1+10*j,11+10*j):
            print(datetime.datetime.now(),"第%d页~~~~~~~~~~~~~~~~~~~"%i)
            #找到该条搜索记录，并点击
            elem = browser.find_element_by_xpath("//*[@id='%d']/h3/a"%i)
            elem.click()
            time.sleep(10)
            #切换到新弹出的窗口
            browser.switch_to.window(browser.window_handles[1])
            #判断是否是新浪微盘网页，若是，则再判断里面分享的歌曲是否大于一首
            if re.match('^https?://vdisk.weibo.com*',browser.current_url):
                print("%s 是一个新浪微盘的网页！" %browser.current_url)
                t = browser.find_elements_by_class_name("short_name")
                if len(t) > 0:
                    print("歌曲大于1首，不进行下载！\n")
                else:
                    print("可以进行下载！")
                    #统计此时下载文件夹中的文件数量，作为下载成功的标志
                    music_exit_flg = len(os.listdir("D:\\download_music\%s"%songer))
                    #找到该页面的“下载”按钮，并按下
                    elem = browser.find_element_by_id("download_big_btn").click()
                    print("歌曲正在下载中...")
                    time.sleep(8)
                    #获取歌曲的歌名信息
                    file_name = browser.find_element_by_class_name("page_down_filename").text
                    exit_flg = 0 #歌曲重新下载的标志
                    while True:
                        #如果下载文件夹文件数量增加1，则下载成功，否则重新下载
                        if len(os.listdir("D:\\download_music\%s"%songer)) == (music_exit_flg+1):
                            print("%s 下载成功！\n"%file_name)
                            break
                        else:
                            browser.refresh() #刷新网页
                            time.sleep(5)
                            music_exit_flg = len(os.listdir("D:\\download_music\%s"%songer))
                            elem = browser.find_element_by_id("download_big_btn").click()
                            print("正在尝试重新下载...")
                            time.sleep(8)
                            exit_flg += 1
                            if exit_flg == 3: #尝试重新下载3次仍未下载后，则下载失败
                                print("%s下载失败啦~~\n" %file_name)
                                break
                        
            else:
                print(("这不是新浪微盘的网页！\n"))
            #关闭当前窗口，并切换到原来的搜索页面
            browser.close()
            time.sleep(2)
            browser.switch_to.window(browser.window_handles[0])
    
    pages = 1 #设置爬取网页的数量为20，即200条搜索记录
    for i in range(pages):
        each_page(i)
        #点击该页面中的“下一页”按钮
        if i ==0:
            browser.find_element_by_class_name("n").click()
        else:
            browser.find_elements_by_class_name("n")[1].click()
        time.sleep(8)
        
    browser.close()#关闭窗口
    print(datetime.datetime.now(),"%s的歌曲已操作完毕啦！" % songer)
    
def main():
    d1 = datetime.datetime.now()
    #要搜索的歌手的列表
    songer_lst = ['红楼梦']
    for songer in songer_lst: #运行getSong()函数，并加入异常处理
        try:
            print(datetime.datetime.now(),"开始搜索%s的歌曲啦！"% songer)
            os.mkdir(os.path.join("D:\\download_music",songer)) #创建新文件夹
            getSong(songer)
        except TimeoutException:
            print(datetime.datetime.now(),"%s的歌曲下载超时啦！嘿嘿~~"% songer)
        except NoSuchElementException:
            print(datetime.datetime.now(),"哎呦，出了点小问题... NoSuchElementException")
        except WebDriverException:
            print(datetime.datetime.now(),"哎呦，出了点小问题...WebDriverException")
    d2 = datetime.datetime.now()
    print("开始时间：",d1)
    print("结束时间：",d2)
    print("一共花费的时间：",d2-d1)
    
main()