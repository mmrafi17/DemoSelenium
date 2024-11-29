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
driver.get('https://rahulshettyacademy.com/angularpractice/')


driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
productCards = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

print(len(productCards))
for product in productCards:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == 'Nokia Edge':
        print(productName)
        product.find_element(By.XPATH, "//button[@class='btn btn-info']").click()

driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()
driver.find_element(By.CLASS_NAME, "btn.btn-success").click()

# search country
driver.find_element(By.ID, "country").send_keys('And')
time.sleep(5)
countries = driver.find_elements(By.XPATH, "//div[@class='suggestions']/ul/li/a")

# for country in countries:
#     if country.text == 'Poland':
#         country.click()
#         print(country.text)

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Poland")))
driver.find_element(By.LINK_TEXT, "Poland").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
alert = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

assert 'Success' in alert
