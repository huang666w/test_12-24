# -*-coding:utf-8-*-
# Time:2022/11/5 21:04
# Author:huangwei
# File:login_page.py
# Desc:
from selenium.webdriver.common.by import By


#页面对象------元素
class LoginPage:
    def __init__(self,driver):
        self.driver = driver                           #实例化一个driver
        self.user_name = By.ID, 'account'              #实例元素
        self.password = By.NAME, 'password'
        self.click_a = By.ID, 'submit'
        self.exit_1 = By.CLASS_NAME, 'user-name'
        self.exit_2 = By.LINK_TEXT, '退出'

# 封装操作方法

    def input_username(self,username):
        self.driver.find_element(*self.user_name).clear()   #清空
        self.driver.find_element(*self.user_name).send_keys(username)

    def input_password(self,password):
        self.driver.find_element(*self.password).clear()      #清空
        self.driver.find_element(*self.password).send_keys(password)

    def click_elem(self):
        self.driver.find_element(*self.click_a).click()

    def tuichu_a(self):
        self.driver.find_element(*self.exit_1).click()
        self.driver.find_element(*self.exit_2).click()