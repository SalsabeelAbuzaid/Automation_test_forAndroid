from time import sleep
import unittest
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
import vlc
from appium.webdriver.common.appiumby import AppiumBy
# import HomeScreen.test_drivingMode
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import Login_Signup
import HomeScreen
from Login_Signup import test_Login
from Config import config


class TestDailybook(Login_Signup.test_Login.TestLogin):
    # def setUp(self):
    #
    #     self.driver = config.create_appium_driver()
    #     self.driver.implicitly_wait(30)
    #     Login_Signup.test_Login.TestLogin.test_login(self)

    def test_click_onListening(self):
        sleep(5)
        # assert the freemium user
        # try:
        #     if not self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        #                                                      value='new UiSelector().resourceId("ListeningButton")').is_displayed():
        #         raise AssertionError("it's not a freemium user")
        # except NoSuchElementException:
        #     pass
        # except AssertionError as E:
        #     raise E
        # sleep(4)
        # Listen to the daily book
        self.Listen_daily_book = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                          value='new UiSelector().resourceId("ListeningButton")')
        self.Listen_daily_book.click()
        sleep(5)
        self.progress_bar_running = self.driver.find_element(by=AppiumBy.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]/android.widget.ProgressBar")

        self.progress_text = self.progress_bar_running.get_attribute("text")
        # self.initial_progress_text = self.progress_bar_running.get_attribute("text")
        sleep(10)
        self.final_progress_text = self.progress_text
        try:
            if self.progress_text != self.final_progress_text:
                print("Progress bar is running")
            else:
                print("Progress bar is not running")

        except NoSuchElementException:
            raise AssertionError("the test failed the progress is not running")

    def test_reading_button(self):
        self.test_reading_button = self.driver.find_element(by=AppiumBy.XPATH,
                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[5]/android.widget.TextView/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[4]")
        self.test_reading_button.click()

    def test_dailyBook(self):

        self.test_click_onListening()
        self.play_the_button.click()
        sleep(10)
        self.switch_reading = self.driver.find_element(by=AppiumBy.XPATH,
                                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[8]")
        self.switch_reading.click()
        # self.switch_reading = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[8]")
        # self.switch_reading.click()
        sleep(5)
        self.reading_screen = self.driver.find_element(by=AppiumBy.XPATH,
                                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]")
        assert self.reading_screen.is_displayed(), "The screen did not display after clicking the button."

        # HomeScreen.test_drivingMode.TestDRivingModee.test_drivingMode(self)
        sleep(5)

    # def test_nextChapter(self):
    #     self.test_click_onListening()
    #     self.nextChapter = self.driver.find_element(by=AppiumBy.XPATH,
    #                                                 value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[3]")
    #     self.nextChapter.click()
    #     sleep(8)

    # def test_add_toFavourite(self):
    #     self.test_clickOnTheDailyBook()
    #     self.ThreeDotOption = self.driver.find_element(by=AppiumBy.XPATH,
    #                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[1]")
    #     self.ThreeDotOption.click()
    #     sleep(2)
    #     self.AddTo_fav = self.driver.find_element(by=AppiumBy.XPATH,
    #                                               value="/hierarchy/android.view.ViewGroup/android.view.View/android.view.View/android.view.View[1]")
    #     self.AddTo_fav.click()
    #     sleep(5)
    # def test_download(self):
    #     self.test_clickOnTheDailyBook()
    #     self.Download = self.driver.find_element(by=AppiumBy.XPATH, value=
    #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[9]")
    #     self.Download.click()
    #     sleep(5)
    #     self.isDownloading = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ProgressBar")
    #     assert self.isDownloading.is_displayed(), "The book wasn't downloaded."
    #     sleep(10)
    #     self.downloaded = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[9]")))
    #     self.assertTrue(self.downloaded.is_displayed(), "it's not downloaded try again")
    #     sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


