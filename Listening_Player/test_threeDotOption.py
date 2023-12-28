import unittest
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.connectiontype import ConnectionType

import Login_Signup.test_Login
from Config import config

from selenium.common.exceptions import NoSuchElementException

from Listening_Player.test_Listening_Reading import TestListeningReadingButton


class TestThreeDotOption(unittest.TestCase):
    def setUp(self):
        self.driver = config.create_appium_driver()
        self.driver.implicitly_wait(10)
        Login_Signup.test_Login.TestLogin.login_required(self)

    def clickThreeDotOPtion(self):
        TestListeningReadingButton.click_on_listening(self)
        self.ThreeDotOption = self.driver.find_element(by=AppiumBy.XPATH,
                                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[1]")
        self.ThreeDotOption.click()
        sleep(2)

    def test_add_toFavourite(self):
        TestThreeDotOption.clickThreeDotOPtion(self)
        self.AddTo_fav = self.driver.find_element(by=AppiumBy.XPATH,
                                                  value="/hierarchy/android.view.ViewGroup/android.view.View/android.view.View/android.view.View[1]")
        self.AddTo_fav.click()
        sleep(2)

        # self.toast_msg = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH,
        #                                                                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[9]")))
        # self.assertTrue(self.toast_msg.is_displayed(), "it's not added to Favourite")
        # sleep(2)

    #     add assertion for the success msg when they add id to it

    def test_add_toPlayList(self):
        TestThreeDotOption.clickThreeDotOPtion(self)
        self.AddTo_PLaylist = self.driver.find_element(by=AppiumBy.XPATH,
                                                       value="/hierarchy/android.view.ViewGroup/android.view.View/android.view.View/android.view.View[1]")
        self.AddTo_PLaylist.click()
        sleep(2)

    def test_Share(self):
        TestThreeDotOption.clickThreeDotOPtion(self)
        self.share = self.driver.find_element(by=AppiumBy.XPATH,
                                              value="/hierarchy/android.view.ViewGroup/android.view.View/android.view.View/android.view.View[1]")
        self.share.click()
        sleep(2)

    def test_Share(self):
        TestThreeDotOption.clickThreeDotOPtion(self)
        self.share = self.driver.find_element(by=AppiumBy.XPATH,
                                              value="/hierarchy/android.view.ViewGroup/android.view.View/android.view.View/android.view.View[1]")
        self.share.click()
        sleep(2)

if __name__ == '__main__':
    unittest.main()