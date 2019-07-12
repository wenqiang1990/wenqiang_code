#coding:utf-8
import copy
import operator
import os
import pymysql
from functools import reduce

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
'''
d = {'胡斌': '8', '王俭': '8', '王利娟': '8', '李强': '7', '魏明阳': '7', '张学正': '7', '张明飞': '6', '张文博': '50', '侯鑫': '5', '林仕鹏': '5', '王正帅': '5', '范红康': '4', '贾政阳': '4', '肖振坤': '4', '詹季春': '4', '刘君平': '35', '高翔': '3', '刘国强': '3', '陆华山': '3', '雷显波': '3', '马亮': '3', '王建': '3', '田傲': '28', '徐元成': '25', '余朝晖': '24', '王灿辉': '22', '姜泊': '2', '刘静波': '2', '潘晓东': '2', '吴超': '2', '王文龙': '2', '王立志': '2', '夏立新': '2', '杨帅': '2', '周逸涵': '18', '杨小洁': '16', '王文旭': '15', '冯胜然': '13', '李德琛': '13', '周瑞杰': '13', '易成雯': '11', '陈威': '1', '丁晓福': '1', '丁洪超': '1', '刘倩': '1', '刘光添': '1', '刘刚': '1', '刘风洁': '1', '劳艳山': '1', '卢波文': '1', '李晓杰': '1', '李眺': '1', '李雪敏': '1', '田可': '1', '吴祖伟': '1', '王帅': '1', '王晓庆': '1', '谢添': '1', '杨海': '1', '朱磊可': '1'} 
n=sorted(d.items(),key = lambda x:x[1],reverse = True)
print(n)
'''
'''
d={'a':1,'b':2,'c':3}
for i in d.keys():
    print(i,d[i])
'''
'''
distance = {'mch_id':100000000000019,'channel_id':2,'channel_name':'广发银企直连-博裕','out_trade_no':'c349a7507a395e174a4fba153900eae9','trade_no':91029154408446299168,'status':-1,'tri_trade_no':2018120616225990,'time_start':'0000-00-00 00:00:00','time_end':'2018-12-06 16:22:59','err_msg':'测试模拟','err_code':'','payer_name':'博裕融资租赁（天津）有限公司 ','payer_card_no':9550880209469900147,'amount':500000,'secret':'88bceeb2d5b91d06da677afe2416dd51'}   
print(sorted(distance.keys()))
'''

'''
#从列表中取得连续最大值
array=[5,-8,-1,6,-5,8,-9]
class Solution:
    def FindGreatestSumSubArray(array):
        # write code here
        maxsofar = 0
        for i in range(0,len(array)):
            presum = 0
            print('i= {}'.format(i))
            for j in range(i,len(array)):
                print('i= {},j= {}'.format(i,j))
                presum += array[j]
                print(presum)
                maxsofar = max(maxsofar, presum)
                print(maxsofar)
        return maxsofar
#bug:不适合最大的<0的情况。
#例如：[5,-8,-1,6,-5,8,-9]
# 对应输出应该为:-1
# 你的输出为:0
    def FindGreatestSumSubArray1(array):
        # write code here
        sum = array[0]
        presum = 0
        for i in array:
            print('i= {}'.format(i))
            if presum < 0:
                presum = i
                print('presum < 0 ,presum = {}'.format(presum))
            else:
                presum += i
                print('presum > 0 ,presum = {}'.format(presum))
            sum = max(presum,sum)
            print('sum = {}'.format(sum))
        return sum

#pind=Solution.FindGreatestSumSubArray(array)
#print(pind)
pind1=Solution.FindGreatestSumSubArray1(array)
print('pind1  {}'.format(pind1))
'''
lis = [12, 34, 456, 12, 34, 66, 223, 12, 5, 66, 12, 23, 66, 12, 66, 5, 456, 12, 66, 34, 5, 34]
'''
def test1():
    # 进行去重
    c = []
    for i in lis:
        if i not in c:
            c.append(i)
    # 进行统计，生成二维列表
    b = []
    print("list C :")
    print(c)
    for i in c:
        num = 0
        for j in range(len(lis)):
            if lis[j] == i:
                num += 1
        a = []
        a.append(i)
        a.append(num)
        print(a)
        b.append(a)
        print("list b :")
        print(b)
    # 排序算法，按出现次数进行降序排列
    for i in range(len(b)):
        for j in range(i, len(b)):
            if b[i][1] < b[j][1]:
                temp = b[i]
                b[i] = b[j]
                b[j] = temp
    print("list b :")
    print(b)
test1()

l=[]
for i in range(3):
	x=int(input('integer:\n'))
	l.append(x)
l.sort()


m=0
n=0
a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
for i in a:
    if i>0:
        m += 1
    elif i<0:
        n += 1
    else:
        pass

print('大于0的个数 {}， 小于0的个数{}'.format(m,n))

a = 1
print("%08d" % a)

a = "hello_world_yoyo"
b = a.split("_")
print(b)

a = [1, 3, 5, 7, 7]

# insert插入数据
a.insert(3, a[0])
print(a)
print(a[1:])
print(a[:2])
print(set(a))
print(list(set(a)))

# 字符串切片s
a = "axbyczdj"
print(a[::2])



a = []
for i in range(1, 1000):
    s = 0
    for j in range(1, i):
        if i % j == 0 and j < i:
            s += j
    if s == i:
        print(i)
        a.append(i)
print("1000以内完全数：%s" % a)


sxh = []
for i in range(100, 1000):
    s = 0
    m = list(str(i))
    for j in m:
        s += int(j)**len(m)
    if i == s:
        print(i)
        sxh.append(i)

print("100-999的水仙花数：%s" % sxh)
'''
wen=[1,2,3,4,5]
qiang=["a","b","c"]
wen.insert(0,9)
wen.append(6)
del wen[2]
wen.extend(qiang)
print(wen)
dict1={"one":"a","two":"b","three":"c"}
print(dict1["one"])

print(dict1.keys(),end='')
print(dict1.values())
print(dict1.items())
print(str(dict1))
print(tuple(dict1))#元组
print(tuple(dict1.values()))#元组
print(list(dict1))
print(dict1.keys())

print("+++++++++字典操作+++++++++++")
print(dict1)
#增加
dict1['wen']=99
print(dict1)
#更新
dict1.update(one=10)
print(dict1)
#删除
dict1.pop("one")
print(dict1)
del dict1["two"]
print(dict1)


print("+++++++++字典操作+++++++++++")


list1=[["x","1"],["m","2"],["n","3"]]
dict2={}
for i in (list1):
    print(i)
    dict2[i[0]]=i[1]
print(dict2)
print(dict(list1))

'''
def digui(n):
    if n == 1:
        return 1
    else:
        return n*digui(n-1)
a = 3
print(digui(a))

a=0
b=1
while b<100:
    #print(b, end=",")
    a,b=b,a+b
    print(b,end=",")
'''
a=3
b=reduce(lambda x,y : x*y ,range(1,a+1))
print(b)


a = [35, 21, 10, 9, 3, 1, 4, 6]
s = range(len(a))[::-1]
print(s)
print(list(s)) # 交换次数
for i in s:
    print(i)
    for j in range(i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
    print("第 %s 轮交换后数据： %s" % (len(s)-i+1, a))
print(a)
