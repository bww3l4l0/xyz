from selenium.webdriver import Chrome, ChromeOptions, ChromeService
from pytest import fixture
from os import getcwd

@fixture(scope='function')
def driver():
    service = ChromeService(executable_path='./chromedriver')
    options = ChromeOptions()
    options.binary_location = '/usr/bin/google-chrome'
    prefs = {"download.default_directory" : f'{getcwd()}'}
    options.add_experimental_option("prefs",prefs)
    driver = Chrome(options=options, service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()