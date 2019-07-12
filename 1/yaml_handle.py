# coding:utf-8
#https://blog.csdn.net/zhenzhendexiaoer/article/details/77833981
import yaml
import os
from ruamel import yaml

#yaml 参数化  。。。
def read_yaml(yamlname,yamlpath=""):
    curpath = os.path.dirname(os.path.realpath(__file__))#当前路径
    yamlpath = os.path.join(curpath, yamlname)
    print(yamlpath)
    f = open(yamlpath, "r", encoding="UTF-8").read()
    cfg = yaml.load(f)
    print(cfg)
    return cfg

def write_yaml(yamlname,redata):
    # 写入到yaml文件
    curpath = os.path.dirname(os.path.realpath(__file__))#当前路径
    #yamlpath = os.path.join(curpath, yamlname)
    print(curpath)
    with open(yamlname, "w", encoding="utf-8") as f: #代表以write的形式打开文件,如果要以添加的形式，只需要把w换成a
        yaml.dump(redata, f, Dumper=yaml.RoundTripDumper)


old=read_yaml("wyaml.yaml")
a=old["sessionId"] % "123456789"
print(a)
print(old)
old["sessionId"]=a
print(old)
