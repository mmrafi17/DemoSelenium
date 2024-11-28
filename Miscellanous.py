import time

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')  # script automation without showing the browser
chrome_options.add_argument('--ignore-certificate-errors--')  # script for ignoring the ssl certificate
# Service("/Users/MRF/document/chromedriver")

driver = webdriver.Chrome(chrome_options)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")  # using javascript

time.sleep(1)
