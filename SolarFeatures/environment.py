from selenium import webdriver

from utilities import configReader


def before_scenario(context, scenario):

    browser_name=configReader.read_configuration("basic info","browser")
    if browser_name.__eq__("Firefox"):
        context.driver = webdriver.Firefox()
    elif  browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()

    context.driver.maximize_window()
    context.driver.get(configReader.read_configuration("basic info","url"))


def after_scenario(context, scenario):
    context.driver.quit()