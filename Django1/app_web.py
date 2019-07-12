#coding:utf-8
import os
import web

urls = (
    '/hello(.*)','hellow',
    '/(.*)','index',
        )
app= web.application(urls,globals())
class index:
    #get请求方法,name为请求的路径
    def GET(self,name):
        #打印参数
        print(web.input())
        print(name)
        if not name:
            name= 'world'
        web.header('Content-Type','text/html;charset=UTF-8')
        return 'www.wenqiang.com'+name
    #post请求
    def POST(self,*args,**kwargs):
        data = web.data().decode('gbk')
        print(data)
class hellow:
    def GET(self,name):
        #打印参数
        print(web.input())
        if not name:
            name= 'world'
        web.header('Content-Type','text/html;charset=UTF-8')
        return 'hellow world'+name

if __name__=="__main__":
    app.run()
