# from html.parser import incomplete
# from idlelib.rpc import response_queue
# from os import waitpid
# from wsgiref.util import application_uri

from behave import *
import re
import logging
# from pytest_bdd.generation import print_missing_code
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests


logging.basicConfig(level=logging.INFO)
logging.info("✅ Logging works too!")

@given(u'I login to solar app')
def step_impl(context):
    # context.driver = webdriver.Firefox()
    # context.driver.maximize_window()
    # context.driver.get("http://solar.silvan.co.in/polycabsolar/#/auth-user/lurlogin")
    context.driver.find_element(By.XPATH, "//div[text()='Admin']").click()
    context.driver.find_element(By.ID, "input-email").send_keys("superadmin@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("superadmin@123")
    context.driver.find_element(By.XPATH, "//div[@class='position: relative; top: 10px;']/child::button").click()
    driver_visible = WebDriverWait(context.driver, 10)
    driver_visible.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='yes']"))).click()

@given(u'the API endpoint for device status is "{url}"')
def step_impl(context,url):
    context.api_url = url

@when(u'I send a GET request to the endpoint')
def step_impl(context):
    context.response=requests.get(context.api_url)
    context.response_json=context.response.json()


@then(u'the response status code should be {status_code:d}')
def step_impl(context,status_code):
      assert context.response.status_code==status_code

@then(u'the response should contain a "{field}"')
def step_impl(context, field):
    print(context.response.text)
    json_data=context.response_json
    assert field in json_data


@then(u'the device status counts should match expected values "{data}"')
def step_impl(context,data):
    wait=WebDriverWait(context.driver,30)

    def get_int_from_element(xpath):
        def text_is_not_empty(driver):
            element_name = driver.find_element(By.XPATH, xpath)
            return element_name.text.strip() != ""

        wait.until(text_is_not_empty)
        element = context.driver.find_element(By.XPATH, xpath)
        text_value = element.text.strip()
        if not text_value.isdigit():
            print(f"⚠ Warning: Expected number, but got '{text_value}'. Defaulting to 0.")
            return 0
        return int(text_value)

    # ✅ Get displayed counts from UI
    online_inverters = get_int_from_element("(//p[@class='headerRow']/following-sibling::p)[2]")
    offline_inverters = get_int_from_element("(//p[@class='headerRow']/following-sibling::p)[3]")
    incomplete_inverters = get_int_from_element("(//p[@class='headerRow']/following-sibling::p)[4]")

    json_data=context.response_json
    data=json_data[data]

    online_count=0
    offline_count=0
    incomplete_count=0
    print('-----------------------------')
    print(data)
    for item in data:
        status = item.get("status", "").lower()
        # count = item.get("count", 0)
        if status == "online":
            online_count =  item.get("count","")
        elif status == "offline":
            offline_count = item.get("count","")
        elif status == "incomplete":
            incomplete_count = item.get("count","")

    assert online_inverters==online_count
    assert offline_inverters==offline_count
    assert incomplete_inverters==incomplete_count
    context.driver.quit()

@given(u'the API endpoint for Daily Production is "{url}"')
def step_impl(context,url):
    context.api_url=url

