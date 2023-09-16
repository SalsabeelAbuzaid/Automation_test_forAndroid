import unittest
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait

# from android.media import MediaPlayer
import Wajeezcast.test_wajeezcast


class TestLatestReleases(Wajeezcast.test_wajeezcast.TestWajeezcast):


    def test_scrollUp(self):
        WebDriverWait(self.driver, 5)
        Wajeezcast.test_wajeezcast.TestWajeezcast.test_wajeezcastclick(self)
        # this is to scroll down
        # action = TouchAction(self.driver)
        # action.press(x=500, y=1000).move_to(x=500, y=2000).release().perform()
        sleep(3)
        action = TouchAction(self.driver)
        action.press(x=500, y=2500).move_to(x=500, y=1000).release().perform()
        sleep(5)
        self.choose_episodes = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
        ".widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
        "1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view"
        ".View/android.widget.ScrollView/android.view.View[2]").click()
        sleep(10)

        self.playTheEpisode = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
        ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
        ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[4]").click()

        sleep(10)
        self.driver.back()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
