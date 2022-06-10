import unittest
import wegostudy_locators as locators
import wegostudy_methods as methods


class NegativeLoginTestCases(unittest.TestCase):

    @staticmethod  # signal to unittest that this is a function inside class (vs @classmethod)
    def test_negative_Login():  # test_ in the name is mandatory
        methods.negative_login_test()
