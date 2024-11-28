import time

from selenium import webdriver
# from selenium.webdriver.chrome import service

# service_obj = service('\Users\MRF\Downloads\Compressed\chromedriver-win64\chromedriver-win64.exe')
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(2)
