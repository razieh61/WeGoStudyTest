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
    def test_WeGoStudy():  # test_ in the name is mandatory
        """test edit profile"""
        methods.log_in()
        methods.update_profile()
        methods.log_out()


    # @staticmethod
    # def test_z():
    #     """test create new student"""
    #     methods.log_in()
    #     methods.create_new_student()
    #     methods.log_out()


