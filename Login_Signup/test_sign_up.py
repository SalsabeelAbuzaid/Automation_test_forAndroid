import re
import unittest
from time import sleep

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import Login_Signup
from Login_Signup import test_Login
import random


class TestSignUp(unittest.TestCase):
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

    def scroll_down(self):
        self.driver.swipe(start_x=500, start_y=1000, end_x=500, end_y=800, duration=500)
        sleep(2)
        pass

    def test_sign_up_Email(self):

        Login_Signup.test_Login.TestLogin.test_EnterEmail(self)
        try:
            self.register_screen = self.driver.find_element(by=AppiumBy.XPATH,

                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.widget.TextView").is_displayed()
            if not self.register_screen:
                assert False == self.register_screen, "it's a new account"

        except NoSuchElementException:
            raise AssertionError("Element not found. Test failed.")

        self.enter_pass = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
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

        wait = WebDriverWait(self.driver, 5)

        self.show_pass = wait.until(
            EC.presence_of_element_located((By.XPATH,
                                            "hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]/android.widget.EditText/android.view.View/android.widget.Button")))

        self.show_pass.click()

        self.create_account = self.driver.find_element(by=AppiumBy.XPATH,
                                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]")
        self.create_account.click()
        sleep(5)

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

        self.categories2 = [{
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
        self.max_categories_to_choose = min(2, len(self.categories))
        self.max_categories_to_choose2 = min(3, len(self.categories2))

        for i in range(self.max_categories_to_choose):
            xpath = self.categories[i]["xpath"]  # Access the XPath string from the dictionary
            self.category_element = self.driver.find_element(by=AppiumBy.XPATH, value=xpath)
            self.category_element.click()

        screen_size = self.driver.get_window_size()
        screen_height = screen_size['height']
        self.driver.swipe(start_x=screen_size['width'] // 2, start_y=screen_height - 1,
                          end_x=screen_size['width'] // 2, end_y=1, duration=500)

        for s in range(self.max_categories_to_choose2):
            xpath2 = self.categories2[s]["xpath2"]  # Access the XPath string from the dictionary
            self.category_element2 = self.driver.find_element(by=AppiumBy.XPATH, value=xpath2)
            print(self.category_element2, "hjgkgfdtrsdfhgjkjlhrdfg")
            #     self.driver.swipe(start_x=500, start_y=1000, end_x=500, end_y=800, duration=500)
            self.category_element2.click()
        # Perform a swipe from the bottom to the top of the screen

        #     if self.category_element.is_displayed():
        #         self.category_element.click()
        #         self..append(xpath["xpath"])
        #
        # print("5 were choosen")
        # sleep(2)
        #     while True:
        #         try:
        #             category_element = self.driver.find_element(by=AppiumBy.XPATH, value=xpath)
        #
        #         # Check if the category element is currently visible on the screen
        #             if category_element.is_displayed():
        #                 category_element.click()
        #                 self.chosen_categories.append(xpath["xpath"])  # Add the chosen category to the list
        #                 break
        #         except NoSuchElementException:
        #             TestSignUp.scroll_down(self)

        #
        # # self.choose_randomly=random.choices(self.category_element.click())
        # self.error_msg = self.driver.find_element(by=AppiumBy.XPATH,
        #                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.TextView")
        # assert self.error_msg.is_displayed(), "only five were choosing"

        # for i in range(5):
        #     self.category_element = self.driver.find_element(by=AppiumBy.XPATH(value=self.categories[i]))
        #     # for element in self.category_element:
        #     self.category_element.click()
        # Display the list of categories to the user.
        # for category in self.categories:
        #     print(category)

        # Allow the user to select one or more categories.
        # self.selected_categories = []
        # while True:
        #     user_input = input("Select one or more categories (separated by commas): ")
        #     selected_categories = user_input.split(",")
        #
        #     # Validate that the user has selected at least one category and no more than five categories.
        #     if len(selected_categories) < 1 or len(selected_categories) > 5:
        #         print("Please select at least one category and no more than five categories.")
        #     else:
        #         break

        # Continue with the rest of your script, using the selected categories.
        # print("You have selected the following categories:", selected_categories)
        # int1 = self.driver.find_element(by=AppiumBy.XPATH,
        #                                 value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[7]")
        # int1.click()
        # sleep(1)
        # int2 = self.driver.find_element(by=AppiumBy.XPATH,
        #                                 value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]")
        # int2.click()
        # sleep(1)
        # int3 = self.driver.find_element(by=AppiumBy.XPATH,
        #                                 value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[3]")
        # int3.click()
        # sleep(1)
        # int4 = self.driver.find_element(by=AppiumBy.XPATH,
        #                                 value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]")
        # int4.click()
        # sleep(1)
        # int5 = self.driver.find_element(by=AppiumBy.XPATH,
        #                                 value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[5]")
        # int5.click()
        # sleep(1)
        # int6 = self.driver.find_element(by=AppiumBy.XPATH,
        #                                 value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[6]")
        # int6.click()
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
        # sleep(2)
        # try:
        #     self.more_then_five = self.driver.find_element(by=AppiumBy.XPATH,
        #                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.cardview.widget.CardView/android.view.ViewGroup").is_displayed()
        #     assert False == self.more_then_five, "choose only five"
        # except NoSuchElementException:
        #     print("more then five")
    #     # self.start_now = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget"
    #     #                                               ".LinearLayout/android.widget.FrameLayout/android.widget"
    #     #                                               ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
    #     #                                               ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
    #     #                                               ".ScrollView/android.view.View[3]/android.widget.Button")
    #     # self.start_now.click()
    #
    # # def tearDown(self):
    # #     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
