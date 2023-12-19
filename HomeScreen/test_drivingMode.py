from time import sleep
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import HomeScreen.test_daily_content

from selenium.common.exceptions import NoSuchElementException
import Login_Signup.test_Login
from Config import config


class TestDRivingModee(unittest.TestCase):

    def setUp(self):
        self.driver = config.create_appium_driver()
        self.driver.implicitly_wait(30)

    def test_drivingMode(self):
        try:
            Login_Signup.test_Login.TestLogin.test_Login_BYEmail(self)
        except NoSuchElementException:
            pass

        HomeScreen.test_daily_content.TestDailybook.test_click_onListening(self)
        sleep(5)

        self.driving_mode = self.driver.find_element(by=AppiumBy.XPATH,
                                                     value=
                                                     "/hierarchy/android.widget.FrameLayout/android.widget"
                                                     ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                     ".LinearLayout/android.widget.FrameLayout/android.view"
                                                     ".ViewGroup/android.widget.FrameLayout/android.widget"
                                                     ".FrameLayout/androidx.compose.ui.platform.ComposeView"
                                                     "/android.view.View/android.widget.Button[9]")
        self.driving_mode.click()
        sleep(20)
        assert self.driving_mode, "it's not the driving mode screen"
        # the xpath for the driving mode and the player screen is the same so the assertion not affective that's way
        # self.driving_mode_screen = self.driver.find_element(by=AppiumBy.XPATH,
        #                                                     value=
        #                                                     "/hierarchy/android.widget.FrameLayout/android.widget"
        #                                                     ".LinearLayout/android.widget.FrameLayout/android.widget"
        #                                                     ".LinearLayout/android.widget.FrameLayout/android.view"
        #                                                     ".ViewGroup/android.widget.FrameLayout/android.widget"
        #                                                     ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View")
        # assert self.driving_mode_screen, "it's not the driving mode screen"
        self.backTo_ThePLayer = self.driver.find_element(by=AppiumBy.XPATH,
                                                         value=
                                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                         "/android.widget.Framself.eLayout/android.widget.LinearLayout/android"
                                                         ".widget.FrameLayout/android.view.ViewGroup/android.widget"
                                                         ".FrameLayout/android.widget.FrameLayout/androidx.compose.ui"
                                                         ".platform.ComposeView/android.view.View/android.widget.Button[3]")
        self.backTo_ThePLayer.click()
        sleep(2)
        self.player_screen = self.driver.find_element(by=AppiumBy.XPATH,
                                                      value=
                                                      "/hierarchy/android.widget.FrameLayout/android.widget"
                                                      ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                      ".LinearLayout/android.widget.FrameLayout/android.view"
                                                      ".ViewGroup/android.widget.FrameLayout/android.widget"
                                                      ".FrameLayout/androidx.compose.ui.platform.ComposeView"
                                                      "/android.view.View/android.widget.TextView[4]")
        assert self.player_screen, "it's not the the main player screen"
        sleep(5)

    def test_button_drivingMOdeScreen(self):
        self.driving_mode = self.driver.find_element(by=AppiumBy.XPATH,
                                                     value=
                                                     "/hierarchy/android.widget.FrameLayout/android.widget"
                                                     ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                     ".LinearLayout/android.widget.FrameLayout/android.view"
                                                     ".ViewGroup/android.widget.FrameLayout/android.widget"
                                                     ".FrameLayout/androidx.compose.ui.platform.ComposeView"
                                                     "/android.view.View/android.widget.Button[9]")
        self.driving_mode.click()
        sleep(20)
        assert self.driving_mode, "it's not the driving mode screen"
        self.next = self.driver.find_element(by=AppiumBy.XPATH,
                                             value=
                                             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                             "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                             ".widget.FrameLayout/android.view.ViewGroup/android.widget"
                                             ".FrameLayout/android.widget.FrameLayout/androidx.compose.ui"
                                             ".platform.ComposeView/android.view.View/android.widget.Button[1]")
        self.next.click()

        sleep(10)
        self.previous = self.driver.find_element(by=AppiumBy.XPATH,
                                                 value=
                                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                 "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                                 ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android"
                                                 ".widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android"
                                                 ".view.View/android.widget.Button[2]")
        self.previous.click()
        sleep(10)
        self.backTo_ThePLayer = self.driver.find_element(by=AppiumBy.XPATH,
                                                         value=
                                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                         "/android.widget.Framself.eLayout/android.widget.LinearLayout/android"
                                                         ".widget.FrameLayout/android.view.ViewGroup/android.widget"
                                                         ".FrameLayout/android.widget.FrameLayout/androidx.compose.ui"
                                                         ".platform.ComposeView/android.view.View/android.widget.Button[3]")
        self.backTo_ThePLayer.click()
        sleep(2)
        self.player_screen = self.driver.find_element(by=AppiumBy.XPATH,
                                                      value=
                                                      "/hierarchy/android.widget.FrameLayout/android.widget"
                                                      ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                      ".LinearLayout/android.widget.FrameLayout/android.view"
                                                      ".ViewGroup/android.widget.FrameLayout/android.widget"
                                                      ".FrameLayout/androidx.compose.ui.platform.ComposeView"
                                                      "/android.view.View/android.widget.TextView[4]")
        assert self.player_screen, "it's not the the main player screen"
        sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
