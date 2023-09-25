import re
import unittest
from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import sys


class TestLogin(unittest.TestCase):
    desired_cap = {
        'uiautomator2ServerInstallTimeout': 120000,
        'adbExecTimeout': 120000,
        "appium:platformName": "Android",
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
            'http://localhost:4723/wd/hub', options=UiAutomator2Options().load_capabilities(self.desired_cap))
        self.driver.implicitly_wait(30)
        # self.driver.setSetting("driver", "compose")

    def test_EnterEmail(self):

        self.element_loginByEmail = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                             value='new UiSelector().resourceId("email_login_button")')
        self.element_loginByEmail.click()
        self.driver.implicitly_wait(5)

        self.enter_email = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                    value='new UiSelector().resourceId("email_text_field")')
        self.enter_email.click()
        self.enter_email.clear()
        self.email = "sl@testwajeez.co"
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
            if self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]/android.widget.TextView").is_displayed():
                raise AssertionError("plz use a correct email format")
        except NoSuchElementException:
            pass
        except AssertionError as E:
            raise E
        sleep(2)

        self.continueButton = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                       value='new UiSelector().resourceId("continue_button")')
        self.continueButton.click()
        sleep(5)
        # x= self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        #                                 value='new UiSelector().resourceId("login_button")')
        # if not x.is_displayed():
        #     print("Element is not displayed. Stopping the test.")
        #     sys.exit(1)
    def test_login(self):

        TestLogin.test_EnterEmail(self)

        # assert self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        #                                             value='new UiSelector().resourceId("com.faylasof.android.waamda:id/nav_host_container")').is_displayed(), "Element is displayed, but it should not be."

        self.enter_pass = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                   value='new UiSelector().resourceId("password_text_field")')
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

        self.Login = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                              value='new UiSelector().resourceId("login_button")')
        self.Login.click()
        sleep(10)

        self.assertHomeScreen = self.driver.find_element(by=AppiumBy.XPATH,
                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.widget.TextView")

        if self.assertHomeScreen is not None:
            if self.assertHomeScreen.is_displayed():
                # The element exists on the screen and is visible.
                print("The element exists on the screen and is visible.")
            else:
                # The element exists on the screen but is not visible.
                print("The element exists on the screen but is not visible.")
        else:
            # The element does not exist on the screen.
            print("The element does not exist on the screen.")
# #
# #     # def tearDown(self):
# #     #     self.driver.quit()
# # #     #     test_wajeezcast.TestWjeezcast.test_wajeezcast(self)
# # #
# # # if __name__ == '__main__':
# # #     # loader = unittest.TestLoader()
# # #     # suite = unittest.TestSuite()
# # #     # suite.addTests(loader.loadTestsFromTestCase(TestDailybook))
# # #     # suite.addTests(loader.loadTestsFromTestCase(TestWajeezcast))
# # #     unittest.main()
