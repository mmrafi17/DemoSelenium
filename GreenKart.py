import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service('C:/Users/MRF/Downloads/Compressed/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.maximize_window()

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')
addItem = []
# driver.find_element(By.XPATH, "//option[@value='10']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
items = driver.find_elements(By.CSS_SELECTOR, "tr td:first-child")
for item in items:
    addItem.append(item.text)

originalItems = addItem.copy()

assert addItem == originalItems

time.sleep(2)
