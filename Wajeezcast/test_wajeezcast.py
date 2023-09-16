from time import sleep
import unittest
from appium import webdriver
import vlc
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# from android.media import MediaPlayer


from appium.webdriver.common.touch_action import TouchAction

import Wajeezcast.test_login_email


class TestWajeezcast(unittest.TestCase):
    desired_cap = {
  "platformName": "Android",
  "appium:deviceName": "Pixel 6 Pro API 29",
  "appium:automationName": "UiAutomator2",
  "appium:platformVersion": "10.0",
  "appium:app": "C:\\Users\\salsa\\Downloads\\app-debug (6).apk",
  "appium:appPackage": "com.faylasof.android.waamda",
  "appium:noReset": True
}


    def setUp(self):
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', self.desired_cap)
        self.driver.implicitly_wait(30)
        self.driver.setSetting("driver", "compose")

        wait = WebDriverWait(self.driver, 10)
        Wajeezcast.test_login_email.TestLogin.test_login(self)

        sleep(2)
    def test_wajeezcastclick(self):

        sleep(3)
        self.wajeezcast = self.driver.find_element(by=AppiumBy.ID, value="com.faylasof.android.waamda:id/navigation_graph_wajeez_cast")
        self.wajeezcast.click()
        sleep(5)

    # def test_shareHub(self):
    #
    #     self.wajeezcastclick()
    #     self.choose_hup = self.driver.find_element(by=AppiumBy.XPATH, value=
    #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
    #     ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
    #     "1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View"
    #     "/android.widget.ScrollView/android.view.View[2]/android.view.View[1]").click()
    #     sleep(5)
    #     self.shareHup = self.driver.find_element(by=AppiumBy.XPATH, value=
    #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
    #     ".widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
    #     "1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view"
    #     ".View/android.view.View/android.widget.Button[2]").click()
    #
    #     sleep(6)
    #     self.popupShareMsg = WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.XPATH,
    #                                                                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ViewPager/android.widget.RelativeLayout/com.android.internal.widget.RecyclerView/android.widget.LinearLayout[3]")))
    #     # self.driver.switch_to.context(self.popupShareMsg)
    #     self.assertTrue(self.popupShareMsg.is_displayed())
    #     sleep(2)
    #
    #     # this to exit from the screen
    #     self.driver.back()
    #
    #     self.back = self.driver.find_element(by=AppiumBy.XPATH,
    #                                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.Button[1]")
    #     self.back.click()
    #     sleep(3)
    #
    # def test_choose_episodes(self):
    #     # self.wajeezcast = self.driver.find_element(by=AppiumBy.ID,
    #     #                                            value="com.faylasof.android.waamda:id/navigation_graph_wajeez_cast")
    #     # self.wajeezcast.click()
    #     # sleep(4)
    #     self.wajeezcastclick()
    #     self.choose_episodes = self.driver.find_element(by=AppiumBy.XPATH, value=
    #         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
    #         ".widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
    #         "1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view"
    #         ".View/android.widget.ScrollView/android.view.View[3]").click()
    #     sleep(5)
    #
    #     self.playTheEpisode = self.driver.find_element(by=AppiumBy.XPATH, value=
    #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
    #     ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
    #     ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[4]").click()
    #
    #     sleep(10)
    #
    #     self.driver.back()
    #
    #     sleep(8)
    # def test_scrollUp(self):
    #     # this is to scroll down
    #     # action = TouchAction(self.driver)
    #     # action.press(x=500, y=1000).move_to(x=500, y=2000).release().perform()
    #     self.wajeezcastclick()
    #     action = TouchAction(self.driver)
    #     action.press(x=500, y=2500).move_to(x=500, y=1000).release().perform()
    #     sleep(5)
    #     self.choose_episodes = self.driver.find_element(by=AppiumBy.XPATH, value=
    #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
    #     ".widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
    #     "1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view"
    #     ".View/android.widget.ScrollView/android.view.View[2]").click()
    #     sleep(10)
    #
    # def test_add_toFavourite(self):
    #     self.test_choose_episodes()
    #     self.ThreeDotOption = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[1]")
    #     self.ThreeDotOption.click()
    #     sleep(5)
    #     self.AddTo_fav = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.view.ViewGroup/android.view.View/android.view.View/android.view.View[1]")
    #     self.AddTo_fav.click()
    #
    #     # there's no xpath for the success msg at the meanwhile we will activate the code as soon we find an id or
    #     # something self.SuccessMsg = self.driver.find_element(by=AppiumBy.XPATH, value="") self.assertTrue(
    #     # self.SuccessMsg.is_displayed()) self.SuccessMsg = WebDriverWait(self.driver, 20).until(
    #     # EC.presence_of_element_located((By.XPATH,
    #     # value="")
    #     # self.SuccessMsg.is_displayed()



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    # def choose_Episodes(self):
    #     # it will work when they but unique id for the play and pause button
    #     self.choose_episodes = self.driver.find_element(by=AppiumBy.XPATH, value=
    #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
    #     ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
    #     "1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View"
    #     "/android.widget.ScrollView/android.view.View[3]").click()
    #     sleep(5)
    #     self.player_already_working = self.driver.find_element(by=AppiumBy.XPATH,
    #                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[4]").is_playing()
    #     if self.player_already_working:
    #         # Player is already playing, no need to click on the button
    #         print("Player is already playing")
    #     else:
    #         # Player is not playing, click on the button to start playing
    #         play_button = self.driver.find_element(by=AppiumBy.XPATH,
    #                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[4]")
    #         play_button.click()
    #         sleep(5)  # Wait for player to start playing
    #         # Check if player is now playing
    #         self.player_already_working = self.driver.find_element(by=AppiumBy.XPATH,
    #                                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.Button[4]").is_playing()
    #
    #         self.assertTrue(self.player_already_working, "Player should be playing now")