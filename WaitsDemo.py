import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service('C:/Users/MRF/Downloads/Compressed/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)  # implicit wait
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By. CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By. XPATH, "//div[@class='products']/div")  # list[]
count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, ".cart-icon img").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Amount
amounts = driver.find_elements(By.XPATH, "//tr/td[5]/p")

addSum = 0
for amount in amounts:
    addSum = addSum + int(amount.text)

totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(totalAmount)
assert addSum == totalAmount

# Promo
wait = WebDriverWait(driver, 10)  # explicit wait is use if we have spesific element that need more than global wait
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
assert driver.find_element(By.CSS_SELECTOR, ".promoInfo").text == 'Code applied ..!'
