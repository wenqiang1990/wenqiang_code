import pymysql
from sshtunnel import SSHTunnelForwarder

with SSHTunnelForwarder(
    ('42.62.69.161', 34185), # B机器的配置
    ssh_pkey="E:/跳板机/Login.KEY",
    ssh_password='XIAO!@#1',
    ssh_username='lcx6',
    remote_bind_address=('192.168.199.12',3327)) as server: # A机器的配置

    db_connect = pymysql.connect(host='127.0.0.1', # 此处必须是是127.0.0.1
                                 port=server.local_bind_port,
                                 user='meitumv',
                                 passwd='123456',
                                 db='PartyNow_Pre')
    cur = db_connect.cursor()
    cur.execute('call storedProcedure')
    db_connect.commit()
