from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given(u'Navigate to login page')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    context.driver.get("http://solar.silvan.co.in/polycabsolar/#/auth-user/login")
    context.driver.find_element(By.XPATH, "//div[text()='Admin']").click()
    time.sleep(3)

@when(u'I login to solar app')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("superadmin@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("superadmin@123")
    context.driver.find_element(By.XPATH, "//div[@class='position: relative; top: 10px;']/child::button").click()
    driver_visible = WebDriverWait(context.driver, 10)
    driver_visible.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='yes']"))).click()
    time.sleep(3)


@then(u'Solar Monitoring Dashboard should be visible')
def step_impl(context):
    expected_output="Solar Monitoring Dashboard"
    assert context.driver.find_element(By.ID,"dhead").text.__eq__(expected_output)
    time.sleep(3)
    context.driver.quit()

@when(u'If i select light')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@class='select-button']").click()
    context.driver.find_element(By.ID,"nb-option-0").click()

@then(u'the light mode should be visible')
def step_impl(context):
    # Check the background color of the layout container
    body = context.driver.find_element(By.XPATH, "//div[@class='col-6']/span")
    bd_color = body.value_of_css_property("color")
    print(bd_color)
    expected_color = "rgb(74, 68, 68)"
    print("Actual background color:", bd_color)

    # Assert the color matches expected
    assert bd_color == expected_color, f"Expected {expected_color}, but got {bd_color}"
    context.driver.quit()


@when(u'If i select dark')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@class='select-button']").click()
    context.driver.find_element(By.ID,"nb-option-1").click()

@then(u'the dark mode should be visible')
def step_impl(context):
    # Check the background color of the layout container
    body = context.driver.find_element(By.XPATH, "//div[@class='col-6']/span")
    bd_color = body.value_of_css_property("color")
    print(bd_color)
    expected_color = "rgb(179, 165, 165)"
    print("Actual background color:", bd_color)

    # Assert the color matches expected
    assert bd_color == expected_color, f"Expected {expected_color}, but got {bd_color}"
    context.driver.quit()

@when(u'If i click on setting icon')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//span[@class='sett-icon context-menu-host']").click()

@then(u'profile and logout option should be visible')
def step_impl(context):
    # expected_texts_one="Profile"
    # expected_text_two="Logout"
    #
    # assert context.driver.find_element(By.XPATH,"//a[@title='Profile']").text.__eq__(expected_texts_one)
    # assert context.driver.find_element(By.XPATH, "//a[@title='Logout']").text.__eq__(expected_text_two)
    # context.driver.quit()

    expected_output={
        "Profile":"//a[@title='Profile']",
        "Logout":"//a[@title='Logout']"
      }

    for value,xpath in expected_output.items():
        actual_result=context.driver.find_element(By.XPATH,xpath).text
        assert value==actual_result

    context.driver.quit()

@then(u'Production Overview, Device Status, Historical Production, Peak Hour Rankings, Overall Planned Production and Power Normalization Rankings should exist.')
def step_impl(context):

    expected_output_value={
            "Production Overview":"(//div[@class='col-6 headname'])[1]",
            "Historical Production":"(//div[@class='col-6 headname'])[2]",
            "Device Status":"//div[@class='col-12 headname']",
            "Peak Hour Rankings":"(//div[@class='col-8 headname'])[1]",
            "Overall Planned Production":"(//div[@class='col-8 headname'])[2]",
            "Power Normalization Rankings":"(//div[@class='col-8 headname'])[3]"
    }

    for values,xpath_value in expected_output_value.items():
            wait=WebDriverWait(context.driver,15)
            actual_result_value=wait.until(EC.visibility_of_element_located((By.XPATH,xpath_value))).text
            print(values)
            assert values==actual_result_value

    context.driver.quit()


@then(u'Daily, Monthly, Yearly and total production and Total Plants Capacity should be visible')
def step_impl(context):
    expected_production_values={
        "Total Plants Capacity": "(//div[@class='col-12'])[1]",
        "Daily Production":"(//div[@class='row headerRow'])[2]",
        "Monthly Production":"(//div[@class='row headerRow'])[3]",
        "Yearly Production":"(//div[@class='row headerRow'])[4]",
        "Total Production":"(//div[@class='row headerRow'])[5]"
    }

    for value, xpath in expected_production_values.items():
        actual_result = context.driver.find_element(By.XPATH, xpath).text
        assert value == actual_result

    context.driver.quit()

@then(u'Total, Online, Offline and Incomplete Inverters should be visible')
def step_impl(context):
    expected_device_status={
        "Total Inverters":"//p[text()=' Total Inverters']",
        "Online Inverters":"//p[text()='Online Inverters']",
        "Offline Inverters":"//p[text()='Offline Inverters']",
        "Incomplete Inverters":"//p[text()='Incomplete Inverters']"
    }

    for value, xpath in expected_device_status.items():
        actual_result = context.driver.find_element(By.XPATH, xpath).text
        assert value == actual_result

    context.driver.quit()

@then(u'By adding the Online, Offline and Incomplete Inverters should be equal to Total Inverters')
def step_impl(context):
      total_inverters=context.driver.find_element(By.XPATH,"(//p[@class='headerRow']/following-sibling::p)[1]").text
      online_inverters=context.driver.find_element(By.XPATH,"(//p[@class='headerRow']/following-sibling::p)[2]").text
      offline_inverters=context.driver.find_element(By.XPATH,"(//p[@class='headerRow']/following-sibling::p)[3]").text
      incomplete_inverters=context.driver.find_element(By.XPATH,"(//p[@class='headerRow']/following-sibling::p)[4]").text

      sum_inverters=int(online_inverters)+int(offline_inverters)+int(incomplete_inverters)

      assert int(total_inverters)==sum_inverters
      context.driver.quit()