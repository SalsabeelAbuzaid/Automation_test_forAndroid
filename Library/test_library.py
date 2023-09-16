import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
# import os
# from uiautomator import device as d

import Library.test_login
import subprocess


class TestSearch(Library.test_login.TestLogin):
    desired_cap = {
  "platformName": "Android",
  "appium:deviceName": "Pixel 2 API 30",
  "appium:automationName": "UiAutomator2",
  "appium:platformVersion": "11.0",
  "appium:app": "C:\\Users\\salsa\\Downloads\\app-debug (10).apk",
  "appium:appPackage": "com.faylasof.android.waamda",
  "appium:fullReset": True,
}

    def setUp(self):
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', self.desired_cap)
        self.driver.implicitly_wait(30)
        self.driver.setSetting("driver", "compose")

        wait = WebDriverWait(self.driver, 10)
        Library.test_login.TestLogin.test_login(self)
        sleep(5)

    def test_library_click(self):
        self.library_click = self.driver.find_element(by=AppiumBy.ID,
                                                     value="com.faylasof.android.waamda:id/navigation_graph_library")

        self.library_click.click()
        sleep(3)

    def test_library_section(self):
        sleep(2)
        self.test_library_click()
        sleep(5)
        self.title_u_startWith = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]")
        self.title_u_startWith.click()
        sleep(5)
        self.driver.back()

        self.title_u_finished = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]")
        self.title_u_finished.click()
        sleep(3)
        self.driver.back()
        sleep(5)

        self.favourite = self.driver.find_element(by=AppiumBy.XPATH, value= "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]")
        self.favourite.click()
        sleep(3)
        self.driver.back()

        self.downloaded_items = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[4]")
        self.downloaded_items.click()
        sleep(5)
        self.driver.back()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()




