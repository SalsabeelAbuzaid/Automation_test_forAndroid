import unittest
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.connectiontype import ConnectionType
import HomeScreen.test_daily_content
from selenium.common.exceptions import NoSuchElementException



class TestDownloadBooks(HomeScreen.test_daily_content.TestDailybook):
    def test_AddDailyBookToPlayList(self):
        HomeScreen.test_daily_content.TestDailybook.test_clickOnTheDailyBook(self)
        self.addToPlayList = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                             value='new UiSelector().resourceId("FeaturedContentAddToPlaylistButton")')
        self.addToPlayList.click()
        sleep(2)

        try:
            self.subscription_screen = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                          value='new UiSelector().resourceId("com.faylasof.android.waamda:id/coordinator")')
            self.addToPlayList.click()

        except NoSuchElementException:
            self.fail("The expected screen is not displayed.")