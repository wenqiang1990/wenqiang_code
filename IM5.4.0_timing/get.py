#!/usr/bin/env python2.7 
import globalvar as GlobalVar 
def get(): 
    return str(GlobalVar.get_mq_client())
def get1(): 
    return str(GlobalVar.get_db_handle())
def get2(): 
    return str(GlobalVar.get_db_handle1())
def get3(): 
    return str(GlobalVar.get_db_handle2())