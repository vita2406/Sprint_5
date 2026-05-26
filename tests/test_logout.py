from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators, MainPageLocators

class TestLogout:
    def test_successful_logout(self, driver):
        email = "popova_34@gmail.com"
        password = "qwertyuiop"
        
        driver.find_element(*AuthLocators.LOGIN_BUTTON).click()
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthLocators.LOGIN_SUBMIT_BUTTON).click()
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(MainPageLocators.POST_AD_BUTTON))
        
        logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Выйти']")))
        logout_button.click()
        
        wait.until(EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON_TOP))
        assert driver.find_element(*MainPageLocators.LOGIN_BUTTON_TOP).is_displayed()
