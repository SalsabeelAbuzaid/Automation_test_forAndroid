import unittest
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.connectiontype import ConnectionType
import Listening_Player.test_Listening_Reading
from selenium.common.exceptions import NoSuchElementException
# from unittest_parallel import R
import Login_Signup.test_Login
from Config import config


class TestAddToPlayList(unittest.TestCase):
    def setUp(self):
        self.driver = config.create_appium_driver()
        self.driver.implicitly_wait(10)
        Login_Signup.test_Login.TestLogin.login_required(self)

    def test_AddDailyBookToPlayList(self):
        self.addToPlayList = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                      value='new UiSelector().resourceId("FeaturedContentAddToPlaylistButton")')
        self.addToPlayList.click()
        sleep(5)

        # try:
        #     self.subscription_screen = self.driver.find_element(by=AppiumBy.XPATH,
        #                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]/android.widget.Button")
        #     # self.subscription_screen = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"وجيز بريميوم")
        #
        # except NoSuchElementException:
        #     self.fail("The expected screen is not displayed.")
        self.close = self.driver.find_element(by=AppiumBy.XPATH,
                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.widget.Button")
        self.close.click()

    # def test_click_on_listening(self):
    #
    #     Listen_daily_book = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
    #                                             value='new UiSelector().resourceId("ListeningButton")')
    #     Listen_daily_book.click()
    #     sleep(5)
    #
    # def test_run(self):
    #     TestAddToPlayList.test_AddDailyBookToPlayList(self)
    #     TestAddToPlayList.test_click_on_listening(self)
