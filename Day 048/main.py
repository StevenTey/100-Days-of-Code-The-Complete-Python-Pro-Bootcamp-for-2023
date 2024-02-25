from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
# driver.get("https://www.python.org/")
driver.get("https://secure-retreat-92358.herokuapp.com/")

# close - tab, quit - browser
# event_times = driver.find_elements(by = By.CSS_SELECTOR, value=".event-widget li time")
# event_names = driver.find_elements(by = By.CSS_SELECTOR, value=".event-widget li ")

# events_dict = {n: {"time": event_times[n].text, "name": event_names[n].text} for n in range(len(event_times))}
# print(events_dict)

# article_count = driver.find_element(by = By.CSS_SELECTOR, value='a[title="Wikipedia:Community portal"]')
# article_count.click()
# print(article_count.text)

# search_input = driver.find_element(by= By.XPATH, value='//*[@id="searchform"]')
# search_input.send_keys("Python")

first_name_input = driver.find_element(by = By.NAME,value='fName')
first_name_input.send_keys("Steven")

last_name_input = driver.find_element(by = By.NAME,value='lName')
last_name_input.send_keys("Tey")

email_input = driver.find_element(by = By.NAME,value='email')
email_input.send_keys("stevenweijun1@gmail.com")

click_button = driver.find_element(by = By.CLASS_NAME,value='btn-primary')
click_button.click()

driver.quit()