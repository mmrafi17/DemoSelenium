import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By. CSS_SELECTOR, ".search-keyword").send_keys("ca")
time.sleep(2)

expectedList = ['Cauliflower - 1 Kg', 'Carrot - 1 Kg', 'Capsicum', 'Cashews - 1 Kg']
actualList = []
results = driver.find_elements(By. CSS_SELECTOR, "div[class='products'] div h4")

for result in results:
    actualList.append(result.text)

assert expectedList == actualList


time.sleep(2)
