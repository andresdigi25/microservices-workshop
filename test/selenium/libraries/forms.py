import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from libraries import locators
from libraries import mouse
from datetime import datetime


# -----------------
# Text functions
# -----------------


def enter_text_on_element(self, locator_type, locator, value):
    time.sleep(0.5)
    element = locators.locator_element(self, locator_type, locator)
    locators.highlight(self, element)
    element.clear()
    element.send_keys(value)


def enter_text_press_enter(self, locator_type, locator, value):
    time.sleep(0.5)
    element = locators.locator_element(self, locator_type, locator)
    locators.highlight(self, element)
    element.clear()
    element.send_keys(value, Keys.ENTER)


def enter_text_press_enter_and_tab(self, locator_type, locator, value):
    time.sleep(0.5)
    element = locators.locator_element(self, locator_type, locator)
    locators.highlight(self, element)
    element.send_keys(value, Keys.ENTER)
    element.send_keys(value, Keys.TAB)


def enter_text_press_tab(self, locator_type, locator, value):
    time.sleep(0.5)
    element = locators.locator_element(self, locator_type, locator)
    locators.highlight(self, element)
    element.send_keys(value, Keys.TAB)


def get_text_on_element(self, locator_type, locator):
    time.sleep(0.5)
    element = locators.locator_element(self, locator_type, locator)
    locators.highlight(self, element)
    return element.text


def get_input_text(self, locator_type, locator):
    element = locators.locator_element(self, locator_type, locator)
    return element.get_attribute('value')


def upload_file(self, locator_type, locator, path):
    element = locators.locator_element(self, locator_type, locator)
    file_path = os.path.expanduser('~') + path
    element.send_keys(file_path)


def press_enter_txt(self, locator_type, locator):
    element = locators.locator_element(self, locator_type, locator)
    element.send_keys(Keys.ENTER)


def press_enter():
    var = Keys.ENTER


def press_arrow(self, locator_type, locator, key):
    element = locators.locator_element(self, locator_type, locator)
    if key == 1:
        arrow = Keys.ARROW_UP
    elif key == 2:
        arrow = Keys.ARROW_DOWN
    elif key == 3:
        arrow = Keys.ARROW_RIGHT
    elif key == 4:
        arrow = Keys.ARROW_LEFT
    else:
        raise Exception("Must define a number between 1 and 4 for the arrow key")
    element.send_keys(arrow)


# ------------------
# Tables driving
# ------------------


def get_information_of_table_columns(self, list_columns, generic_xpath):
    xpaths_columns = []
    columns_driver = []
    columns_list_with_information = []
    for number_column in list_columns:
        xpaths_columns.append(generic_xpath + "[" + str(number_column) + "]")
    for xpath_column in xpaths_columns:
        column = self.driver.find_elements_by_xpath(xpath_column)
        columns_driver.append(column)
    for column_driver in columns_driver:
        data_columns = []
        for position in range(len(column_driver)):
            data_columns.append(column_driver[position].text)
        columns_list_with_information.append(data_columns)
    return columns_list_with_information


# ------------------
# Checkbox functions
# ------------------

def check_checkbox(self, locator_type, locator):
    """Check a checkbox if this is not checked"""
    is_checked = locators.get_attribute_value(self, locator_type, locator, 'checked')
    if not is_checked:
        mouse.click_on_element(self, locator_type, locator)


def uncheck_checkbox(self, locator_type, locator):
    """Uncheck a checkbox if this is checked"""
    is_checked = locators.get_attribute_value(self, locator_type, locator, 'checked')
    if is_checked:
        mouse.click_on_element(self, locator_type, locator)


# ------------------
# Dropdown functions
# ------------------

def select_option_by_value(self, locator_type, locator, value):
    Select(locators.locator_element(self, locator_type, locator)).select_by_value(value)


def select_option_by_index(self, locator_type, locator, index):
    Select(locators.locator_element(self, locator_type, locator)).select_by_index(index)


