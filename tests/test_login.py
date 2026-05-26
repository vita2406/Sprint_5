from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators, MainPageLocators

class TestLogin:
    def test_successful_login(self, driver):
        email = "popova_34@gmail.com"
        password = "qwertyuiop"
        
        driver.find_element(*AuthLocators.LOGIN_BUTTON).click()
        driver.find_element(*AuthLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthLocators.LOGIN_SUBMIT_BUTTON).click()
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(MainPageLocators.POST_AD_BUTTON))
        
        assert driver.find_element(*MainPageLocators.POST_AD_BUTTON).is_displayed()
