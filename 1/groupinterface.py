# -*- coding: utf-8 -*-
import urllib,urllib2  
for i in range(10001,10002):
    xml1="<Request><appId>ff8080814e760cd0014e760e70d00000</appId><userName>13366778605</userName><subAccountSid></subAccountSid><groupId>g801343370</groupId><members><member>ff8080814e760cd0014e760e70d00000#"
    xml2="</member></members><declared>hello</declared><confirm>1</confirm></Request>"
    xml_request = xml1 + str(i) + xml2
    #xml_request = str(xml_request)
    url = "http://192.168.180.81:8029/2016-03-14/Corp/yuntongxun/InviteJoinGroup"
    headers = {'Content-Type':'application/xml','Accept':'application/xml','charset':'UTF-8'}
    #data = urllib.quote(xml_request)
    print xml_request
    req = urllib2.Request(url=url,headers=headers,data=xml_request)
    response = urllib2.urlopen(req)
    res = response.read()
    print res