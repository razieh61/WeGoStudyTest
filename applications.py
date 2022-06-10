import unittest
import wegostudy_locators as locators
import wegostudy_methods as methods


class ApplicationsTestCases(unittest.TestCase):

    @staticmethod
    def test_all_applications():
        methods.log_in()
        methods.all_applications()
        methods.log_out()