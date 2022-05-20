import unittest
import wegostudy_locators as locators
import wegostudy_methods as methods


class WeGoStudyPositiveTestCases(unittest.TestCase):

    @staticmethod  # signal to unittest that this is a function inside class (vs @classmethod)
    def test_WeGoStudy():  # test_ in the name is mandatory
        methods.setUp()
        methods.log_in()
        methods.create_new_student()
        methods.log_out()
        methods.tearDown()
