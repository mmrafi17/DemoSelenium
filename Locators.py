import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# from selenium.webdriver.chrome import service

# service_obj = service('\Users\MRF\Downloads\Compressed\chromedriver-win64\chromedriver-win64.exe')
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()
driver.find_element(By.NAME, "name").send_keys("Majin Buu")  # find element by attribut name name and send keys majin buu
driver.find_element(By.NAME, "email").send_keys("Majinbuu@test.com")  # find element by attribut name email and send keys majin buu
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Poiuy09876%") # find element by atribut id
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
# driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Majin Buu again")  # find element by XPATH index 3 and send keys majib buu again

# Static Dropdowns
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# dropdown.select_by_visible_text("Female")  # select element dropdown by visible text
dropdown.select_by_index(1)  # select element dropdown by index start from 0
# dropdown.select_by_value("")  # select element dropdown by value


driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()  # clear element by XPATH index 3
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()  # find element by CSS_SELECTOR and click
driver.find_element(By.XPATH, "//input[@type='submit']").click()  # find element by XPATH that include value is submit in atribut type on the input tag

message = driver.find_element(By.CLASS_NAME, "alert-success").text  # find element by CLASS_NAME and select the word using syntax text
print(message)
assert "Success!" in message  # how to assert that include word Success! in messages variable

# for XPATH you can type "//tagname[@attribute='value'] -> //button[@type='submit']
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# for CSS_SELECTOR you can type "tagname[attribute='value'] -> button[type='submit'] , for id #id for class .classname
# driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# driver.find_element(By.CSS_SELECTOR, "#agreeTerms").click()

time.sleep(2)
