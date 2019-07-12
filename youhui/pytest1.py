# coding:utf-8
import pytest
import time, os
import unittest

##pytest test_mod.py# run tests in module  
#pytest somepath# run all tests below somepath  
#pytest -k stringexpr# only run tests with names that match the  
# the "string expression", e.g. "MyClass and not method"  
# will select TestMyClass.test_something  
# but not TestMyClass.test_method_simple  
#pytest test_mod.py::test_func# only run tests that match the "node ID",  
# e.g "test_mod.py::test_func" will select  
# only test_func in test_mod.py  

#pytest -s -q --alluredir report_xml  report_xml 是报告生成路径
#allure generate report_xml --clean    report_xml 是报告存放路径  新报告生成路径为默认allure-report
#allure open -h 127.0.0.1 -p 8083 ./report/
#http://127.0.0.1:8083/index.html
