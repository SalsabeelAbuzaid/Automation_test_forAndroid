
import unittest
from Wajeezcast.test_latestReleases import TestLatestReleases
from Wajeezcast.test_episodeWajeezcast import TestEpisodes
from Wajeezcast.test_share_hub import TestWajeezcastShareHub

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromTestCase(TestEpisodes))
suite.addTests(loader.loadTestsFromTestCase(TestWajeezcastShareHub))
suite.addTests(loader.loadTestsFromTestCase(TestLatestReleases))
if __name__ == '__main__':
    unittest.main()
# # from test_login_email import TestLogin
# # from test_wajeezcast import TestWjeezcast
# #
# # if __name__ == '__main__':
# #     suite = unittest.TestSuite()
# #     suite.addTest(TestLogin('test_login'))
# #     suite.addTest(TestWjeezcast('test_wajeezcast'))
# #     # suite.addTest(TestCase2('test_case_2'))
# #
# #     # run the test suite
# #     runner = unittest.TextTestRunner(verbosity=2)
# #     runner.run(suite)
#
# # if __name__ == '__main__':
# #     suite = unittest.TestSuite()
# #     suite.addTest(TestLogin('test_login'))
# #     suite.addTest(TestWjeezcast('test_reading_book'))
# #     runner = unittest.TextTestRunner(verbosity=2)
# #     runner.run(suite)
#
# # from appium import webdriver
# #
# #
# #
# # class TestSuite(unittest.TestSuite):
# #     def Testsuitee(self):
# #
# #         suite = unittest.TestSuite()
# #         suite.addTest(TestLogin())
# #         suite.addTest(TestWjeezcast())
# #         return suite
# #
# #
#
# #
# #     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities={"platformName": "Android",
# #                                                                                     "appium:deviceName": "Pixel 6 Pro API 29",
# #                                                                                     "appium:automationName": "UiAutomator2",
# #                                                                                     "appium:platformVersion": "11.0",
# #                                                                                     "appium:app": "C:\\Users\\salsa\\Downloads\\app-debug (4).apk",
# #                                                                                     "appium:appPackage": "com.faylasof.android.waamda"})
# #     suite = unittest.TestSuite()
# #     suite.addTest(TestLogin())
# #     suite.addTest(TestWjeezcast())
# #     unittest.TextTestRunner(verbosity=2).run(suite)
# #
# #     driver.quit()
# #     unittest.main()
# import unittest
# from test_login_email import TestLogin
# from test_wajeezcast import TestWjeezcast
#
# class MyTestSuite(unittest.TestSuite):
#     def suite(self):
#         test_suite = unittest.TestSuite()
#
#         test_suite.addTest(unittest.TestLoader.loadTestsFromTestCase(TestLogin))
#         test_suite.addTest(unittest.TestLoader.loadTestsFromTestCase(TestWjeezcast))
#
#         return test_suite
#
# if __name__ == '__main__':
#     unittest.TextTestRunner(verbosity=2).run(MyTestSuite().suite())
