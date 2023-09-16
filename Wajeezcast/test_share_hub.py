import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import test_wajeezcast
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import Wajeezcast.test_wajeezcast


# from android.media import MediaPlayer

class TestWajeezcastShareHub(Wajeezcast.test_wajeezcast.TestWajeezcast):

    def test_shareHub(self):
        WebDriverWait(self.driver, 10)
        test_wajeezcast.TestWajeezcast.test_wajeezcastclick(self)
        self.choose_hup = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
        ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
        "1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View"
        "/android.widget.ScrollView/android.view.View[2]/android.view.View[1]").click()
        sleep(5)
        self.shareHup = self.driver.find_element(by=AppiumBy.XPATH, value=
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
        ".widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
        "1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view"
        ".View/android.view.View/android.widget.Button[2]").click()

        sleep(6)
        self.popupShareMsg = WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.XPATH,
                                                                                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ViewPager/android.widget.RelativeLayout/com.android.internal.widget.RecyclerView/android.widget.LinearLayout[3]")))
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
