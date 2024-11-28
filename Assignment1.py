import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By. CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By. XPATH, "//div[@class='products']/div")
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
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

# Total amount after Discount
totalAfterDiscount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(totalAfterDiscount)

assert totalAfterDiscount <= totalAmount

# total amount - discount = total after discount

time.sleep(2)
