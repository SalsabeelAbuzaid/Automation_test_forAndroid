import re
import unittest
from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import sys
from Config import config
# import commen_function

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = config.create_appium_driver()
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

    #
        # Validate the email format
        self.email = "salsa+123@wajeez.test"
        self.enter_email.send_keys(self.email)
        pat = re.compile(r"^\S+@\S+\.\S+$")
        self.result = re.match(pat, self.email)
        if self.result:
            print("valid email")
        else:
            print("not valid")
        assert self.result, "invalid email"
        print(self.result)
        sleep(2)

        # Check for an error message
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

    def test_login(self):

        # Call the test_EnterEmail as it's the first step
        TestLogin.test_EnterEmail(self)

        self.enter_pass = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                   value='new UiSelector().resourceId("password_text_field")')
        self.enter_pass.click()
        self.enter_pass.clear()
        sleep(2)
        self.password = "salsabeel"
        self.enter_pass.send_keys(self.password)
        sleep(2)

        # Validate the password stander
        valid_pass = re.compile(r"[A-Za-z0-9@#$%^.&+=]{8,}")
        pass_result = re.match(valid_pass, self.password)
        print(pass_result)
        if pass_result:
            print("match")
        else:
            print("not match")
        sleep(2)
        assert pass_result, "invalid pass"
        # Trying to navigate the user to the sign up function when it's a new email
        # self.register_screen = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        #                                            value='new UiSelector().resourceId("register_button")').is_displayed()
        #
        # if not self.register_screen:
        #     pass
        # else:
        #     commen_function.TestCommenFuntion.Signp_function()

        # self.show_pass = self.driver.find_element(by=AppiumBy.XPATH,
        #                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.widget.EditText/android.view.View/android.widget.Button")
        # self.show_pass.click()

        #  login
        self.Login = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                              value='new UiSelector().resourceId("login_button")')
        self.Login.click()
        sleep(10)

        self.assertHomeScreen = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                         value='new UiSelector().resourceId("ReadingButton")')

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

    if __name__ == '__main__':
        unittest.main()
