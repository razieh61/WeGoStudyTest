import unittest

# import your test modules
import update_profile
import negative_login
import applications
import student
import create_application
import setup
import teardown

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(setup))
suite.addTests(loader.loadTestsFromModule(update_profile))
suite.addTests(loader.loadTestsFromModule(applications))
suite.addTests(loader.loadTestsFromModule(student))
suite.addTests(loader.loadTestsFromModule(create_application))
suite.addTests(loader.loadTestsFromModule(negative_login))
suite.addTests(loader.loadTestsFromModule(teardown))

# initialize a runner, pass it your suite and run it
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)