import re
import unittest
from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


class TestLogin(unittest.TestCase):
    desired_cap = {
        'uiautomator2ServerInstallTimeout': 120000,
        'adbExecTimeout': 120000,
        "appium:platformName": "Android",
        "appium:deviceName": "Pixel 6 Pro API 29",
        "appium:automationName": "UiAutomator2",
        "appium:platformVersion": "10.0",
        "appium:app": "C:\\Users\\salsa\\Downloads\\app-debug (16).apk",
        "appium:appPackage": "com.faylasof.android.waamda",
        # "appium:noReset": True,
        "appium:locale": "JO",
        "appium:language": "en",
        "appium:unicodeKeyboard": True,
        "appium:resetKeyboard": True,
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True}

    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                       options=UiAutomator2Options().load_capabilities(caps=self.desired_cap))
        self.driver.implicitly_wait(30)

    def test_EnterEmail(self):
        self.element_loginByEmail = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                             value='new UiSelector().resourceId("email_login_button")')
        self.element_loginByEmail.click()
        self.driver.implicitly_wait(5)

        self.enter_email = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                    value='new UiSelector().resourceId("email_text_field")')
        self.enter_email.click()
        self.enter_email.clear()
        self.email = "sl@testwajeez.co"
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
