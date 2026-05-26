import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators, MainPageLocators

class TestRegistration:
    def test_successful_registration(self, driver):
        unique_email = f"user{time.time()}@test.ru"
        password = "123456"
        wait = WebDriverWait(driver, 10)
        
        driver.find_element(*AuthLocators.LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.REGISTER_LINK)).click()
        
        email_input = wait.until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT))
        email_input.send_keys(unique_email)
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthLocators.CREATE_ACCOUNT_BUTTON).click()
        
        wait.until(EC.visibility_of_element_located(MainPageLocators.POST_AD_BUTTON))
        assert driver.find_element(*MainPageLocators.POST_AD_BUTTON).is_displayed()
