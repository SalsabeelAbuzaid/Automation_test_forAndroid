import unittest
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
import Wajeezcast.test_episodeWajeezcast
# from android.media import MediaPlayer
import Wajeezcast.test_wajeezcast


class TestLatestReleases(Wajeezcast.test_wajeezcast.TestWajeezcast):


    def test_addToFavorite(self):
        WebDriverWait(self.driver, 5)
        Wajeezcast.test_episodeWajeezcast.TestEpisodes.test_choose_episodes(self)

        self.ThreeDotOption = self.driver.find_element(by=AppiumBy.XPATH,
                                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[1]")
        self.ThreeDotOption.click()
        sleep(2)
        self.AddTo_fav = self.driver.find_element(by=AppiumBy.XPATH,
                                                  value="/hierarchy/android.view.ViewGroup/android.view.View/android.view.View/android.view.View[1]")
        self.AddTo_fav.click()
        sleep(7)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()