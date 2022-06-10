import unittest
import wegostudy_locators as locators
import wegostudy_methods as methods


class ApplicationsTestCases(unittest.TestCase):

    @staticmethod
    def test_student():
        methods.log_in()
        methods.create_new_student()
        methods.view_details_of_student()
        methods.log_out()