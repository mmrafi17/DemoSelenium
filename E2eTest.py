import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(4)
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "a[href$='/angularpractice/shop']").click()
shopCards = driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100']")
for card in shopCards:
    productName = card.find_element(By.CSS_SELECTOR, "div h4 a").text
    if productName == 'Blackberry':
        card.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR, "#country").send_keys('ind')
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Indonesia")))
driver.find_element(By.LINK_TEXT, 'Indonesia').click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in successText
time.sleep(1)
driver.close()
