import unittest
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
import Login_Signup
from Config import config
from Listening_Player.test_Listening_reading import TestListeningReadingButton
from Login_Signup import test_Login
from appium.webdriver.common.appiumby import AppiumBy


class TestPlaybackAction(unittest.TestCase):

    def setUp(self):
        self.driver = config.create_appium_driver()
        self.driver.implicitly_wait(10)
        Login_Signup.test_Login.TestLogin.login_required(self)

    def test_next_previousCH(self):
        # verify the next button is clickable
        TestListeningReadingButton.click_on_listening(self)
        self.nextChapter = self.driver.find_element(by=AppiumBy.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.widget.Button[3]")
        self.nextChapter.click()
        sleep(8)

        # add the assertion after each button
        # self.chapterNumber = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH,
        #                                                                                         value = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[9]")))
        # self.assertTrue(self.chapter.is_displayed(), "it's not added to Favourite")
        # sleep(2)

        # verify the next previous button is clickable
        self.PreviousChapter = self.driver.find_element(by=AppiumBy.XPATH,
                                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.widget.Button[4]")
        self.PreviousChapter.click()
        sleep(8)

    # verify the forword button is clickable
    def test_forword_BackwordTen(self):
        TestListeningReadingButton.click_on_listening(self)
        self.forword = self.driver.find_element(by=AppiumBy.XPATH,
                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.widget.Button[2]")
        self.forword.click()
        sleep(2)

        # verify the backword button is clickable

        self.backword = self.driver.find_element(by=AppiumBy.XPATH,
                                                 value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView/android.widget.Button[5]")
        self.backword.click()
        sleep(8)
