# coding:utf-8
#https://blog.csdn.net/zhenzhendexiaoer/article/details/77833981
import yaml
import os
from ruamel import yaml


def read_yaml(yamlname,yamlpath=""):
    curpath = os.path.dirname(os.path.realpath(__file__))#当前路径
    yamlpath = os.path.join(curpath, yamlname)
    print(yamlpath)
    f = open(yamlpath, "r", encoding="UTF-8").read()
    cfg = yaml.load(f)
    return cfg

def write_a_yaml(yamlname,redata):
    # 累加写入到yaml文件
    curpath = os.path.dirname(os.path.realpath(__file__))#当前路径
    yamlpath = os.path.join(curpath, yamlname)
    print(curpath)
    with open(yamlpath, "a", encoding="utf-8") as f: #代表以write的形式打开文件,如果要以添加的形式，只需要把w换成a
        yaml.dump(redata, f, Dumper=yaml.RoundTripDumper)

def write_w_yaml(yamlname,redata):
    # 写入到yaml文件
    curpath = os.path.dirname(os.path.realpath(__file__))#当前路径
    yamlpath = os.path.join(curpath, yamlname)
    print(curpath)
    with open(yamlpath, "w", encoding="utf-8") as f: #代表以write的形式打开文件,如果要以添加的形式，只需要把w换成a
        yaml.dump(redata, f, Dumper=yaml.RoundTripDumper)