import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# chrome_options = webdriver.ChromeOptions()
# webdriver.Chrome()
# Service("/Users/MRF/document/chromedriver")

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.switch_to.frame('courses-iframe')  # script os make inside iframe
# driver.find_element(By.ID, "hide-textbox").click()

print(driver.find_element(By.CSS_SELECTOR, "section[class=subscribe-style-one] div:first-child h2").text)
driver.switch_to.default_content()  # script to make outside iframe
print(driver.find_element(By.CSS_SELECTOR, ".block:nth-child(6) div:first-child").text)

time.sleep(1)
