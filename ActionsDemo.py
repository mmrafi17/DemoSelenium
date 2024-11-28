import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action = ActionChains(driver)
# action.scroll_to_element(driver.find_element(By.))
action.move_to_element(driver.find_element(By.ID, "mousehover1")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
# action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

time.sleep(2)
