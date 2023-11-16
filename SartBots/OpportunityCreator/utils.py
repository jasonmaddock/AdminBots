from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from env import email


def sfdc_login(instance, email):
    instance_urls = {
        "prod": "https://sartorius.lightning.force.com/lightning/page/home",
        "uat": "https://sartorius--uat.sandbox.lightning.force.com/lightning/page/home",
        "qa": "https://sartorius--qa.sandbox.lightning.force.com/lightning/page/home",
    }
    driver = webdriver.Chrome()
    driver.get(instance_urls[instance])
    if instance in ["uat", "qa"]:
        ssn = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "idp_section_buttons"))
        )
        ssn.click()
    firstname_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "loginfmt"))
    )
    next_button = driver.find_element(By.ID, "idSIButton9")
    firstname_field.send_keys(email)
    next_button.click()
    breakpoint()
    confirm_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
    )
    confirm_button.click()
    yes_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
    )
    yes_button.click()
    return driver
