import unittest
import wegostudy_locators as locators
import wegostudy_methods as methods


class TeardownTestCases(unittest.TestCase):

    @staticmethod  # signal to unittest that this is a function inside class (vs @classmethod)
    def test_teardown():  # test_ in the name is mandatory
        methods.tearDown()

