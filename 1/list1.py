#coding:utf-8
import ast
x ="[['sh600275','武昌鱼','4.68','10.12','1','0.05','0','11.84'],['sz002105','信隆实业','11.06','10.05','1','18.01','0','7.12'],['sz300402','宝色股份','13.81','10.04','1','1','0','4.37'],['sh603169','兰石重装','5.70','10.04','1','0.58','0','3.45'],['sz002528','英飞拓','15.03','10.03','1','0.2','146.19','3.26']]"
x = ast.literal_eval(x)
#print (x)
#print (x[0])

dict={'getlist': [(1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "ALL"}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "ALL", "pageSize": 200, "pageNo": 0}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "READY", "pageSize": 200, "pageNo": 0}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "LIVEING", "pageSize": 200, "pageNo": 0}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "NOSTREAM", "pageSize": 200, "pageNo": 0}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "STOPED", "pageSize": 200, "pageNo": 0}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "BANNED", "pageSize": 200, "pageNo": 0}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "UNBAN", "pageSize": 200, "pageNo": 0}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "DELETE", "pageSize": 200, "pageNo": 0}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "ALL", "pageSize": 20, "pageNo": 1}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "ALL", "pageSize": 20, "pageNo": 1,"ascDesc":0}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "ALL", "pageSize": 20, "pageNo": 1,"ascDesc":1}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "ALL","uid":00000001}', 'parse the request to json failed, req={"status": "ALL","uid":00000001}, ex=Expecting , delimiter: line 1 column 25 (char 24), code=100'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '', 'parse the request to json failed, req=, ex=No JSON object could be decoded, code=100'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": ""}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"pageSize": 200}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"pageSize":}', 'parse the request to json failed, req={"pageSize":}, ex=No JSON object could be decoded, code=100'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"uid":00000001}', 'parse the request to json failed, req={"uid":00000001}, ex=Expecting , delimiter: line 1 column 9 (char 8), code=100'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"uid":}', 'parse the request to json failed, req={"uid":}, ex=No JSON object could be decoded, code=100'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"pageNo": 0}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"pageNo":-1}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"pageNo":1.1}', "'pageNo' Requires integer type"), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"pageNo":100000000}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"ascDesc":0}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"ascDesc":3}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"ascDesc":-0}', 'success'), (1.0, '获取直播频道列表', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"ascDesc":}', 'parse the request to json failed, req={"ascDesc":}, ex=No JSON object could be decoded, code=100')], 'Info': [(1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "ALL"}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "ALL", "pageSize": 200, "pageNo": 0}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "READY", "pageSize": 200, "pageNo": 0}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "LIVEING", "pageSize": 200, "pageNo": 0}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "NOSTREAM", "pageSize": 200, "pageNo": 0}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "STOPED", "pageSize": 200, "pageNo": 0}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "BANNED", "pageSize": 200, "pageNo": 0}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "UNBAN", "pageSize": 200, "pageNo": 0}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "DELETE", "pageSize": 200, "pageNo": 0}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "ALL", "pageSize": 20, "pageNo": 1}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "ALL", "pageSize": 20, "pageNo": 1,"ascDesc":0}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "ALL", "pageSize": 20, "pageNo": 1,"ascDesc":1}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": "ALL","uid":00000001}', 'parse the request to json failed, req={"status": "ALL","uid":00000001}, ex=Expecting , delimiter: line 1 column 25 (char 24), code=100'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '', 'parse the request to json failed, req=, ex=No JSON object could be decoded, code=100'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"status": ""}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"pageSize": 200}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"pageSize":}', 'parse the request to json failed, req={"pageSize":}, ex=No JSON object could be decoded, code=100'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"uid":00000001}', 'parse the request to json failed, req={"uid":00000001}, ex=Expecting , delimiter: line 1 column 9 (char 8), code=100'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"uid":}', 'parse the request to json failed, req={"uid":}, ex=No JSON object could be decoded, code=100'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"pageNo": 0}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"pageNo":-1}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"pageNo":1.1}', "'pageNo' Requires integer type"), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"pageNo":100000000}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"ascDesc":0}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"ascDesc":3}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"ascDesc":-0}', 'success'), (1.0, '获取直播频道信息', '192.168.180.39', '8088', 'afea8601a3204c4e9106b6c116c74972', 'http://%s/v1/application/%s/livestream/channelList', 'POST', 'form', '{"Content-Type": "application/json;charset=utf-8"}', '{"ascDesc":}', 'parse the request to json failed, req={"ascDesc":}, ex=No JSON object could be decoded, code=100')]}
print(dict["getlist"][0])