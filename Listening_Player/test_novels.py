from time import sleep
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import HomeScreen.test_drivingMode
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
import HomeScreen.test_daily_content
from Config import config
import Login_Signup.test_Login


class TestNovels(unittest.TestCase):
    def setUp(self):
        self.driver = config.create_appium_driver()
        self.driver.implicitly_wait(30)
        Login_Signup.test_Login.TestLogin.login_required(self)

    def test_novelsss(self):
        try:
            Login_Signup.test_Login.TestLogin.test_Login_BYEmail(self)
        except NoSuchElementException:
            pass
        sleep(5)
        action = TouchAction(self.driver)

        for i in range(2):
            action.press(x=500, y=2500).move_to(x=500, y=1000).release().perform()
            sleep(5)

        self.novel = self.driver.find_element(by=AppiumBy.XPATH,
                                              value=
                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                              "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                              ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
                                              "1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView"
                                              "/android.view.View/android.view.View/android.widget.ScrollView/android"
                                              ".view.View[5]")
        self.novel.click()
        sleep(7)
        self.play_the_button = self.driver.find_element(by=AppiumBy.XPATH,
                                                        value=
                                                        "/hierarchy/android.widget.FrameLayout/android.widget"
                                                        ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                        ".LinearLayout/android.widget.FrameLayout/android.view"
                                                        ".ViewGroup/android.widget.FrameLayout/android.widget"
                                                        ".FrameLayout/androidx.compose.ui.platform.ComposeView"
                                                        "/android.view.View/android.widget.Button[4]")
        self.play_the_button.click()
        sleep(15)

        # Listening_Player.test_drivingMode.TestDRivingModee.test_drivingMode(self)
        sleep(5)
        self.forwardTen = self.driver.find_element(by=AppiumBy.XPATH,
                                                   value=
                                                   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                   "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                   ".widget.FrameLayout/android.view.ViewGroup/android.widget"
                                                   ".FrameLayout/android.widget.FrameLayout/androidx.compose.ui"
                                                   ".platform.ComposeView/android.view.View/android.widget.Button[2]")
        self.forwardTen.click()

        self.backwardTen = self.driver.find_element(by=AppiumBy.XPATH,
                                                    value=
                                                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                    "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                                    ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android"
                                                    ".widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android"
                                                    ".view.View/android.widget.Button[6]")
        self.backwardTen.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


    def test_run(self):
        TestListeningReadingButton.click_on_listening(self)
        TestListeningReadingButton.test_download(self)
        TestListeningReadingButton.test_switch_reading()
