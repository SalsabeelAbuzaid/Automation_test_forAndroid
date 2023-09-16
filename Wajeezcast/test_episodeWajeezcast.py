import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import Wajeezcast.test_wajeezcast
# import Wajeezcast.test_login_email
# from Login_Signup import test_Login

# from android.media import MediaPlayer
from appium.webdriver.connectiontype import ConnectionType

class TestEpisodes(Wajeezcast.test_wajeezcast.TestWajeezcast):

    def test_choose_episodes(self):
        WebDriverWait(self.driver, 10)
        Wajeezcast.test_wajeezcast.TestWajeezcast.test_wajeezcastclick(self)
        self.choose_episodes = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
        ".widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
        "1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view"
        ".View/android.widget.ScrollView/android.view.View[3]").click()
        sleep(5)

        self.playTheEpisode = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
        ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
        ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[4]").click()

        sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
