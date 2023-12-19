# import unittest
# from Login_Signup import test_Login
# from Login_Signup import test_sign_up
#
# loader = unittest.TestLoader()
# suite = unittest.TestSuite()
# suite.addTests(loader.loadTestsFromTestCase(test_Login.TestLogin.test_login(self)))
# suite.addTests(loader.loadTestsFromTestCase(test_sign_up.TestSignUp))
# if __name__ == '__main__':
#     unittest.main()
import unittest
from Login_Signup.test_Login import TestLogin
from Login_Signup.test_sign_up import TestSignUp
from HomeScreen.test_daily_content import TestDailybook

class Suite(unittest.TestCase):
    def suite_test(self):
# Create a test loader
        loader = unittest.TestLoader()

        # Create a test suite
        suite = unittest.TestSuite()

        # Add test cases (test classes) to the suite
        # suite.addTests(loader.loadTestsFromTestCase(TestLogin.test_enter_the_password(self)))
        # suite.addTests(loader.loadTestsFromTestCase(TestSignUp))
        # suite.addTests(loader.loadTestsFromTestCase(TestDailybook))
        # suite.addTest(TestLogin('test_enter_the_password'))4
        TestLogin().test_enter_the_password()
        # return suite

if __name__ == '__main__':
    unittest.main()
    # runner = unittest.TextTestRunner(verbosity=2)
    # suite = Suite().suite_test()
    # runner.run(suite)