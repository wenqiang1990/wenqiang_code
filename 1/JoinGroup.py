# -*- coding: utf-8 -*-
import json,urllib2
textmod={"jsonrpc": "2.0","method":"user.login","params":{"user":"admin","password":"zabbix"},"auth": None,"id":1}
textmod = json.dumps(textmod)
print(textmod)
#输出内容:{"params": {"password": "zabbix", "user": "admin"}, "jsonrpc": "2.0", "method": "user.login", "auth": null, "id": 1}
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
url='http://192.168.199.10/api_jsonrpc.php'
req = urllib2.Request(url=url,data=textmod,headers=header_dict)
res = urllib2.urlopen(req)
res = res.read()
print(res)
#输出内容:{"jsonrpc":"2.0","result":"2c42e987811c90e0491f45904a67065d","id":1}