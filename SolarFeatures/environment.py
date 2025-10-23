from selenium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    context.driver.get("http://solar.silvan.co.in/polycabsolar/#/auth-user/login")


def after_scenario(context, scenario):
    context.driver.quit()