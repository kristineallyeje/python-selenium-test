import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative

    def test_negative_username(self):
        #Open page
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")
        # Push Submit button
        submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_locator = driver.find_element(By.ID, "error")
        assert error_locator.is_displayed(), "Error message was not displayed, but it should."

        # Verify error message text is Your username is invalid!
        error_message = error_locator.text
        assert error_message == "Your username is invalid!", "Error message is not expected"

