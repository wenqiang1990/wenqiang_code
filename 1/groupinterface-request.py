# -*- coding: utf-8 -*-
import requests
import json
for i in range(10001,11001):
    data = {
            "pushType":"2",
            "appId":"ff8080814e760cd0014e760e70d00000",
            "sender":"13366778604",
            "receiver":["g801343367"],
            "msgType":"1",
            "msgContent":i, 
            "msgDomain":"yuntongxun",
            "msgFileName":"",
            "msgFileUrl":""
            }

    url1 = "http://192.168.180.83:8060/2013-12-26/Application/ff8080814e760cd0014e760e70d00000/IM/PushMsg?"
    url2 ="sig=d8a62f48707f3b2d6e70a5d056a5a479"
    url = url1+url2
    headers = {'Content-Type' : 'application/json','charset':'UTF-8','Authorization':'ZmY4MDgwODE0ZTc2MGNkMDAxNGU3NjBlNzBkMDAwMDA6MjAxODA0MjMxNTI2MTk='}
#req = urllib2.Request(url = url, headers=headers,data=data)
#response = urllib2.urlopen(req)
#res = response.read()
    response = requests.post(url = url, headers=headers,data=json.dumps(data))
    print i
    print(response.text)
