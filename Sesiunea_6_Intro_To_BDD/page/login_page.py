from selenium.webdriver.common.by import By
from page.base_page import BasePage


class LoginPage(BasePage):
    username = (By.ID, "username")
    password = (By.ID, "password")
    banner = (By.ID, "flash")
    login_button = (By.XPATH, '//button[@type="submit"]')
    logout_button = (By.XPATH, '//a[@class="button secondary radius"]')
    secure_area_title = (By.XPATH, "//h2")
    banner_valid_text = "You logged into a secure area!\n×"
    banner_invalid_password_text = "Your password is invalid!\n×"
    banner_invalid_username_text = "Your username is invalid!\n×"
    valid_username = "tomsmith"
    valid_password = "SuperSecretPassword!"
    wrong_password = "SuperSecretPassword!321"

    def send_valid_username_and_password(self):
        self.chrome.find_element(*self.username).send_keys(self.valid_username)
        self.chrome.find_element(*self.password).send_keys(self.valid_password)

    def press_on_the_login_button(self):
        self.chrome.find_element(*self.login_button).click()

    def check_secure_area_page(self):
        check = self.chrome.find_element(*self.secure_area_title)
        assert check.text == "Secure Area", check.text

    def banner_logged_secure_area(self):
        check_banner = self.chrome.find_element(*self.banner)
        assert check_banner.text == self.banner_valid_text

    def check_logout_button(self):
        assert self.chrome.find_element(*self.logout_button).is_enabled()

    def correct_username_wrong_password(self):
        self.chrome.find_element(*self.username).send_keys(self.valid_username)
        self.chrome.find_element(*self.password).send_keys(self.wrong_password)

    def pasword_invalid_banner(self):
        invalid_banner = self.chrome.find_element(*self.banner)
        assert invalid_banner.text == self.banner_invalid_password_text

    def send_wrong_username_and_password(self, username, password):
        self.chrome.find_element(*self.username).send_keys(username)
        self.chrome.find_element(*self.password).send_keys(password)

    def username_invalid_banner(self):
        banner = self.chrome.find_element(*self.banner)
        assert banner.text == self.banner_invalid_username_text, banner.text
