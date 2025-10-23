from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'I have navigted to login page')
def step_impl(context):
    # context.driver=webdriver.Firefox()
    # context.driver.maximize_window()
    # context.driver.get("http://solar.silvan.co.in/polycabsolar/#/auth-user/login")
    pass


@when(u'I entered valid email address and password into the valid fiels')
def step_impl(context):
       context.driver.find_element(By.XPATH,"//div[text()='Admin']").click()
       context.driver.find_element(By.ID, "input-email").send_keys("superadmin@gmail.com")
       context.driver.find_element(By.ID, "input-password").send_keys("superadmin@123")


@when(u'I click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@class='position: relative; top: 10px;']/child::button").click()


@when(u'I select the yes option')
def step_impl(context):
      driver_visible = WebDriverWait(context.driver, 10)
      driver_visible.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='yes']"))).click()
      # context.driver.find_element(By.XPATH,"//button[@class='yes']").click()

@then(u'I should be logged in')
def step_impl(context):
     display_context="Solar Monitoring Dashboard"
     visible_text=WebDriverWait(context.driver,10)
     assert visible_text.until(EC.visibility_of_element_located((By.ID,"dhead"))).text.__eq__(display_context)
     # context.driver.quit()

@when(u'I have entered invalid email address and valid password into the fiels')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[text()='Admin']").click()
    context.driver.find_element(By.ID, "input-email").send_keys("superadmin1234567@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("superadmin@123")


@then(u'I should not be logged in and should get proper warning message')
def step_impl(context):
    expected_text = "failed"  # Replace with your actual warning text


    warning = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='content-container']/span"))
        )
    assert warning.text == expected_text
    # context.driver.quit()


@when(u'I have entered valid email address and invalid password into the fiels')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[text()='Admin']").click()
    context.driver.find_element(By.ID, "input-email").send_keys("superadmin@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("super")


@when(u'I have entered invalid email and password')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[text()='Admin']").click()
    context.driver.find_element(By.ID, "input-email").send_keys("superadmin1234567@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("super")


@when(u'I have not entered email and password')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[text()='Admin']").click()
    context.driver.find_element(By.ID, "input-email").send_keys()
    context.driver.find_element(By.ID, "input-password").send_keys()

@then(u'I should not be logged in and should get proper warning message that is Failed')
def step_impl(context):
    expected_text = "Failed"  # Replace with your actual warning text


    warning = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='content-container']/span"))
        )
    assert warning.text == expected_text
    # context.driver.quit()