import re
import unittest
from time import sleep

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Login_Signup import test_Login
# from Login_Signup import commen_function
import random
from Config import config


# Create a test class that inherits from unittest.TestCase

class TestSignUp(unittest.TestCase):
    def setUp(self):
        self.driver = config.create_appium_driver()
        self.driver.implicitly_wait(30)

    def test_sign_up_Email(self):
        #  this function to enter the email as a first step
        test_Login.TestLogin.enter_Email(self)
        try:
            self.register_button = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                            value='new UiSelector().resourceId("register_button")').is_displayed()
            if not self.register_button:
                assert False == self.register_button, "it's a new account"

        except NoSuchElementException:
            raise AssertionError("Element not found. Test failed.")

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
            print(self.enter_pass)
        else:
            print("not match")
        sleep(2)
        assert pass_result, "invalid pass"

        wait = WebDriverWait(self.driver, 5)

        # self.show_pass = wait.until(
        #     EC.presence_of_element_located((By.XPATH,
        #                                     "hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]/android.widget.EditText/android.view.View/android.widget.Button")))
        #
        # self.show_pass.click()

        self.create_account = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                       value='new UiSelector().resourceId("register_button")')
        self.create_account.click()
        sleep(5)
        # Gather and shuffle category elements and select a random number of them
        self.categories = [
            {
                "xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]/android.widget.TextView"},
            {
                "xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.widget.TextView"},
            {
                "xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[3]/android.widget.TextView"},
            {
                "xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]/android.widget.TextView"},
            {
                "xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[5]/android.widget.TextView"},
            {
                "xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[6]/android.widget.TextView"},
            {
                "xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[7]/android.widget.TextView"},
            {
                "xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[8]/android.widget.TextView"},
            {
                "xpath": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[9]/android.widget.TextView"}]

        self.categories2 = [
            {
                "xpath2": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.widget.TextView"},
            {
                "xpath2": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[3]/android.widget.TextView"},
            {
                "xpath2": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]/android.widget.TextView"},
            {
                "xpath2": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[5]/android.widget.TextView"},
            {
                "xpath2": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[6]/android.widget.TextView"},
            {
                "xpath2": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[7]/android.widget.TextView"},
            {
                "xpath2": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[8]/android.widget.TextView"},
            {
                "xpath2": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[9]/android.widget.TextView"}]

        random.shuffle(self.categories)
        random.shuffle(self.categories2)

        # Specify the maximum number of categories to choose (up to 5)
        self.max_categories_to_choose = min(3, len(self.categories))
        self.max_categories_to_choose2 = min(2, len(self.categories2))

        for i in range(self.max_categories_to_choose):
            xpath = self.categories[i]["xpath"]  # Access the XPath string from the dictionary
            self.category_element = self.driver.find_element(by=AppiumBy.XPATH, value=xpath)
            self.category_element.click()

        #  scroll the whole screen up
        screen_size = self.driver.get_window_size()
        screen_height = screen_size['height']
        self.driver.swipe(start_x=screen_size['width'] // 2, start_y=screen_height - 1,
                          end_x=screen_size['width'] // 2, end_y=1, duration=500)
        sleep(2)
        for s in range(self.max_categories_to_choose2):
            xpath2 = self.categories2[s]["xpath2"]  # Access the XPath string from the dictionary
            self.category_element2 = self.driver.find_element(by=AppiumBy.XPATH, value=xpath2)
            self.category_element2.click()

        #  check if thr user tried to choose more than five
        try:
            if self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.cardview.widget.CardView/android.view.ViewGroup/android.widget.TextView").is_displayed():
                raise AssertionError("only five were choosing ")
        except NoSuchElementException:
            pass
        except AssertionError as E:
            raise E
        sleep(2)

        # proceed with the sighup process if the user choose a category, if it's not the test will stop
        self.start_now = self.driver.find_element(by=AppiumBy.XPATH,
                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button")
        try:
            if self.start_now.is_displayed() and self.start_now.is_enabled():
                self.start_now.click()
                print("the button is displayed and clickable")
            else:
                raise AssertionError("choose one of the category")
        except NoSuchElementException:
            pass
        except AssertionError as E:
            raise E

        #  assert the home screen
        self.assertHomeScreen = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                         value='new UiSelector().resourceId("com.faylasof.android.waamda:id/navigation_graph_home_filtered")')

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
