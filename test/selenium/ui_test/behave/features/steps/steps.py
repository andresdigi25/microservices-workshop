import os, allure
from allure_commons.types import AttachmentType
from behave import given, when, then

from libraries import mapping
from ui_test.pages.pages import Login
from libraries.environment_setup import EnvironmentSetup

class LoginSteps(EnvironmentSetup):

    @given(u'Open the website')
    def step_impl(self):

        self.url = mapping.map_environment()
        self.driver.get(self.url)
        self.login = Login(self.driver)
        self.login.load()
        username = os.environ.get("USER_NAME")
        password = os.environ.get("PASSWORD")
        self.login.type_user_name(username)
        self.login.type_password(password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Credentials.png", attachment_type=AttachmentType.PNG)
        self.login.click_on_sign_in_button()
        allure.attach(self.driver.get_screenshot_as_png(), name="Goto_Login.png", attachment_type=AttachmentType.PNG)

    @when(u'Go to App b')
    def step_impl(self):
        self.login.click_on_app_b()
        allure.attach(self.driver.get_screenshot_as_png(), name="App_b.png", attachment_type=AttachmentType.PNG)

    @then(u'Go to App c')
    def step_impl(self):
        self.login.click_on_app_c()
        allure.attach(self.driver.get_screenshot_as_png(), name="App_c.png", attachment_type=AttachmentType.PNG)
