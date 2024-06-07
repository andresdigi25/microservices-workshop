from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common import desired_capabilities
import os

CHROME = "CHROME"
FIREFOX = "FIREFOX"
EDGE = "EDGE"
SAFARI = "SAFARI"


def chromeEnvironment():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-web-security")
    options.add_argument("--allow-running-insecure-content")
    urlSelenium = os.environ.get('LOAD_BALANCER_NAME') + "/wd/hub"
    return webdriver.Remote(command_executor=urlSelenium,
                            options=options)


def firefoxEnvironment():
    urlSelenium = os.environ.get('LOAD_BALANCER_NAME') + "/wd/hub"
    return webdriver.Remote(command_executor=urlSelenium)


def edgeEnvironment():
    urlSelenium = os.environ.get('LOAD_BALANCER_NAME') + "/wd/hub"
    return webdriver.Remote(command_executor=urlSelenium)


def createEnvironment():
    if (os.environ.get("BROWSER_NAME") == None) or (os.environ.get("LOAD_BALANCER_NAME") == None):
        print("Error, can't found the environment variables:[BROWSER_NAME or LOAD_BALANCER_NAME]")
        return None
    browser = os.environ.get("BROWSER_NAME").upper()
    print(browser)
    if browser == SAFARI:
        return webdriver.Safari()
    elif browser == CHROME:
        return chromeEnvironment()
    elif browser == FIREFOX:
        return firefoxEnvironment()
    elif browser == EDGE:
        return edgeEnvironment()
    else:
        return chromeEnvironment()
