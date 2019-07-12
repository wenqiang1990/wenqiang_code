#coding:utf-8
import requests
import unittest
#from test_toloan_xiao import *

#http://develop.rmbfapi.test.youxinjinrong.com/in_loan/to_loan?debug=1&cuser_id=1590207739&product_id=1&loan_period=2&loan_money=5000&bank_card_id=489

class to_loan111(unittest.TestCase):
    '''下单接口'''
    def __init__(self,url,**kwargs):
        unittest.TestCase.__init__(self,url,**kwargs)
        self.url = 'http://develop.rmbfapi.test.youxinjinrong.com/in_loan/to_loan'

        #self.cuser_id = 915884
        #self.bank_card_id= bank_card_id()
        
    def test_case0_SysError(self):
        r = requests.get(self.url1, params={'cuser_id': 1590207739, 'loan_period': 3, 'loan_money': 5000, 'product_id': 1, 'bank_card_id': 489,
              'debug': 1})
        data = json.loads(r.text)['data']
        if data is  None:
            print('系统有误！'+json.loads(r.text)['msg'])
'''
    def test_error(self):
        r.requests.get(self.url,params={'cuser_id': 1590207739, 'loan_period': 3, 'loan_money': 5000, 'product_id': 1, 'bank_card_id': 489,
              'debug': 1})
        result = r.json()
        self.assertEqual(result['code'], -1)
        self.assertEqual(result['msg'], "当前用户无授信额度！")
    def test_success(self,cuser_id,bank_card_id):
        r.requests.get(self.url,params={'cuser_id': cuser_id, 'loan_period': 3, 'loan_money': 5000, 'product_id': 1, 'bank_card_id': bank_card_id,
              'debug': 1})
        result = r.json()
        self.assertEqual(result['code'], 1)
        self.assertEqual(result['msg'], 'seccess')'''
    
'''code    -1
msg    "系统有误，请稍后重试！"    
msg '对不起，暂无法为您提供服务!'        
msg    "操作太频繁，请稍候重试"  '''
        
if __name__ == '__main__':
    unittest.main()        
        
'''  
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(test("setup"))
    suite.addTest(test("test_data_error"))
    suite.addTest(test("test_success"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)     
'''   
    