#coding:utf8 
import json
import os
'''
l="哈哈IM"
#print "Start : %s" % l
with open('C:\\Users\\dodo\\Desktop\\test.txt','a') as f:  #如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
    f.write(l+'\r\n')
 
with open('C:\\Users\\dodo\\Desktop\\test.txt', 'r') as f:
    #print(f.readlines())#调用readlines()一次读取所有内容并按行返回list  
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉    


obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)#对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
print s
'''

'''
import requests
r = requests.get('https://www.douban.com/') # 豆瓣首页
r.status_code
print r.text
'''

'''
import psutil
print psutil.cpu_count() # CPU逻辑数量
print psutil.cpu_count(logical=False) # CPU物理核心
for x in range(10):#再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
    print psutil.cpu_percent(interval=1, percpu=True)

print psutil.virtual_memory()

'''
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
print(os.getcwd())
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.abspath(os.path.dirname(os.getcwd())))