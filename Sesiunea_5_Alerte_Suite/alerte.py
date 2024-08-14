import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options#Problema cu default browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class TestAlerts(unittest.TestCase):
    js_alert_button = (By.XPATH, "//button[@onclick=\"jsAlert()\"]")
    js_confirm_button = (By.XPATH, "//button[@onclick=\"jsConfirm()\"]")
    js_prompt_button = (By.XPATH, "//button[@onclick=\"jsPrompt()\"]")
    result_text = (By.ID, "result")

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        self.chrome = webdriver.Chrome(options=chrome_options)
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")

    def tearDown(self):
        self.chrome.quit()

    def test_jsalert(self):
        self.chrome.find_element(*self.js_alert_button).click()
        self.chrome.switch_to.alert.accept()
        result = self.chrome.find_element(*self.result_text)
        assert result.text == "You successfully clicked an alert"

    def test_jsconfirm_accept(self):
        self.chrome.find_element(*self.js_confirm_button).click()
        self.chrome.switch_to.alert.accept()
        result = self.chrome.find_element(*self.result_text)
        assert result.text == "You clicked: Ok"

    def test_jsconfirm_cancel(self):
        self.chrome.find_element(*self.js_confirm_button).click()
        self.chrome.switch_to.alert.dismiss()
        result = self.chrome.find_element(*self.result_text)
        assert result.text == "You clicked: Cancel"

    def test_jsprompt_accept(self):
        text = "Robert"
        self.chrome.find_element(*self.js_prompt_button).click()
        self.chrome.switch_to.alert.send_keys(text)
        self.chrome.switch_to.alert.accept()
        result = self.chrome.find_element(*self.result_text)
        assert result.text == f"You entered: {text}"

    def test_jspromt_cancel(self):
        self.chrome.find_element(*self.js_prompt_button).click()
        self.chrome.switch_to.alert.dismiss()
        result = self.chrome.find_element(*self.result_text)
        assert result.text == f"You entered: null"
