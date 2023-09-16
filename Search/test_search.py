import random
import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
# import os
# from uiautomator import device as d

import Search.test_login
import subprocess


class TestSearch(Search.test_login.TestLogin):
    desired_cap = {
  "platformName": "Android",
  "appium:deviceName": "Pixel 2 API 30",
  "appium:automationName": "UiAutomator2",
  "appium:platformVersion": "11.0",
  "appium:app": "C:\\Users\\salsa\\Downloads\\app-debug (10).apk",
  "appium:appPackage": "com.faylasof.android.waamda",
  "appium:fullReset": True,
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

        wait = WebDriverWait(self.driver, 10)
        Search.test_login.TestLogin.test_login(self)
        sleep(5)

    def test_search_click(self):
        self.search_click = self.driver.find_element(by=AppiumBy.ID,
                                                     value="com.faylasof.android.waamda:id/navigation_graph_explore")

        self.search_click.click()
        sleep(3)

    def test_search(self):
        sleep(2)
        self.test_search_click()
        self.choose_cat = self.driver.find_element(by=AppiumBy.XPATH,
                                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[5]")

        self.choose_cat.click()
        sleep(5)
        self.follow = self.driver.find_element(by=AppiumBy.XPATH,
                                               value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View")
        self.follow.click()
        # we need to add assertion for the toest msg here t ensure that the cat has been followed
        sleep(10)
        self.toast_msg = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.cardview.widget.CardView/android.view.ViewGroup/android.widget.ImageView")
        self.assertTrue(self.toast_msg.is_displayed())
        # sleep(3)
        self.back = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.widget.Button")
        self.back.click()

        # self.search_field = self.driver.find_element(by=AppiumBy.XPATH, value=
        # "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText/android.view.View")
        # self.search_field.click()
        sleep(3)
        # self.search_field.clear()

    def test_search_input(self):
        self.test_search_click()

        self.search_field = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText/android.view.View")
        self.search_field.click()
        sleep(5)
        self.search_field.clear()
        sleep(3)
        # self.driver.activate_ime_engine('io.appium.android.ime/.UnicodeIME')
        # sleep(2)
        self.search_query = "ال"
        # # str_decoded = self.search_query.decode('utf_16', 'strict')
        self.search_field.send_keys(self.search_query)
        # sleep(5)
        # self.driver.activate_ime_engine('com.android.inputmethod.latin/.LatinIME')
        # sleep(2)
        # list_ime_cmd = "adb shell ime list -s"
        # available_ime = subprocess.check_output(list_ime_cmd.split()).decode().strip().split(":")
        # if "com.android.inputmethod.Arabic" not in available_ime:
        #     print("Arabic keyboard is not installed. Please install it from the Google Play Store.")
        #     exit()

        # Set the Arabic keyboard as the default input method
        # set_ime_cmd = "adb shell ime set com.android.inputmethod.Arabic"
        # subprocess.run(set_ime_cmd.split(), capture_output=True)

        # # Type in the search query using ADB shell input text command
        # tap_cmd = "adb shell input tap 100 100"  # Tap the search field
        # text_cmd = "adb shell input text 'مرحبا'"  # Type the Arabic search query
        # submit_cmd = "adb shell input keyevent 84"  # Press the search button
        #
        # subprocess.run(tap_cmd.split(), capture_output=True)
        # subprocess.run(text_cmd.split(), capture_output=True)
        # subprocess.run(submit_cmd.split(), capture_output=True)
        # d.server.adb.cmd("ime set com.android.inputmethod.Arabic").wait()

        # self.search_field.send_keys("h")
        # action = TouchAction(self.driver)
        # action.tap(self.search_field).perform()
        # os.system("adb shell ime set com.android.inputmethod.Arabic")
        # # Type in the search query using ADB shell input text command
        # os.system("adb shell input tap 100 100")  # Tap the search field
        # os.system("adb shell input text 'ملالا'")  # Type the عربية search query
        # os.system("adb shell input keyevent 84")
        # search_query = "م"
        # unicode_string = search_query.decode('utf-8')
        # unicode_strings = [byte_string.decode('utf-8') for byte_string in search_query]

        # unicode_strings = [search_query.decode('utf-8') for b in search_query]
        # self.search_text = random.choice(unicode_strings)
        # self.driver.execute_script('mobile: shell', {'command': 'input text "{}"'.format(os.system())})

        # Close the keyboard by tapping outside the search bar
        # action.tap(x=8, y=8).perform()

        sleep(10)

        # ///// this how i can control the mouse
        # ///// py.click()
        # ///// py.write("ggggg", interval=0.1)
        # //// py.press("return")

        #
        # self.search_top10 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]")
        # self.search_top10.click()
        # sleep(5)

        # self.books_tab = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View")
        # self.books_tab.click()
        # sleep(2)
        #
        # self.choose_book = self.driver.find_element(by=AppiumBy.XPATH, value= "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[3]/android.view.View")
        # self.choose_book.click()
        # sleep(3)

        # random_text = 'انا الملالا'.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        # self.search_field.send_keys(random_text)
        #
        #
        # # keyboard.write("blah", delay = 0.1)
        # text = k(self.driver)
        # text.press_keycode(66)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
