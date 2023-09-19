import re
import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
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
  "appium:app": "C:\\Users\\salsa\\Downloads\\app-debug (16).apk",
  "appium:appPackage": "com.faylasof.android.waamda",
  # "appium:noReset": True,
  "appium:locale": "JO",
  "appium:language": "en",
  "appium:unicodeKeyboard": True,
  "appium:resetKeyboard": True,
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot" : True,
    "appium:newCommandTimeout":3600,
    "appium:connectHardwareKeyboard": True}


    def setUp(self):
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', self.desired_cap)
        self.driver.implicitly_wait(30)
        self.driver.setSetting("driver", "compose")

    def test_Login(self):

        self.element_loginByEmail = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[3]")
        self.element_loginByEmail.click()
        self.driver.implicitly_wait(10)

        self.enter_email = self.driver.find_element(by=AppiumBy.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]/android.widget.EditText")
        self.enter_email.click()
        self.enter_email.clear()
        self.email = "ssssl1@wajeez.co"
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
        # self.emailScreen = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView")
        # self.assertTrue(self.emailScreen.is_displayed(), "it is not displayed the right page")
        sleep(2)
        self.continueButton = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        self.continueButton.click()

        self.LoginEmailScreen = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]/android.widget.Button")
                                                         # value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.TextView[1]")
        self.assertTrue(self.LoginEmailScreen.is_displayed(), "it is not displayed the right page")
        sleep(2)

#         self.enter_pass = self.driver.find_element(by=AppiumBy.XPATH,
#                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.widget.EditText")
#
#         self.enter_pass.click()
#         self.enter_pass.clear()
#         sleep(2)
#         self.password = "salsabeel"
#
#
#         self.enter_pass.send_keys(self.password)
#         sleep(2)
#         valid_pass = re.compile(r"[A-Za-z0-9@#$%^.&+=]{8,}")
#         pass_result = re.match(valid_pass, self.password)
#         print(pass_result)
#         if pass_result:
#             print("match")
#         else:
#             print("not match")
#         sleep(2)
#         assert pass_result, "invalid pass"
#         self.show_pass = self.driver.find_element(by=AppiumBy.XPATH,
#                                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.widget.EditText/android.view.View/android.widget.Button")
#         self.show_pass.click()
#
#         sleep(2)
#
#         self.Login = self.driver.find_element(by=AppiumBy.XPATH,
#                                               value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]/android.widget.Button")
#         self.Login.click()
#         sleep(10)
#
#     # def test_success(self):
#
#         self.home_screen = self.driver.find_element(by=AppiumBy.XPATH,
#                                                     value="/hierarchy/android.widget.FrameLayout")
#         self.assertTrue(self.home_screen.is_displayed(),"HomeScreen not displayed after login")
#         sleep(8)
#
#
#
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