@then(u'the daily production value should match')
def step_impl(context):
    wait=WebDriverWait(context.driver,320)
    # daily_production_value=wait.until(EC.visibility_of_element_located((By.XPATH,"(//div[@class='row contentRow'])[2]"))).text
    # print(daily_production_value)
    # # context.driver.find_element(By.XPATH,"(//div[@class='row contentRow'])[2]").text
    # numeric_value=re.findall(r"\d+\.\d+|\d",daily_production_value)[0]
    # print(numeric_value)
    # dp_value=float(numeric_value)

    wait.until(lambda driver: driver.find_element(By.XPATH, "(//div[@class='row contentRow'])[2]").text.strip() != "")
    daily_production_value = context.driver.find_element(By.XPATH, "(//div[@class='row contentRow'])[2]").text

    print("Raw text:", daily_production_value)

    # Safely extract numeric value
    matches = re.findall(r"\d+\.\d+|\d+", daily_production_value)
    if matches:
        numeric_value = matches[0]
        print("Extracted numeric value:", numeric_value)
        dp_value = int(float(numeric_value))
        print(dp_value)
    else:
        print("No numeric value found in:", daily_production_value)
        dp_value = None  # or handle this case as needed

    json_data=context.response.json()
    data=json_data["data"]
    daily_value_int=0
    for item in json_data.get("data", []):
        print(item)
        daily_energy_list = item.get("dailyEnergy", [])
        print(daily_energy_list)
        for energy in daily_energy_list:
            daily_value = energy.get("dailyEnergy")
            daily_value_int=int(float(daily_value))
            print("Daily Energy:", daily_value_int)
        else:
            print("none")

    assert dp_value>=daily_value_int
    # context.driver.quit()



@given(u'the API endpoint for peak hour ranking is "{url}"')
def step_impl(context,url):
    context.api_url=url

@then(u'peak hour rankings should be displayed')
def step_impl(context):
    # context.driver.find_element(By.XPATH,"(//div[@class='col-5']/child::div)[2]").text
    # context.driver.find_element(By.XPATH, "(//div[@class='col-5']/child::div)[5]").text
    # context.driver.find_element(By.XPATH, "(//div[@class='col-5']/child::div)[8]").text
    # context.driver.find_element(By.XPATH, "(//div[@class='col-5']/child::div)[11]").text
    # context.driver.find_element(By.XPATH, "(//div[@class='col-5']/child::div)[14]").text
    # context.driver.find_element(By.XPATH, "(//div[@class='col-5']/child::div)[17]").text
    # context.driver.find_element(By.XPATH, "(//div[@class='col-5']/child::div)[20]").text
    # context.driver.find_element(By.XPATH, "(//div[@class='col-5']/child::div)[23]").text
    # context.driver.find_element(By.XPATH, "(//div[@class='col-5']/child::div)[26]").text
    # context.driver.find_element(By.XPATH, "(//div[@class='col-5']/child::div)[29]").text
    ui_element_plant=[]
    for index in range(2,30,3):
        xpath=f"(//div[@class='col-5']/child::div)[{index}]"
        wait=WebDriverWait(context.driver,5)
        element_text=wait.until(EC.visibility_of_element_located((By.XPATH,xpath))).text
        ui_element_plant.append(element_text)
        print(element_text)

    json_data=context.response.json()
    api_plant_name=[]

    for item in json_data.get("data",[]):
        plant_name=item.get("plantName")
        api_plant_name.append(plant_name.strip())

    assert ui_element_plant==api_plant_name
    # context.driver.quit()


@given(u'the API endpoint for power normalization values is "{url}"')
def step_impl(context,url):
    context.api_url=url


@then(u'Top 10 power normalization values should be displayed')
def step_impl(context):

    ui_normalization_values=[]
    for items in range(11,30,2):
        xpath=f"(//div[@class='col-5'])[{items}]"
        wait=WebDriverWait(context.driver,5)
        normalization_value=wait.until(EC.visibility_of_element_located((By.XPATH,xpath))).text
        # ui_normalization_values.append(normalization_value)

        if normalization_value:
            normalized = normalization_value.lower()
            if normalized not in ui_normalization_values:
                ui_normalization_values.append(normalized)
                #print(normalized)
                print(ui_normalization_values)



    json_data=context.response.json()

    api_user_names=[]
    api_values=""
    for text in json_data.get("data", {}).get("topTen", []):
        user_name = text.get("username")
        if user_name:
            user_name = user_name.lower()
            if user_name not in api_user_names:  # prevent duplicates
                api_user_names.append(user_name)
                #print(user_name)
                print(api_user_names)

    assert ui_normalization_values==api_user_names
    # context.driver.quit()




















