#!/usr/bin/env python
# -*- coding: utf-8 -*-
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

#person('name1','age1',gender='M', job='Engineer')
  
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
n=my_abs(-1)
print n