import re
import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
# from test_daily_book import TestDailybook
# from test_wajeezcast import TestWajeezcast

import os


# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class TestLogin(unittest.TestCase):

    desired_cap = {
  "platformName": "Android",
  "appium:deviceName": "Pixel 6 Pro API 29",
  "appium:automationName": "UiAutomator2",
  "appium:platformVersion": "11.0",
  "appium:app": "C:\\Users\\salsa\\Downloads\\644.apk",
  "appium:appPackage": "com.faylasof.android.waamda",
        "noReset": True,
  # "appium:forceEspressoRebuild": true
}

    def setUp(self):

        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', self.desired_cap)
        self.driver.implicitly_wait(30)
        self.driver.setSetting("driver", "compose")

    def test_login(self):

        self.element_login = self.driver.find_element(by=AppiumBy.XPATH,
                                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                                            ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
                                                            ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
                                                            ".ScrollView/android.view.View[3]/android.widget.Button")
        self.element_login.click()
        self.driver.implicitly_wait(10)

        self.enter_email = self.driver.find_element(by=AppiumBy.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                                          ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
                                                          ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
                                                          ".ScrollView/android.view.View[1]/android.widget.EditText")
        self.enter_email.click()
        self.enter_email.clear()
        self.email = "fe@fe.fe"
            # "ad@ad.ad"
            # "yousals123@gmail.com"
        self.enter_email.send_keys(self.email)
        pat = re.compile(r"^\S+@\S+\.\S+$")
        self.result = re.match(pat, self.email)
        if self.result:
            print("valid email")
        else:
            print("not valid")
        assert self.result, "invalid email"
        print(self.email)
        sleep(2)
        self.enter_pass = self.driver.find_element(by=AppiumBy.XPATH,
                                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                                         ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
                                                         ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
                                                         ".ScrollView/android.view.View[2]/android.widget.EditText")

        self.enter_pass.click()
        self.enter_pass.clear()
        sleep(2)
        self.password = "fefefefe"
            # "adadadad"
            # "Year.329"

        self.enter_pass.send_keys(self.password)
        sleep(2)
        valid_pass = re.compile(r"[A-Za-z0-9@#$%^.&+=]{8,}")
        pass_result = re.match(valid_pass, self.password)
        print(pass_result)
        if pass_result:
            print("match")
        else:
            print("not match")
        sleep(2)
        assert pass_result, "invalid pass"
        self.show_pass = self.driver.find_element(by=AppiumBy.XPATH,
                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                                        ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
                                                        ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget"
                                                        ".ScrollView/android.view.View[2]/android.widget.EditText/android.view.View/android.widget.Button")
        self.show_pass.click()

        sleep(2)

        self.Login = self.driver.find_element(by=AppiumBy.XPATH,
                                              value="/hierarchy/android.widget.FrameLayout/android.widget"
                                                    ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                    ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup"
                                                    "/android.widget.FrameLayout/android.widget.FrameLayout/androidx"
                                                    ".compose.ui.platform.ComposeView/android.view.View/android.view"
                                                    ".View/android.widget.ScrollView/android.view.View["
                                                    "3]/android.widget.Button")
        self.Login.click()
        sleep(10)

    # def test_success(self):

        self.home_screen = self.driver.find_element(by=AppiumBy.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.ScrollView")
        self.assertTrue(self.home_screen.is_displayed(), "HomeScreen not displayed after login")
        sleep(8)



    # def tearDown(self):
    #     self.driver.quit()
    #     test_wajeezcast.TestWjeezcast.test_wajeezcast(self)

if __name__ == '__main__':
    # loader = unittest.TestLoader()
    # suite = unittest.TestSuite()
    # suite.addTests(loader.loadTestsFromTestCase(TestDailybook))
    # suite.addTests(loader.loadTestsFromTestCase(TestWajeezcast))
    unittest.main()

