import time
from libraries import mapping, mouse, forms
from selenium.webdriver.common.alert import Alert


class ShoppingCart:

    def __init__(self, driver):
        self.driver = driver
        self.item_button = "//a[contains(text(),'{}')]"
        self.add_car_button = "//a[contains(text(),'Add to cart')]"
        self.car_button = "//*[@id='cartur']"
        self.place_order_button = "//*[@id='page-wrapper']/div/div[2]/button"
        self.name = "//*[@id='name']"
        self.country = "//*[@id='country']"
        self.city = "//*[@id='city']"
        self.credit_card = "//*[@id='card']"
        self.month = "//*[@id='month']"
        self.year = "//*[@id='year']"
        self.purchase_button = "//*[@id='orderModal']/div/div/div[3]/button[2]"

    def click_on_product(self, product_name: str):
        mouse.click_on_element(self, "XPATH", self.item_button.format(product_name))

    def click_on_add_to_cart(self):
        mouse.click_on_element(self, "XPATH", self.add_car_button)
        Alert(self.driver).accept()
        # forms.press_enter()
        time.sleep(5)

    def click_on_car_option(self):
        mouse.click_on_element(self, "XPATH", self.car_button)

    def place_order_option(self):
        mouse.click_on_element(self, "XPATH", self.place_order_button)

    def purchase(self, name, country, city, credit_card, month, year):
        forms.enter_text_on_element(self, "XPATH", self.name, name)
        forms.enter_text_on_element(self, "XPATH", self.country, country)
        forms.enter_text_on_element(self, "XPATH", self.city, city)
        forms.enter_text_on_element(self, "XPATH", self.credit_card, credit_card)
        forms.enter_text_on_element(self, "XPATH", self.month, month)
        forms.enter_text_on_element(self, "XPATH", self.year, year)
        mouse.click_on_element(self, "XPATH", self.purchase_button)
