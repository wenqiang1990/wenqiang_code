#coding:utf-8
import requests
import json
  
def get_token():
  
  url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
  values = {'corpid' : 'your corpid' ,
      'corpsecret':'your corpsecret',
       }
  req = requests.post(url, params=values)  
  data = json.loads(req.text)
  return data["access_token"]
  
def send_msg():
  url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+get_token()
  values = """{"touser" : "1" ,
      "toparty":"1",
      "msgtype":"text",
      "agentid":"1",
      "text":{
        "content": "%s"
      },
      "safe":"0"
      }""" %(str("10.1.1.8 is down"))
   
  data = json.loads(values) 
  req = requests.post(url, values)  
  
if __name__ == '__main__':
  send_msg()