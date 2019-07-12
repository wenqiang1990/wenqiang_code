#coding:utf-8
import globalvar as GlobalVar 
def set_value():
    GlobalVar.set_mq_client(value='')
    #GlobalVar.set_db_handle("aaaaaaaaaaa")
    print str(GlobalVar.get_mq_client()) 
    #print str(GlobalVar.get_db_handle())