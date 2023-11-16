from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


user_dict = {'FirstName': 'Jason', 'LastName': 'Maddock', 'Email': 'jason.maddock@sartorius.com', 'UserType': 'LPSSalesRep', 'Country': 'United Kingdom'}

firstname = "Jason"
lastname = "Maddock"
username = "jason.maddock@sartorius.com"
user_type = "LPSSalesRep"
country = "United Kingdom"

def startup():
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=/home/jason/Jason/Sart/SartBots/User Data")
    driver = webdriver.Chrome(options=options)
    sfdc_url = "https://sartorius.lightning.force.com/lightning/r/Quote/0Q07T000001GDsISAW/view"
    driver.get(sfdc_url)
    quote_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="brandBand_2"]/div/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-c-p-q_-quote_-record_-page___-quote___-v-i-e-w/forcegenerated-flexipage_cpq_quote_record_page_quote__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-template-desktop2/div/div[1]/slot/flexipage-component2[1]/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_quote___0127t000001105cqaq___compact___view___recordlayout2/records-highlights2/div[1]/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li/runtime_platform_actions-action-renderer/runtime_platform_actions-executor-lightning-component/slot/slot/lightning-button/button')))
    quote_button.click()
    time.sleep(2)
    return(driver)

def add_user(driver, user_dict):
    users_url = "https://sartoriusadgmbh.cpq.cloud.sap/multiusers/UserAdministerUsersList.aspx"
    driver.get(users_url)
    add_new_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "new_button")))
    add_new_button.click()

    firstname_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "ctl01$MainContentPlaceHolder$txtFirstName")))
    lastname_field = driver.find_element(By.NAME, 'ctl01$MainContentPlaceHolder$txtLastName')
    username_field = driver.find_element(By.NAME, 'ctl01$MainContentPlaceHolder$txtUsername')
    email_field = driver.find_element(By.NAME, 'ctl01$MainContentPlaceHolder$txtEmail')
    user_type_dd = Select(driver.find_element(By.NAME, 'ctl01$MainContentPlaceHolder$ddlType'))
    country_dd = Select(driver.find_element(By.NAME, 'ctl01$MainContentPlaceHolder$CountryState$ddlCountry'))


    firstname_field.send_keys(user_dict["FirstName"])
    lastname_field.send_keys(user_dict["LastName"])
    email_field.send_keys(user_dict["Email"])
    username_field.send_keys(user_dict["Email"])
    user_type_dd.select_by_visible_text(user_dict["UserType"])
    country_dd.select_by_visible_text(user_dict["Country"])

    save_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'ctl01$MainContentPlaceHolder$btnSave')))
    save_button.click()
    try:
        add_new_button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "new_button")))
        return("SUCCESS")
    except:
        return("DUPLICATE")

if __name__ == "__main__":
    driver = startup()
    add_user(driver, user_dict)
    breakpoint()