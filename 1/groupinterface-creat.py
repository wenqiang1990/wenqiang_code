# -*- coding: utf-8 -*-
import urllib2
for i in range(1000,1001):
    xml="<Request><appId>ff8080814e760cd0014e760e70d00000</appId><userName>13366778604</userName><groupName>1000人</groupName><scope>5</scope><declared>1</declared><permission>1</permission><mode>2</mode></Request>"
    print xml
    url1 = "http://192.168.180.81:8029/2013-12-26/Accounts/ff8080815aa6948f015aa6c9784d0000/Corp/yuntongxun/CreateGroup"
    url = url1
    headers = {'Content-Type' : 'application/xml','charset':'UTF-8'}
    req = urllib2.Request(url = url, headers=headers,data=xml)
    response = urllib2.urlopen(req)
    res = response.read()
    print i
    print res