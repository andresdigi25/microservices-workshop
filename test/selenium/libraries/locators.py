import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# -----------------
# Locator functions
# -----------------

def wait_for_clickable_element(self, how, what, source=0):
    response = is_element_present_visible_enabled(self, how, what, source)
    is_present_visible_enable = response[0]
    element = response[1]
    wait = 0
    wait_max = 3
    while not is_present_visible_enable and wait < wait_max:
        time.sleep(0.5)
        wait += 0.5
        response = is_element_present_visible_enabled(self, how, what, source)
        is_present_visible_enable = response[0]
        element = response[1]
    time.sleep(1)
    return element


def is_element_present_visible_enabled(self, how, what, source):
    if source == 0:
        try:
            element = self.driver.find_element(by=how, value=what)
            visible = element.is_displayed()
            enabled = element.is_enabled()
            response = visible and enabled
        except NoSuchElementException as e:
            return [False, None]
        return [response, element]
    else:
        try:
            element = source.find_element(by=how, value=what)
            visible = element.is_displayed()
            enabled = element.is_enabled()
            response = visible and enabled
        except NoSuchElementException as e:
            return [False, None]
        return [response, element]


def locator_element(self, locator_type, locator):
    """Find an element and return it"""
    time.sleep(0.5)
    if str(locator_type).upper() == 'ID':
        by = By.ID
    elif str(locator_type).upper() == 'NAME':
        by = By.NAME
    elif str(locator_type).upper() == 'XPATH':
        by = By.XPATH
    elif str(locator_type).upper() == 'CSS':
        by = By.CSS_SELECTOR
    elif str(locator_type).upper() == 'LINK':
        by = By.LINK_TEXT
    elif str(locator_type).upper() == 'CLASS_NAME':
        by = By.CLASS_NAME
    return wait_for_clickable_element(self, by, locator)


def locator_elements(self, locator_type, locator):
    """Find set of elements and return them"""
    time.sleep(0.5)
    if str(locator_type).upper() == 'ID':
        by = By.ID
    elif str(locator_type).upper() == 'NAME':
        by = By.NAME
    elif str(locator_type).upper() == 'XPATH':
        by = By.XPATH
    elif str(locator_type).upper() == 'CSS':
        by = By.CSS_SELECTOR
    elif str(locator_type).upper() == 'LINK':
        by = By.LINK_TEXT
    elif str(locator_type).upper() == 'CLASS_NAME':
        by = By.CLASS_NAME
    return self.driver.find_elements(by, locator)


def highlight(self, element):
    """Highlights (blinks) a Selenium Webdriver element"""
    #driver = element._parent
    try:
        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
        original_style = element.get_attribute('style')
        apply_style("background: yellow; border: 2px solid red;")
        time.sleep(0.3)
        apply_style(original_style)
    except:
        return


def get_by_element(locator_type):
    """Get the by type of an element"""
    time.sleep(0.5)
    if str(locator_type).upper() == 'ID':
        by = By.ID
    elif str(locator_type).upper() == 'NAME':
        by = By.NAME
    elif str(locator_type).upper() == 'XPATH':
        by = By.XPATH
    elif str(locator_type).upper() == 'CSS':
        by = By.CSS_SELECTOR
    elif str(locator_type).upper() == 'LINK':
        by = By.LINK_TEXT
    elif str(locator_type).upper() == 'CLASS_NAME':
        by = By.CLASS_NAME
    return by


def element_exists(self, locator_type, locator):
    element = []
    element = locator_elements(self, locator_type, locator)
    if len(element) > 0:
        return True
    else:
        return False

def element_is_displayed(self, locator_type, locator):
    element = locator_element(self, locator_type, locator)
    if element.is_displayed():
        return True
    else:
        return False

# -----------------
# Waits in the DOM
# -----------------


def wait_until_invisibility_of_element(self, locator_type, locator):
    """Wait until invisibility of element in the screen"""
    wait_for = 0.5
    by = get_by_element(locator_type)
    wait = WebDriverWait(self.driver, wait_for)
    while True:
        try:
            wait.until(EC.invisibility_of_element_located((by, locator)))
            break
        except:
            wait_for += 0.5


def wait_until_visibility_of_element(self, locator_type, locator):
    """Wait until visibility of element in the screen"""
    wait_for = 0.5
    by = get_by_element(locator_type)
    wait = WebDriverWait(self.driver, wait_for)
    while True:
        try:
            wait.until(EC.visibility_of_element_located((by, locator)))
            break
        except:
            wait_for += 0.5


def wait_until_presence_of_element(self, locator_type, locator):
    """Wait until presence of element in DOM"""
    wait_for = 0.5
    by = get_by_element(locator_type)
    wait = WebDriverWait(self.driver, wait_for)
    while True:
        try:
            wait.until(EC.presence_of_element_located((by, locator)))
            break
        except:
            wait_for += 0.5


def wait_until_alert_is_present(self):
    """Wait until alert is present"""
    wait_for = 0.2
    wait = WebDriverWait(self.driver, wait_for)
    while True:
        try:
            wait.until(EC.alert_is_present())
            break
        except:
            wait_for += 0.5

# ----------------------------------
# Attributes and properties functions
# ----------------------------------


def get_attribute_value(self, locator_type, locator, attribute):
    element = locator_element(self, locator_type, locator)
    attribute_value = element.get_attribute(attribute)
    return attribute_value


def get_all_attributes(self, locator_type, locator):
    element = locator_element(self, locator_type, locator)
    attrs = []
    for attr in element.get_property('attributes'):
        attrs.append([attr['name'], attr['value']])
    return attrs