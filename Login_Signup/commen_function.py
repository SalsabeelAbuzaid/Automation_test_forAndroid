import test_sign_up
import test_Login
import re
import unittest
from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import sys

from Config import config


class TestCommenFuntion(unittest.TestCase):
    def setUp(self):
        self.driver = config.create_appium_driver()
        self.driver.implicitly_wait(30)

    # def Login_function(self):
    #     test_Login.TestLogin.test_EnterEmail()

    def Signp_function(self):
        test_sign_up.TestSignUp.test_sign_up_Email()

#
