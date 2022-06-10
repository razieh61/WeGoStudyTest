import unittest
import wegostudy_locators as locators
import wegostudy_methods as methods


class CreateApplicationTestCases(unittest.TestCase):

    @staticmethod
    def test_std_application():
        methods.log_in()
        methods.create_application()
        methods.log_out()