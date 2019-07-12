#coding:utf-8
import copy

'''
el='123"'
x = el.split('"')#split分割函数，返回列表
print x
print x[0]
print x[1]
'''
'''
l=['1','2','3','4','5','6']
a=copy.copy(l)
l.append('7')
print(l)
print(a)
'''  

d = {'a':1,'b':4,'c':2}  
sorted(d.items(),key = lambda x:x[1],reverse = True)
print(sorted)


str = "-";
seq = ("a", "b", "c"); # 字符串序列
print str.join( seq );