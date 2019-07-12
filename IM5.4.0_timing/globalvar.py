#coding:utf-8
class GlobalVar: 
    db_handle = None
    mq_client = None
    db_handle1 = None
    
def set_db_handle(db): 
    GlobalVar.db_handle = db 
def get_db_handle(): 
    return GlobalVar.db_handle

def set_mq_client(mq_cli): 
    GlobalVar.mq_client = mq_cli 
def get_mq_client(): 
    return GlobalVar.mq_client

def set_db_handle1(db): 
    GlobalVar.db_handle1 = db 
def get_db_handle1(): 
    return GlobalVar.db_handle1

def set_db_handle2(db): 
    GlobalVar.db_handle2 = db 
def get_db_handle2(): 
    return GlobalVar.db_handle2
