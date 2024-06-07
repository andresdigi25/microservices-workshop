import unittest, os

from libraries import selenium_env_local
from libraries import selenium_env


class EnvironmentSetup(unittest.TestCase):
    def setUp(self):
        execution_type = os.environ.get("EXECUTION_TYPE")
        if execution_type.upper() == "LOCAL":
            self.driver = selenium_env_local.createEnvironment()
        elif execution_type.upper() == "REMOTE":
            self.driver = selenium_env.createEnvironment()
        else:
            raise Exception("Environment variable EXECUTION_TYPE is not set")
        self.driver.maximize_window()
        return self.driver

    def tearDown(self):
        self.driver.quit()