def select_option_by_text(self, locator_type, locator, text):
    Select(locators.locator_element(self, locator_type, locator)).select_by_visible_text(text)


def get_options(self, locator_type, locator):
    """
    Func that return a list of strings with all the options from a dropdown selector
    """
    optionsList = []
    dropdown = locators.locator_element(self, locator_type, locator)
    selector = Select(dropdown)
    options = selector.options
    for index in range(1, len(options) - 1):
        optionsList.append(options[index].text)
    return optionsList


# --------------------
# Datepicker functions
# --------------------


def select_date(self, date, id_locator):  # Obligatorio ingresar locator type = ID
    split_date = date.split('/')
    # self.driver.find_element_by_id(str(type_entry).lower() + "_range_" + str(report).lower()).text
    current_date = locators.locator_element(self, 'ID', id_locator).text
    split_current_date = current_date.split('/')
    current_date_object = datetime.strptime(current_date, '%m/%d/%Y')
    date_object = datetime.strptime(date, '%m/%d/%Y')

    if date_object < current_date_object:
        mouse.click_on_element(self, 'CSS', '#' + id_locator + '>img')
        month = date_object.strftime('%B')
        if split_date[2] < split_current_date[2]:
            select_year(self, date)
            if month != get_month(self):
                select_month(self, date)
                select_day(self, date)
            else:
                select_day(self, date)
        elif month != get_month(self):
            select_month(self, date)
            select_day(self, date)
        else:
            select_day(self, date)


def select_date_all(self, date, id_locator):  # Obligatorio ingresar locator type = ID
    split_date = date.split('/')
    current_date = locators.locator_element(self, 'ID', id_locator).text
    split_current_date = current_date.split('/')
    current_date_object = datetime.strptime(current_date, '%m/%d/%Y')
    date_object = datetime.strptime(date, '%m/%d/%Y')

    mouse.click_on_element(self, 'CSS', '#' + id_locator + '>img')
    month = date_object.strftime('%B')
    if split_date[2] < split_current_date[2]:
        select_year(self, date)
        if month != get_month(self):
            select_month(self, date)
            select_day(self, date)
        else:
            select_day(self, date)
    elif month != get_month(self):
        select_month(self, date)
        select_day(self, date)
    else:
        select_day(self, date)


def select_month(self, date):
    split_date = date.split('/')
    mouse.click_on_element(self, 'XPATH', ".//div[contains(@class,'react-datepicker__month-read-view')]")
    mouse.click_on_element(self, 'XPATH',
                           ".//div[contains(@class,'react-datepicker__month-option')][" + split_date[0] + "]")


def select_year(self, date):
    split_date = date.split('/')
    mouse.click_on_element(self, 'XPATH', ".//div[contains(@class,'react-datepicker__year-read-view')]")
    mouse.click_on_element(self, 'XPATH',
                           ".//div[contains(@class,'react-datepicker__year-option') and text()='" + split_date[
                               2] + "']")


def select_day(self, date):
    split_date = date.split('/')
    mouse.click_on_element(self, 'XPATH',
                           "//div[not(contains(@class,'--outside-month')) and (contains(@class,'day--0" + split_date[
                               1] + "'))]")


def get_month(self):
    return locators.locator_element(self, 'XPATH', ".//span[contains(@class,'--selected-month')]").text


# ----------------
# Input functions
# ----------------

def set_input_value(self, locator_type, locator, value):
    element = locators.locator_element(self, locator_type, locator)
    locators.highlight(self, element)
    self.driver.execute_script("arguments[0].value = '" + value + "';", element)


# ---------------------
# Payer forms functions
# ---------------------

def p_select_option_by_value(self, locator_type_arrow, locator_arrow, locator_type_text, locator_text, text):
    mouse.click_on_element(self, locator_type_arrow, locator_arrow)
    enter_text_press_enter(self, locator_type_text, locator_text, text)
