from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils import sfdc_login
from env import email


def opportunity_creator(driver, instance):
    driver.get(
        "https://sartorius--uat.sandbox.lightning.force.com/lightning/o/Opportunity/new?"
    )
    breakpoint()
    account_name = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="combobox-input-499"]'))
    )
    account_name.send_keys("0200011116")
    account = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="combobox-input-499-0-499"]')
        )
    )
    account.click()
    breakpoint()


if __name__ == "__main__":
    breakpoint()
    driver = sfdc_login("uat", email)
    opportunity_creator(driver, "uat")


# driver.find_element(By.XPATH, '//*[@id="combobox-input-499"]')
# //*[@id="combobox-input-499-0-499"]
