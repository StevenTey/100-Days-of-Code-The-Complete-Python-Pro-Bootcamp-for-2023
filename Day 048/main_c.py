from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# write me code that will keep clicking on the cookie and for every 5 secs it will perform something else which i will mention later
cookie_button = driver.find_element(by = By.ID, value="cookie")
start_time = time.time()
next_button_time = start_time + 5
end_time = start_time + 1*60

while True:
    cookie_button.click()
    
    if time.time() >= next_button_time:
        non_grey_buttons = driver.find_elements(by = By.CSS_SELECTOR, value="#store div:not(.grayed)")
        last_non_grey_button = non_grey_buttons[-1].click()
        next_button_time = time.time() + 5
    
    if time.time() >= end_time:
        break

# Get the score
score = driver.find_element(by = By.ID, value="money").text
score_per_second = driver.find_element(by = By.ID, value="cps").text.split(":")[1].strip()
print(f"Your score is: {score}")
print(f"Your score per second is: {score_per_second}")