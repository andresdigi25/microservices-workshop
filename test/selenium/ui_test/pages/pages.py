import time
from libraries import mapping, mouse, forms


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.user_txt = "//*[@name='Username']"
        self.user_password_txt = "//*[@name='passwords']"
        self.sign_in_button = "//*[@role='button']"
        self.app_b = "//*[@href='/app-b/home']"
        self.app_c = "//*[@href='/app-c/home']"

    def load(self):
        url = mapping.map_environment()
        self.driver.get(url)

    def type_user_name(self, name):
        time.sleep(2)
        forms.enter_text_on_element(self, "XPATH", self.user_txt, name)

    def type_password(self, password):
        forms.enter_text_on_element(self, "XPATH", self.user_password_txt, password)

    def click_on_sign_in_button(self):
        mouse.click_on_element(self, "XPATH", self.sign_in_button)

    def click_on_app_b(self):
        mouse.click_on_element(self, "XPATH", self.app_b)

    def click_on_app_c(self):
        mouse.click_on_element(self, "XPATH", self.app_c)

