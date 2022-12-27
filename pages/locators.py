from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    Login_link = (By.CSS_SELECTOR, "#id_login-username")
    Registration_link_email = (By.CSS_SELECTOR, '#id_registration-email')
