import unittest
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import HomeScreen.test_daily_book
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestCuratedList(HomeScreen.test_daily_book.TestDailybook):

    def test_curatedList(self):
        sleep(5)
        action = TouchAction(self.driver)
        for i in range(3):
            action.press(x=500, y=2500).move_to(x=500, y=1000).release().perform()
            sleep(4)
        self.showMore = self.driver.find_element(by=AppiumBy.XPATH,
                                                 value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[3]/android.widget.Button")
        self.showMore.click()
        sleep(3)
        for i in range(2):
            action.press(x=500, y=2500).move_to(x=500, y=1000).release().perform()
            sleep(4)
        self.curated_list = self.driver.find_element(by=AppiumBy.XPATH,
                                                     value=
                                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View[6]")
        self.curated_list.click()
        sleep(5)
        action = TouchAction(self.driver)

        action.press(x=500, y=2500).move_to(x=500, y=1000).release().perform()
        sleep(4)

        self.pick_book = self.driver.find_element(by=AppiumBy.XPATH,
                                                  value=
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]")
        self.pick_book.click()

        sleep(5)
        self.play = self.driver.find_element(by=AppiumBy.XPATH,
                                             value=
                                             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                             ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
                                             ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[4]")
        self.play.click()

        sleep(10)

        self.driver.back()
        sleep(2)
        action = TouchAction(self.driver)
        action.press(x=500, y=2500).move_to(x=500, y=1000).release().perform()
        sleep(5)

        self.pick_book = self.driver.find_element(by=AppiumBy.XPATH,
                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]")
        self.pick_book.click()
        sleep(5)
        self.assertTrue(self.pick_book, "didn't open the book")
        sleep(2)

    def test_shareCuratedList(self):
        WebDriverWait(self.driver, 10)
        action = TouchAction(self.driver)
        for i in range(3):
            action.press(x=500, y=2500).move_to(x=500, y=1000).release().perform()
            sleep(4)
        # self.test_curatedList()
        self.choose_curatedList = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[4]/android.view.View[1]")
        self.choose_curatedList.click()
        sleep(5)
        self.shareList = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.Button[2]").click()

        sleep(6)
        self.popupShareMsg = WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.ID, "android:id/contentPanel")))
        # self.driver.switch_to.context(self.popupShareMsg)
        self.assertTrue(self.popupShareMsg.is_displayed())
        sleep(2)

        # this to exit from the screen
        self.driver.back()

        self.back = self.driver.find_element(by=AppiumBy.XPATH,
                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.Button[1]")
        self.back.click()
        sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
