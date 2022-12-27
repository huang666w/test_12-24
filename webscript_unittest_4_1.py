# -*-coding:utf-8-*-
# Time:2022/10/31 21:18
# Author:huangwei
# File:webscript_unittest_4_1.py
# Desc:  unittest框架

"""
规则
以test开头函数（测试用例）
继承unittest.TestCasel类
unittest.main()
测试夹具fixture:setupclass (执行)   teardownclass (销毁)    作用域是整个类，只执行一次

setup(执行)   teardown(销毁)   作用域是函数，每一个函数都要执行一次

"""
import unittest

class Lgoin(unittest.TestCase):

    @classmethod                           #类方法
    def setUpClass(cls):
        print('打开浏览器')

    @classmethod                           #类方法
    def tearDownClass(cls):
        print('关闭浏览器')

    # 函数方法
    # def setUp(self):
    #     print('打开浏览器')
    #
    # def tearDown(self):
    #     print('关闭浏览器')

#test开头都是测试用例

    def test_uer1(self):
        print('admin用户系统登录')
        print('admin用户退出系统')

    def test_uer2(self):
        print('uesr用户系统登录')
        print('uesr用户退出系统')

    def test_1(self):
        print('第一个测试用例')

if __name__=='__main__':
    # unittest.main()
    suite=unittest.TestSuite()  #实列化对象
    testcases=[Lgoin('test_uer1'),Lgoin('test_uer2')]  #加载多条
    suite.addTests(testcases)
    # suite.addTest(Lgoin('test_uer2'))   #加载一条
    unittest.main(defaultTest='suite')
    # runner=unittest.TextTestRunner()  #实列化一个执行器
    # runner.run(suite)