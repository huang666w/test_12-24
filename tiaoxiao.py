# -*-coding:utf-8-*-
# Time:2022/11/3 21:59
# Author:huangwei
# File:tiaoxiao.py
# Desc:


import unittest
from BeautifulReport import BeautifulReport

# 加载批量的测试用例

suite=unittest.defaultTestLoader.discover(start_dir='./练习',pattern='test_aa.py')
# runner=unittest.TextTestRunner()
#
# runner.run(suite)
result = BeautifulReport(suite)  #生成html的测试报告
result.report(description='系统登录测试报告',filename='测试报告',report_dir='./report')