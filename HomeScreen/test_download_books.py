import unittest
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.connectiontype import ConnectionType
import HomeScreen.test_daily_content
import Login_Signup.test_Login
# import HomeScreen.test_daily_book
from Config import config
from selenium.common.exceptions import NoSuchElementException


class TestDownloadBooks(unittest.TestCase):

    def setUp(self):
        self.driver = config.create_appium_driver()
        self.driver.implicitly_wait(30)

    def test_download(self):
        # self.Listen_daily_book = self.driver.find_element(by=AppiumBy.XPATH,
        #                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]")
        # self.Listen_daily_book.click()

        try:
            Login_Signup.test_Login.TestLogin.test_Login_BYEmail(self)
        except NoSuchElementException:
            pass

        sleep(10)
        self.Download = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[8]")
        self.Download.click()
        sleep(20)
        self.isDownloading = self.driver.find_element(by=AppiumBy.XPATH,
                                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.widget.ProgressBar")
        assert self.isDownloading.is_displayed(), "The book wasn't downloaded."
        sleep(30)

        self.downloaded = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[8]")))
        self.assertTrue(self.downloaded.is_displayed(), "it's not downloaded try again")
        sleep(5)

        # # turn off the internet
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        self.driver.launch_app()
        self.Downloaded_books = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
        ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
        "1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View"
        "/android.view.View[2]/android.view.View/android.widget.Button")
        self.Downloaded_books.click()

        sleep(2)

        self.choose_downloaded_book = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
        ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
        "1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View"
        "/android.view.View[3]/android.view.View/android.view.View")
        self.choose_downloaded_book.click()
        sleep(5)
        self.play_the_book = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
        ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
        ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[4]")
        self.play_the_book.click()
        sleep(15)
        self.switch_reading = self.driver.find_element(by=AppiumBy.XPATH,
                                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[8]")
        self.switch_reading.click()
        self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        self.driver.launch_app()
        sleep(7)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()