import unittest
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.connectiontype import ConnectionType
import HomeScreen.test_daily_content
from selenium.common.exceptions import NoSuchElementException

import Login_Signup.test_Login
from Config import config


class TestAddToPlayList(unittest.TestCase):
    def setUp(self):
        self.driver = config.create_appium_driver()
        self.driver.implicitly_wait(30)

    def test_AddDailyBookToPlayList(self):
        try:
            Login_Signup.test_Login.TestLogin.test_Login_BYEmail(self)
        except NoSuchElementException:
            pass

        self.addToPlayList = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                      value='new UiSelector().resourceId("FeaturedContentAddToPlaylistButton")')
        self.addToPlayList.click()
        sleep(10)

        try:
            self.subscription_screen = self.driver.find_element(by=AppiumBy.XPATH,
                                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]/android.widget.Button")
            # self.subscription_screen = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"وجيز بريميوم")

        except NoSuchElementException:
            self.fail("The expected screen is not displayed.")