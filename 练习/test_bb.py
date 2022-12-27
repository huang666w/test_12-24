# -*-coding:utf-8-*-
# Time:2022/11/3 21:57
# Author:huangwei
# File:test_bb.py
# Desc:

import unittest

class User(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('打开浏览器')

    @classmethod
    def tearDownClass(cls):
        print('关闭浏览器')


    def test_3(self):
        print('进入第一个测试用例')

    def test_4(self):
        print('进入第二个测试用例')