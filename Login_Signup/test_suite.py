# import unittest
# from Login_Signup import test_Login
# from Login_Signup import test_sign_up
from unittest import TestSuite

from Listening_Player.test_addToPlayList import TestAddToPlayList
# from unittest_parallel import TestSuite
import concurrent.futures
# loader = unittest.TestLoader()
# suite = unittest.TestSuite()
# suite.addTests(loader.loadTestsFromTestCase(test_Login.TestLogin.test_login(self)))
# suite.addTests(loader.loadTestsFromTestCase(test_sign_up.TestSignUp))
# if __name__ == '__main__':
#     unittest.main()
import unittest
from Login_Signup.test_Login import TestLogin

# from Login_Signup.test_sign_up import TestSignUp
# from Listening_Player.test_addToPlayList import TestAddToPlayList

# class Suite(unittest.TestCase):
#     def suite_test(self):
# Create a test loader
if __name__ == '__main__':
    # Create a test suite
    suite = TestSuite()
    loader = unittest.TestLoader()

    # Create a test suite
    # suite = unittest.TestSuite()

    # Add test cases (test classes) to the suite
    suite.addTest(loader.loadTestsFromTestCase(TestAddToPlayList))
    # suite.addTests(loader.loadTestsFromTestCase(TestSignUp))
    # suite.addTests(loader.loadTestsFromTestCase(TestDailybook))
    # suite.addTest(TestLogin('test_enter_the_password'))
    # suite.addTest(TestAddToPlayList('test_AddDailyBookToPlayList'))
    # suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # TestLogin().test_enter_the_password()
    # return suite
    suite.run(parallel='processes', processes=2)
    # if __name__ == '__main__':
    #     unittest.main()
    #     runner = unittest.TextTestRunner(verbosity=2)
