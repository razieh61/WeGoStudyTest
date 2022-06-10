import unittest
import wegostudy_locators as locators
import wegostudy_methods as methods


class UpdateProfileTestCases(unittest.TestCase):

    @staticmethod  # signal to unittest that this is a function inside class (vs @classmethod)
    def test_update_profile():  # test_ in the name is mandatory
        methods.log_in()
        methods.update_profile()
        methods.log_out()