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

# Create a test loader
loader = unittest.TestLoader()

# Create a test suite
suite = unittest.TestSuite()

# Add test cases (test classes) to the suite
suite.addTests(loader.loadTestsFromTestCase(TestLogin))
suite.addTests(loader.loadTestsFromTestCase(TestSignUp))
suite.addTests(loader.loadTestsFromTestCase(TestDailybook))

# Run the test suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite)
