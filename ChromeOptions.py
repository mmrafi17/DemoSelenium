from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()

chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://rahulshettyacademy.com/angularpractice/")


print(driver.title)
