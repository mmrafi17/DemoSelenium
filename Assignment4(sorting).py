import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')
expectedData = []

# click head of column
driver.find_element(By.CSS_SELECTOR, "tr th:first-child").click()

# collect all column data vegetables
dataVegetables = driver.find_elements(By.CSS_SELECTOR, "tr td:first-child")

for vegetable in dataVegetables:
    expectedData.append(vegetable.text)

originalData = expectedData.copy()

# sorting the vegetables data
expectedData.sort()

# assert the sorting
# assert expectedData == originalData
print(expectedData)
print(originalData)
time.sleep(1)
