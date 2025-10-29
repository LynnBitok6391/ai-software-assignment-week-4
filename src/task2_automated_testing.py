from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://example.com/login")  # replace with your test page

# Valid login test
driver.find_element(By.ID, "username").send_keys("valid_user")
driver.find_element(By.ID, "password").send_keys("valid_pass")
driver.find_element(By.ID, "login").click()
time.sleep(2)
print("✅ Valid login test completed.")

# Invalid login test
driver.find_element(By.ID, "username").send_keys("wrong_user")
driver.find_element(By.ID, "password").send_keys("wrong_pass")
driver.find_element(By.ID, "login").click()
time.sleep(2)
print("❌ Invalid login test completed.")

driver.quit()
