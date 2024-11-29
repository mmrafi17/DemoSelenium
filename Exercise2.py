import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service('C:/Users/MRF/Downloads/Compressed/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

# search keywords
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys('be')
time.sleep(2)
products = driver.find_elements(By.CSS_SELECTOR, "div[class='product']")
# iterate for result of search

actualProductName = ['Cucumber - 1 Kg', 'Beetroot - 1 Kg', 'Beans - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
expectedProductName = []
for product in products:
    product.find_element(By.CSS_SELECTOR, "div[class='product-action'] button").click()
    expectedProductName.append(product.find_element(By.CSS_SELECTOR, "div h4[class='product-name']").text)

assert expectedProductName == actualProductName

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME, "promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# promo
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

totalAmount = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")

expectedAmount = 0
for amount in totalAmount:
    expectedAmount = expectedAmount + int(amount.text)

actualAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert expectedAmount == actualAmount

discAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert discAmount < expectedAmount
