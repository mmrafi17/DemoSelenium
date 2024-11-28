import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")

driver.find_element(By.LINK_TEXT, "Forgot password?").click()  # find element by link/a/href and choose their value
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")  # find element by xpath and choose their parent and child.
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("hello@1234")  # find element by css_selector and choose their parent and child.
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("hello@1234")  # find element by css_selector and choose their id
# driver.find_element(By.XPATH,  "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()  # find element by path choose text on it

time.sleep(2)
