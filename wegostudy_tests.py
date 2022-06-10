import unittest
import wegostudy_locators as locators
import wegostudy_methods as methods


class WeGoStudyTestCases(unittest.TestCase):

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

    @staticmethod
    def test_5negative_Login():
        """negative login test """
        methods.negative_login_test()

    @staticmethod
    def test_4std_application():
        """test create application"""
        methods.log_in()
        methods.create_application()
        methods.log_out()

    @staticmethod
    def test_3student():
        """test student"""
        methods.log_in()
        methods.create_new_student()
        methods.view_details_of_student()
        methods.log_out()

    @staticmethod  # signal to unittest that this is a function inside class (vs @classmethod)
    def test_2all_applications():
        # """test all applications"""
        methods.log_in()
        methods.all_applications()
        methods.log_out()

    @staticmethod  # signal to unittest that this is a function inside class (vs @classmethod)
    def test_1update_profile():  # test_ in the name is mandatory
        # """test edit profile"""
        methods.log_in()
        methods.update_profile()
        methods.log_out()


