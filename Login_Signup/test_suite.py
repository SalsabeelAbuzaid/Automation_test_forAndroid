import unittest
from test_Login import TestLogin
from test_sign_up import TestSignUp

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromTestCase(TestLogin))
suite.addTests(loader.loadTestsFromTestCase(TestSignUp))
if __name__ == '__main__':
    unittest.main()
