# -*- coding: utf-8 -*-
import datetime 
import hashlib
import base64

def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

main = '5c6260c525d811e8ba14005056ae87a2'
maintoken = '23961149d1793dc1ae2b0cafdbbe0845'
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# sig md5加密
sig_str1 = main + maintoken + timestamp
sig_str2 = md5(sig_str1.encode("utf8"))
print(sig_str2)
print('**************************')
# auth base64加密
auth_str1 = main + ':' + timestamp
auth_str2 = base64.b64encode(auth_str1.encode("utf8"))
print(auth_str2)