import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver import ChromeOptions


def createEnvironment():

    try:
        browser_name = os.environ['BROWSER_NAME']
        return get_driver(browser_name.upper())

    except KeyError:
        raise Exception('Environment variable, BROWSER_NAME is not set!')

    except Exception as e:
        raise Exception(f'Failed to setup driver! \nMessage: {e}')


def get_driver(browser_name: str):

    if browser_name == 'CHROME':
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        return webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    elif browser_name == 'FIREFOX':
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif browser_name == 'EDGE':
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))