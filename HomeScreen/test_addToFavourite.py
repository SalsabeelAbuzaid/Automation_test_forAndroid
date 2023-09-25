import unittest
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.connectiontype import ConnectionType
import HomeScreen.test_daily_content



class TestDownloadBooks(HomeScreen.test_daily_book.TestDailybook):
    def test_add_toFavourite(self):
        HomeScreen.test_daily_book.TestDailybook.test_clickOnTheDailyBook(self)
        self.ThreeDotOption = self.driver.find_element(by=AppiumBy.XPATH,
                                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[1]")
        self.ThreeDotOption.click()
        sleep(2)
        self.AddTo_fav = self.driver.find_element(by=AppiumBy.XPATH,
                                                  value="/hierarchy/android.view.ViewGroup/android.view.View/android.view.View/android.view.View[1]")
        self.AddTo_fav.click()
        sleep(5)

    #     add assertion for the success msg when they add id to ti
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()