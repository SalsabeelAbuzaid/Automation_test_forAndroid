from appium import webdriver
from appium.options.android import UiAutomator2Options

desired_cap = {
    # 'uiautomator2ServerInstallTimeout': 120000,
    # 'adbExecTimeout': 120000,
    "appium:platformName": "Android",
    "appium:deviceName": "Pixel 6 Pro API 29",
    "appium:automationName": "UiAutomator2",
    "appium:platformVersion": "10.0",
    "appium:app": "C:\\Users\\salsa\\Downloads\\app-release 15.apk",
    "appium:appPackage": "com.faylasof.android.waamda",
    "appium:noReset": True,
    "appium:locale": "JO",
    "appium:language": "en",
    "appium:unicodeKeyboard": True,
    "appium:resetKeyboard": True,
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
}


def create_appium_driver():
    return webdriver.Remote(
        'http://localhost:4723/wd/hub', options=UiAutomator2Options().load_capabilities(desired_cap))
