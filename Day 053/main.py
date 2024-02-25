from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
import time

from bs4 import BeautifulSoup
import requests


FORM_URL = "https://forms.gle/t2ueJAMAxSimaanv5"
WEBSITE_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(WEBSITE_URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the URLs, addresses, and prices
# Assuming there are multiple listings on the page
urls = [a['href'] for a in soup.find_all('a', class_='StyledPropertyCardDataArea-anchor')]
addresses = [address.get_text(strip=True) for address in soup.find_all('address', {'data-test': 'property-card-addr'})]
prices = [price.get_text(strip=True).replace("+/mo", "") for price in soup.find_all('span', {'data-test': 'property-card-price'})]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)


def fill_form(urls, addresses, prices):
    for i in range(len(urls)):
        driver.get(FORM_URL)
        time.sleep(2)
        input_elements = driver.find_elements(By.CLASS_NAME, 'whsOnd')
        click_button = driver.find_element(By.CSS_SELECTOR, ".NPEfkd.RveJvd.snByac")
        
        input_elements[0].send_keys(addresses[i])
        input_elements[1].send_keys(prices[i])
        input_elements[2].send_keys(urls[i])
        click_button.click()
        
fill_form(urls, addresses, prices)
driver.quit()