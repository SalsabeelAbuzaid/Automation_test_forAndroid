from encodings import undefined

from appium import webdriver
import random

from appium.common.exceptions import NoSuchContextException
from appium.webdriver import WebElement
# import keyboard
# import os
# from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
import re

from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from time import sleep
# from appium.common import exceptions
import unittest
from appium.webdriver.common.appiumby import AppiumBy
import re
import csv
from selenium.webdriver import Keys
from time import sleep
import unittest


class TestSignUp(unittest.TestCase):
    desired_cap = {
        "platformName": "Android",
        "appium:deviceName": "Pixel 6 Pro API 29",
        "appium:automationName": "UiAutomator2",
        "appium:platformVersion": "11.0",
        "appium:app": "C:\\Users\\salsa\\Downloads\\app-debug (4).apk",
        "appium:appPackage": "com.faylasof.android.waamda"
    }


    def setUp(self):
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', self.desired_cap)
        self.driver.implicitly_wait(10)
        self.driver.setSetting("driver", "compose")

    def test_sign_up_(self):

        self.email_login = self.driver.find_element(by=AppiumBy.XPATH,
                                                    value=
                                                    "/hierarchy/android.widget.FrameLayout/android.widget"
                                                    ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                    ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
                                                    ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
                                                    ".ScrollView/android.view.View[3]/android.widget.Button")
        self.email_login.click()
        self.driver.implicitly_wait(10)

        self.create_account = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
        ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
        ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
        ".ScrollView/android.view.View[5]/android.widget.TextView")
        self.create_account.click()
        sleep(2)

        self.enter_email = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
        ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
        ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
        ".ScrollView/android.view.View[1]/android.widget.EditText")
        self.enter_email.click()
        self.enter_email.clear()
        self.email = "adretest@ad.ad"
        self.enter_email.send_keys(self.email)
        pat = re.compile(r"^\S+@\S+\.\S+$")
        self.result = re.match(pat, self.email)
        if self.result:
            print("valid email")
        else:
            print("not valid")
            assert self.result, "invalid email"
        print(self.email)
        sleep(2)

        try:
            self.new_account = self.driver.find_element(by=AppiumBy.XPATH, value=
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
            ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
            ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
            ".ScrollView/android.view.View[1]/android.widget.TextView").is_displayed()
            assert False == self.new_account, "use another account"

        except NoSuchElementException:

            sleep(2)
            self.enter_pass = self.driver.find_element(by=AppiumBy.XPATH, value=
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
            ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
            ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
            ".ScrollView/android.view.View[2]/android.widget.EditText")

            self.enter_pass.click()
            self.enter_pass.clear()
            sleep(2)
            self.password = "adadadad"
            self.enter_pass.send_keys(self.password)
            sleep(2)
            valid_pass = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")
            pass_result = re.match(valid_pass, self.password)
            print(pass_result)
            if pass_result:
                print("match")
            else:
                print("not match")
            sleep(2)
            assert pass_result, "invalid pass"
        self.show_pass = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
        ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
        ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
        ".ScrollView/android.view.View[2]/android.widget.EditText/android.view.View/android.widget.Button")
        self.show_pass.click()

        sleep(2)

        self.Login = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
        ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
        ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
        ".ScrollView/android.view.View[3]/android.widget.Button")
        self.Login.click()
        int1 = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[7]")
        int1.click()
        sleep(1)
        int2 = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]")
        int2.click()
        sleep(1)
        int3 = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[3]")
        int3.click()
        sleep(1)
        int4 = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]")
        int4.click()
        sleep(1)
        int5 = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[5]")
        int5.click()
        sleep(1)
        int6 = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[6]")
        int6.click()
        # elements = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.view.View")
        # if len(elements) >= 5:
        #     random_indices = random.sample(range(len(elements)), 1)
        #     for i in random_indices:
        #         sleep(2)
        #         elements[i].click()
        # else:
        #     print('Not enough elements to click on.')
        # random_indices = random.sample(range(len(elements)), 5)
        # for i in random_indices:
        #     elements[i].click()
        sleep(2)
        try:
            self.more_then_five = self.driver.find_element(by=AppiumBy.XPATH,
                                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.cardview.widget.CardView/android.view.ViewGroup").is_displayed()
            assert False == self.more_then_five, "choose only five"
        except NoSuchElementException:
            print("more then five")
        # self.start_now = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget"
        #                                               ".LinearLayout/android.widget.FrameLayout/android.widget"
        #                                               ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
        #                                               ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
        #                                               ".ScrollView/android.view.View[3]/android.widget.Button")
        # self.start_now.click()

    # def tearDown(self):
    #     self.driver.quit()

if __name__ == '__main__':
    unittest.main()
