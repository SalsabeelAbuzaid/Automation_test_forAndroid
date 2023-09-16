#
# from appium import webdriver
# # import keyboard
# # import os
# # from time import sleep
# from appium.webdriver.common.appiumby import AppiumBy
# import re
# from selenium.webdriver import Keys
# from time import sleep
# import unittest
# from appium.webdriver.common.appiumby import AppiumBy
# import re
# from selenium.webdriver import Keys
# from time import sleep
# import unittest
# # import random
# # from validate_email import validate_email
#
#
# class TestStringMethods (unittest.TestCase):
#     desired_cap = {
#         "platformName": "Android",
#         "appium:deviceName": "Pixel 6 API 29",
#         "appium:automationName": "UiAutomator2",
#         "appium:platformVersion": "11.0",
#         "appium:app": "C:\\Users\\salsa\\Downloads\\app-debug.apk",
#         "appium:appPackage": "com.faylasof.android.waamda"
#     }
#
#     def setUp(self):
#         self.driver = webdriver.Remote(
#             'http://localhost:4723/wd/hub', self.desired_cap)
#         self.driver.implicitly_wait(10)
#     #     self.element_login = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
#     #                                                   ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
#     #                                                   ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
#     #                                                   ".ScrollView/android.view.View[3]/android.widget.Button")
#     #     self.element_login.click()
#     #     self.driver.implicitly_wait(10)
#     #
#     #     self.enter_email = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
#     #                                                 ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
#     #                                                 ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
#     #                                                 ".ScrollView/android.view.View[1]/android.widget.EditText")
#     #     self.enter_email.click()
#     #     self.enter_email.clear()
#     #     self.email = "ad@ad.ad"
#     #     self.enter_email.send_keys(self.email)
#     #     pat = re.compile(r"^\S+@\S+\.\S+$")
#     #     self.result = re.match(pat, self.email)
#     #     if self.result:
#     #         print("valid email")
#     #     else:
#     #         print("not valid")
#     #     assert self.result, "invalid email"
#     #     print(self.email)
#     #     sleep(2)
#     #     self.enter_pass = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
#     #                                                ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
#     #                                                ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
#     #                                                ".ScrollView/android.view.View[2]/android.widget.EditText")
#     #
#     #     self.enter_pass.click()
#     #     self.enter_pass.clear()
#     #     sleep(2)
#     #     self.password = "adadadad"
#     #     self.enter_pass.send_keys(self.password)
#     #     sleep(2)
#     #     valid_pass = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")
#     #     pass_result = re.match(valid_pass, self.password)
#     #     print(pass_result)
#     #     if pass_result:
#     #         print("match")
#     #     else:
#     #         print("not match")
#     #     sleep(2)
#     #     assert pass_result, "invalid pass"
#     #     self.show_pass = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
#     #                                               ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
#     #                                               ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
#     #                                               ".ScrollView/android.view.View[2]/android.widget.EditText/android.view.View/android.widget.Button")
#     #     self.show_pass.click()
#     #
#     #     sleep(2)
#     #
#     #     self.test_login_signup.py = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
#     #                                           ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
#     #                                           ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
#     #                                           ".ScrollView/android.view.View[3]/android.widget.Button")
#     #     self.test_login_signup.py.click()
#     #     sleep(2)
#
#     if __name__ == '__main__':
#         unittest.main()
import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Android Emulator",
            "app": "path/to/app.apk"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.wait = WebDriverWait(self.driver, 10)

    def test_login(self):
        # Perform login
        email_field = self.driver.find_element(by=AppiumBy.ID, value="email_field_id")
        email_field.send_keys("testuser@test.com")
        password_field = self.driver.find_element(by=AppiumBy.ID, value="password_field_id")
        password_field.send_keys("testpassword")
        login_button = self.driver.find_element(by=AppiumBy.ID, value="login_button_id")
        login_button.click()
        sleep(2)

    def tearDown(self):
        self.driver.quit()

class TestBook(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Android Emulator",
            "app": "path/to/app.apk"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.wait = WebDriverWait(self.driver, 10)

    def test_select_book(self):
        # Perform action that requires login
        self.driver.find_element(by=AppiumBy.ID, value="books_tab_id").click()
        sleep(2)
        book_title = "Test Book Title"
        book_element = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f"//android.widget.TextView[@text='{book_title}']")))
        book_element.click()
        sleep(2)
        # Add assertions here

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestLogin('test_login'))
    suite.addTest(TestBook('test_select_book'))
    unittest.TextTestRunner(verbosity=2).run(suite)

