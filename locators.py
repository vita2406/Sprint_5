from selenium.webdriver.common.by import By

class AuthLocators:
    LOGIN_BUTTON = (By.CLASS_NAME, "buttonSecondary")
    REGISTER_LINK = (By.XPATH, "//button[text()='Нет аккаунта']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "submitPassword")

class MainPageLocators:
    AVATAR = (By.CLASS_NAME, "circleSmall")
    USER_NAME = (By.CLASS_NAME, "profileText")
    POST_AD_BUTTON = (By.CLASS_NAME, "buttonPrimary")
    LOGIN_BUTTON_TOP = (By.CLASS_NAME, "buttonSecondary")

class ModalLocators:
    MODAL_TITLE = (By.XPATH, "//div[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")

class AdFormLocators:
    TITLE_INPUT = (By.NAME, "title")
    DESCRIPTION_INPUT = (By.NAME, "description")
    PRICE_INPUT = (By.NAME, "price")
    CATEGORY_DROPDOWN = (By.NAME, "category")
    CITY_DROPDOWN = (By.NAME, "city")
    CONDITION_NEW = (By.XPATH, "//input[@value='new']")
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")

class ProfileLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    MY_ADS_BLOCK = (By.CSS_SELECTOR, ".my-ads")
    AD_ITEM = (By.CSS_SELECTOR, ".ad-item")
