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


class TestDailybook(Login_Signup.test_Login.TestLogin):
    desired_cap = {"platformName": "Android",
                   "appium:deviceName": "Pixel 6 Pro API 29",
                   "appium:automationName": "UiAutomator2",
                   "appium:platformVersion": "10.0",
                   "appium:app": "C:\\Users\\salsa\\Downloads\\app-debug (16).apk",
                   "appium:appPackage": "com.faylasof.android.waamda",
                   # "appium:noReset": True,
                   "appium:locale": "JO",
                   "appium:language": "en",
                   "appium:unicodeKeyboard": True,
                   "appium:resetKeyboard": True,
                   "appium:ensureWebviewsHavePages": True,
                   "appium:nativeWebScreenshot": True,
                   "appium:newCommandTimeout": 3600,
                   "appium:connectHardwareKeyboard": True
                   }

    def setUp(self):
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', self.desired_cap)
        self.driver.implicitly_wait(30)
        self.driver.setSetting("driver", "compose")

        WebDriverWait(self.driver, 10)
        Login_Signup.test_Login.TestLogin.test_login(self)

    def test_click_onListening(self):

        sleep(5)
        try:
            if self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.TextView[1]").is_displayed():
                raise AssertionError("it's not a freemium user")
        except NoSuchElementException:
            pass
        except AssertionError as E:
            raise E
        sleep(2)
        # Listen to the daily book
        self.Listen_daily_book = self.driver.find_element(by=AppiumBy.XPATH,
                                                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[4]")
        self.Listen_daily_book.click()

        self.progress_bar_running = self.driver.find_element(by=AppiumBy.XPATH,
                                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[2]")
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[3]"
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[3]"
        sleep(10)
    def test_dailyBook(self):

        self.test_click_onListening()
        self.play_the_button = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[4]")
        self.play_the_button.click()
        sleep(10)
        self.switch_reading = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[8]")
        self.switch_reading.click()
        # self.switch_reading = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[8]")
        # self.switch_reading.click()
        sleep(5)
        self.reading_screen = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]")
        assert self.reading_screen.is_displayed(), "The screen did not display after clicking the button."

        # HomeScreen.test_drivingMode.TestDRivingModee.test_drivingMode(self)
        sleep(5)

    def test_nextChapter(self):
        self.test_click_onListening()
        self.nextChapter = self.driver.find_element(by=AppiumBy.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[3]")
        self.nextChapter.click()
        sleep(8)

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


