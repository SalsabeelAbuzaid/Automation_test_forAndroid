import unittest
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

import HomeScreen.test_daily_content
from selenium.common.exceptions import NoSuchElementException
from Config import config
import Login_Signup.test_Login


class TestNovels(unittest.TestCase):
    def setUp(self):
        self.driver = config.create_appium_driver()
        self.driver.implicitly_wait(30)

    def test_Show_more(self):
        try:
            Login_Signup.test_Login.TestLogin.test_Login_BYEmail(self)
        except NoSuchElementException:
            pass
        HomeScreen.test_daily_content.TestDailybook.test_click_onListening(self)
        sleep(5)
        action = TouchAction(self.driver)
        action.press(x=500, y=2500).move_to(x=500, y=1000).release().perform()
        sleep(5)

        self.show_more = self.driver.find_element(by=AppiumBy.XPATH,
                                                  value=
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                  "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                                  ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
                                              "1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView"
                                              "/android.view.View/android.view.View/android.widget.ScrollView/android"
                                              ".view.View[4]")
        self.show_more.click()
        sleep(7)
        self.pick_book = self.driver.find_element(by=AppiumBy.XPATH,
                                                        value=
                                                        "/hierarchy/android.widget.FrameLayout/android.widget"
                                                        ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                        ".LinearLayout/android.widget.FrameLayout/android.view"
                                                        ".ViewGroup/android.widget.FrameLayout["
                                                        "1]/android.widget.FrameLayout/androidx.compose.ui.platform"
                                                        ".ComposeView/android.view.View/android.view.View/android.view.View[2]")
        self.pick_book.click()

        sleep(5)
        self.play = self.driver.find_element(by=AppiumBy.XPATH,
                                                   value=
                                                   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                   "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                   ".widget.FrameLayout/android.view.ViewGroup/android.widget"
                                                   ".FrameLayout/android.widget.FrameLayout/androidx.compose.ui"
                                                   ".platform.ComposeView/android.view.View/android.widget.Button[4]")
        self.play.click()
        sleep(10)


    def tearDown(self):
        self.driver.quit()


#
#
if __name__ == '__main__':
    unittest.main()
