#coding:utf-8
import requests
import unittest
import http.cookiejar,urllib.request

#将cookie保存到本地 保存格式分为 LWPCookieJar和 MozillaCookieJar
filename = 'cookies.txt'
cookie = http.cookiejar.LWPCookieJar(filename)#LWPCookieJar,MozillaCookieJar
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

#读取cookie并与请求一起发送
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookies.txt',ignorediscard=True,ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response= opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))