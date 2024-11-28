import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = 'Majin'
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert  # to access alert browser
print(alert.text)

assert name in alert.text

alert.accept()  # to click ok on alert
# alert.dismiss()

time.sleep(1)
