from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators, MainPageLocators, AdFormLocators, ModalLocators

class TestAds:
    def test_create_ad_unauthorized(self, driver):
        driver.find_element(*MainPageLocators.POST_AD_BUTTON).click()
        wait = WebDriverWait(driver, 5)
        modal_title = wait.until(EC.visibility_of_element_located(ModalLocators.MODAL_TITLE))
        assert modal_title.is_displayed()
