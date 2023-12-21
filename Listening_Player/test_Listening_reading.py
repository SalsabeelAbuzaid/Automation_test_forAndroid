import unittest
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import Listening_Player.test_drivingMode
import Login_Signup
from Login_Signup import test_Login

from Config import config
from selenium.common.exceptions import NoSuchElementException


class TestListeningReadingButton(unittest.TestCase):

    def setUp(self):
        self.driver = config.create_appium_driver()
        # self.driver.implicitly_wait(10)
        Login_Signup.test_Login.TestLogin.login_required(self)

        # return self.driver

    def click_on_listening(self):
        self.Listen_daily_book = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                          value='new UiSelector().resourceId("ListeningButton")')
        self.Listen_daily_book.click()
        sleep(5)

    def test_check_freemium_user(self):

        # assert the freemium user wait until mohammed add the id so you can modify it.
        try:
            if not self.driver.find_element(AppiumBy.XPATH,
                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.TextView[1]").is_displayed():
                raise AssertionError("it's not a freemium user")
        except NoSuchElementException:
            pass
        except AssertionError as E:
            raise E
        sleep(4)

        # Listen to the daily book
        TestListeningReadingButton.click_on_listening(self)

        # close the screen
        action = TouchAction(self.driver)
        action.press(x=700, y=250).move_to(x=500, y=2000).release().perform()
        sleep(5)

        # self.progress_bar_running = self.driver.find_element(by=AppiumBy.XPATH,
        #                                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.widget.ProgressBar")
        #
        # self.progress_text = self.progress_bar_running.get_attribute("text")
        # # self.initial_progress_text = self.progress_bar_running.get_attribute("text")
        # sleep(10)
        # self.final_progress_text = self.progress_text
        # try:
        #     if self.progress_text != self.final_progress_text:
        #         print("Progress bar is running")
        #     else:
        #         print("Progress bar is not running")
        #
        # except NoSuchElementException:
        #     raise AssertionError("the test failed the progress is not running")
        # pass
        # sleep(5)

    def test_switch_reading(self):

        TestListeningReadingButton.click_on_listening(self)
        sleep(3)
        self.switch_reading = self.driver.find_element(by=AppiumBy.XPATH,
                                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[7]")
        self.switch_reading.click()
        # self.switch_reading = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[8]")
        # self.switch_reading.click()
        sleep(5)

        # change this to any id button to assert the reading screen
        self.reading_screen = self.driver.find_element(by=AppiumBy.XPATH,
                                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.widget.Button[7]")
        assert self.reading_screen.is_displayed(), "The screen did not display after clicking the button."
        self.close_reading_Screen = self.driver.find_element(by=AppiumBy.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.Button[2]")
        self.close_reading_Screen.click()

        pass
        sleep(3)

    def test_download(self):
        TestListeningReadingButton.click_on_listening(self)
        self.Download = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[9]")
        self.Download.click()
        sleep(5)
        self.isDownloading = self.driver.find_element(by=AppiumBy.XPATH,
                                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ProgressBar")
        assert self.isDownloading.is_displayed(), "The book wasn't downloaded."
        sleep(10)
        self.downloaded = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH,
                                                                                                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[9]")))
        self.assertTrue(self.downloaded.is_displayed(), "it's not downloaded try again")
        sleep(2)

        # swipe the screen down to close it
        action = TouchAction(self.driver)
        action.press(x=700, y=250).move_to(x=500, y=2000).release().perform()
        sleep(5)

    def test_reading_button(self):

        self.test_reading_button = self.driver.find_element(by=AppiumBy.XPATH,
                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[5]/android.widget.TextView/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[4]")
        self.test_reading_button.click()


if __name__ == '__main__':
    unittest.main()
