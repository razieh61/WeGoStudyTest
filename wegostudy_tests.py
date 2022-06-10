import unittest
import wegostudy_locators as locators
import wegostudy_methods as methods


class WeGoStudyPositiveTestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        methods.setUp()

    @classmethod
    def tearDownClass(cls):
        methods.tearDown()

    def setUp(self) -> None:
        print('\n ===== Test started :', self.shortDescription())

    def tearDown(self) -> None:
        print('\n ===== Test finished :', self.shortDescription())

    @staticmethod  # signal to unittest that this is a function inside class (vs @classmethod)
    def test1_WeGoStudy():  # test_ in the name is mandatory
        """test edit profile"""
        methods.log_in()
        methods.update_profile()
        methods.log_out()

    @staticmethod
    def test2_WeGoStudy():
        """test student"""
        methods.log_in()
        methods.create_new_student()
        methods.view_details_of_student()
        methods.log_out()

    @staticmethod
    def test4_WeGoStudy():
        """test application"""
        methods.log_in()
        methods.create_application()
        methods.log_out()

    @staticmethod
    def test3_WeGoStudy():
        """negative login test """
        methods.negative_login_test()

