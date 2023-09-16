import unittest
from test_login_email import TestStringMethods
from Login_Signup.test_sign_up import TestSignUp

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromTestCase(TestStringMethods))
suite.addTests(loader.loadTestsFromTestCase(TestSignUp))
if __name__ == '__main__':
    unittest.main()


