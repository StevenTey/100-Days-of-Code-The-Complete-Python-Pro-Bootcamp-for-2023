# Import packages for Linkedin Job Application Automation
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.linkedin.com/jobs/search/?currentJobId=3757500873&f_AL=true&geoId=102454443&keywords=python&location=Singapore&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true&sortBy=R"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get(url)

user_name = "stevenweijun1@gmail.com"

login_button = driver.find_element(By.CSS_SELECTOR, 'a.nav__button-secondary.btn-md.btn-secondary-emphasis')
login_button.click()

time.sleep(2)

email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(user_name)