#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
String = "www shu&di 123"
print(re.search('shu', String))
print(re.findall('\w', String))
print(re.findall('\d', String))
print(re.findall('\D', String))
l=String.split("")
l1=l[1]
l2=l1.split("&")
print(l2[0]+l2[1])
