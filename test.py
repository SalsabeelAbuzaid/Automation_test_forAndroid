import re
import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


# from test_daily_book import TestDailybook
# from test_wajeezcast import TestWajeezcast

# import os


# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class TestLogin(unittest.TestCase):
    desired_cap = {
        "platformName": "Android",
        "appium:deviceName": "Pixel 6 Pro API 29",
        "appium:automationName": "UiAutomator2",
        "appium:platformVersion": "10.0",
        "appium:app": "C:\Users\salsa\Downloads\app-debug (14).apk",
        "appium:appPackage": "com.faylasof.android.waamda",
        "appium:noReset": True,
        "appium:locale": "ar",
        "appium:language": "ar",
        "appium:unicodeKeyboard": True,
        "appium:resetKeyboard": True
    }

    def setUp(self):
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', self.desired_cap)
        self.driver.implicitly_wait(30)
        self.driver.setSetting("driver", "compose")

    def test_Login(self):

        self.element_loginByEmail = self.driver.find_element(by=AppiumBy.ID, value="email_login_button")
        self.element_loginByEmail.click()
        self.driver.implicitly_wait(10)

        # self.enter_email = self.driver.find_element(by=AppiumBy.XPATH,
        #                                             value="")
        # self.enter_email.click()
        self.element_loginByEmail.clear()
        self.email = "fe@fe.fe"
        # "ad@ad.ad"
        # "yousals123@gmail.com"
        self.element_loginByEmail.send_keys(self.email)
        pat = re.compile(r"^\S+@\S+\.\S+$")
        self.result = re.match(pat, self.email)
        if self.result:
            print("valid email")
        else:
            print("not valid")
        assert self.result, "invalid email"
        print(self.email)
        sleep(2)
        self.emailScreen = self.driver.find_element(by=AppiumBy.ID,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View")
        self.assertTrue(self.emailScreen.is_displayed(), "Button is not displayed on the page")
