import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

windowOpened = driver.window_handles
driver.switch_to.window(windowOpened[1])
textElement = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
emailText = textElement.split()
print(emailText[4])
driver.switch_to.window(windowOpened[0])
driver.find_element(By.ID,"username").send_keys(emailText[4])
driver.find_element(By.CSS_SELECTOR, "#password").send_keys('password123')
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(1)
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

