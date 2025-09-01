import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Open browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#browser new update - web browser manager downloaded new version of chrome driver to support newer browser ver)
time.sleep(3)

#1 Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

#2. Type username student into Username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")
#command to type text into input keys (push) - send_keys

# 3. Type password Password123 into Password field
password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")

#4. Push Submit button
submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_locator.click()
time.sleep(2)
#click command to click the button

#5 Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"
#assert - compares

#6 Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text  = text_locator.text
assert actual_text == "Logged In Successfully"
#text locator - find the element to get the text

#7Verify button Log out is displayed on the new page
logout_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert logout_locator.is_displayed()
#link text = output of link text
