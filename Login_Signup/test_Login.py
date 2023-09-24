# from test_daily_book import TestDailybook
# from test_wajeezcast import TestWajeezcast
from selenium.common.exceptions import NoSuchElementException

import re
import unittest
from time import sleep

from google.auth.transport import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.appiumby import AndroidBy

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from Login_Signup import test_sign_up


# import os


# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class TestLogin(unittest.TestCase):
    desired_cap = {
        "platformName": "Android",
        "appium:deviceName": "Pixel 6 Pro API 29",
        "appium:automationName": "UiAutomator2",
        "appium:platformVersion": "10.0",
        "appium:app": "C:\\Users\\salsa\\Downloads\\app-debug (16).apk",
        "appium:appPackage": "com.faylasof.android.waamda",
        # "appium:noReset": True,
        "appium:locale": "JO",
        "appium:language": "en",
        "appium:unicodeKeyboard": True,
        "appium:resetKeyboard": True,
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True}

    def setUp(self):
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', self.desired_cap)
        self.driver.implicitly_wait(30)
        self.driver.setSetting("driver", "compose")

    def test_EnterEmail(self):
        # try:
        # self.new_account = self.driver.find_element(by=AppiumBy.XPATH, value=
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
        #     ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
        #     ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
        #     ".ScrollView/android.view.View[1]/android.widget.TextView").is_displayed()
        #     assert False == self.new_account, "use another account"
        #
        self.element_loginByEmail = self.driver.find_element(by=AppiumBy.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[3]")

        self.element_loginByEmail.click()
        self.driver.implicitly_wait(10)

        self.enter_email = self.driver.find_element(by=AppiumBy.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]/android.widget.EditText")
        self.enter_email.click()
        self.enter_email.clear()
        self.email = "cxdammjhs@wajeez.co"
        self.enter_email.send_keys(self.email)
        # self.entered_email = self.enter_email.get_attribute("text")
        # assert self.entered_email == self.email, "Entered email does not match expected email"

        pat = re.compile(r"^\S+@\S+\.\S+$")
        self.result = re.match(pat, self.email)
        if self.result:
            print("valid email")
        else:
            print("not valid")
        assert self.result, "invalid email"
        print(self.email)
        sleep(2)

        self.continueButton = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        self.continueButton.click()
        sleep(2)

        # self.Login = self.driver.find_element(by=AppiumBy.XPATH,
        #                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]/android.widget.Button")
        # if not self.Login.is_displayed():
        #     raise AssertionError("Email is new. Test failed.")
        # else:
        #     print("email is not new")
        #     test_sign_up.TestSignUp.test_sign_up_Email(self)

        # except NoSuchElementException:
        #     raise AssertionError("Element not found. Test failed.")
        # backend_url = "https://api.wajeez.group/api/identity/v1/Account/authenticate"
        # response = requests.post(backend_url, json={"email": self.email})
        #
        # if response == 200:
        #     data = response.json()
        #     if data.get("exists"):
        #         login_screen = WebDriverWait(self.driver, 10).until(
        #             EC.presence_of_element_located((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]/android.widget.Button"))
        #         )
        #         print(f"Email '{self.email}' already exists. Navigating to login screen.")
        #     else:
        #         registration_screen = WebDriverWait(self.driver, 10).until(
        #             EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.Button"))
        #         )
        #         print(f"Email '{self.email}' doesn't exist. Navigating to registration screen.")
        # else:
        #     print("Error occurred while checking email existence.")

    def test_login(self):

        TestLogin.test_EnterEmail(self)

        # find a way to assert this screen
        # sleep(10)
        #
        # self.LoginEmailScreen = self.driver.find_element(by=AppiumBy.XPATH,
        #                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.TextView[1]").is_displayed()
        # assert self.LoginEmailScreen, "it is not displayed the right page"
        # self.asser"tTrue(self.LoginEmailScreen.is_displayed(), "it is not displayed the right page")

        self.enter_pass = self.driver.find_element(by=AppiumBy.XPATH,
                                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.widget.EditText")

        self.enter_pass.click()
        self.enter_pass.clear()
        sleep(2)
        self.password = "salsabeel"

        self.enter_pass.send_keys(self.password)
        sleep(2)
        valid_pass = re.compile(r"[A-Za-z0-9@#$%^.&+=]{8,}")
        pass_result = re.match(valid_pass, self.password)
        print(pass_result)
        if pass_result:
            print("match")
        else:
            print("not match")
        sleep(2)
        assert pass_result, "invalid pass"
        self.show_pass = self.driver.find_element(by=AppiumBy.XPATH,
                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.widget.EditText/android.view.View/android.widget.Button")
        self.show_pass.click()

        self.Login = self.driver.find_element(by=AppiumBy.XPATH,
                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]/android.widget.Button")
        self.Login.click()
        sleep(10)

        assertHomeScreen = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="الرئيسية")

        if assertHomeScreen is not None:
            if assertHomeScreen.is_displayed():
                # The element exists on the screen and is visible.
                print("The element exists on the screen and is visible.")
            else:
                # The element exists on the screen but is not visible.
                print("The element exists on the screen but is not visible.")
        else:
            # The element does not exist on the screen.
            print("The element does not exist on the screen.")

#     # def tearDown(self):
#     #     self.driver.quit()
# #     #     test_wajeezcast.TestWjeezcast.test_wajeezcast(self)
# #
# # if __name__ == '__main__':
# #     # loader = unittest.TestLoader()
# #     # suite = unittest.TestSuite()
# #     # suite.addTests(loader.loadTestsFromTestCase(TestDailybook))
# #     # suite.addTests(loader.loadTestsFromTestCase(TestWajeezcast))
# #     unittest.main()
