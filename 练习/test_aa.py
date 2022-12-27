# -*-coding:utf-8-*-
# Time:2022/11/3 21:55
# Author:huangwei
# File:test_aa.py
# Desc:  测试用例
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from objectpage.login_page import LoginPage
from config.config import url

class Lgoin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('打开浏览器')
        cls.driver = webdriver.Chrome()  # 实列化对象（浏览器）
        cls.driver.maximize_window()  # 窗口最大化
        cls.driver.get(url)
        cls.loginpage=LoginPage(cls.driver)  #实例对象driver

    @classmethod
    def tearDownClass(cls):
        print('关闭浏览器')
        cls.driver.quit()


    def test_1(self):
        """
        验证有效用户名和密码时成功登录
        """
        self.loginpage.input_username('admin')

        self.loginpage.input_password('hw123456.')

        self.loginpage.click_elem()

        sleep(1)
        self.loginpage.tuichu_a()


    def test_2(self):
        """
        验证没有密码登录时失败
        """
        self.loginpage.input_username('admin')
        self.loginpage.input_password('')
        self.loginpage.click_elem()


