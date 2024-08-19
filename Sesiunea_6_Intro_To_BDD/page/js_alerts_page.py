from selenium.webdriver.common.by import By
from page.base_page import BasePage


class JsAlertsPage(BasePage):
    js_alert_button = (By.XPATH, "//button[@onclick=\"jsAlert()\"]")
    js_confirm_button = (By.XPATH, "//button[@onclick=\"jsConfirm()\"]")
    js_prompt_button = (By.XPATH, "//button[@onclick=\"jsPrompt()\"]")
    result_text = (By.ID, "result")
    def click_jsalert_button(self):
        self.chrome.find_element(*self.js_alert_button).click()

    def click_ok_button(self):
        self.chrome.switch_to.alert.accept()

    def you_successfully_clicked_an_alert(self):
        result = self.chrome.find_element(*self.result_text)
        assert result.text == "You successfully clicked an alert"

    def click_jsconfirm_button(self):
        self.chrome.find_element(*self.js_confirm_button).click()

    def you_clicked_ok(self):
        result = self.chrome.find_element(*self.result_text)
        assert result.text == "You clicked: Ok"

    def click_on_the_cancel_button(self):
        self.chrome.switch_to.alert.dismiss()

    def you_clicked_cancel(self):
        result = self.chrome.find_element(*self.result_text)
        assert result.text == "You clicked: Cancel"

    def click_on_the_jsprompt_button(self):
        self.chrome.find_element(*self.js_prompt_button).click()

    def send_text_to_alert(self, text):
        self.chrome.switch_to.alert.send_keys(text)

    def verify_result_name(self, name):
        result = self.chrome.find_element(*self.result_text)
        assert result.text == f"You entered: {name}"

    def you_entered_null(self):
        result = self.chrome.find_element(*self.result_text)
        assert result.text == f"You entered: null"

