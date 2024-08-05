import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import random

chrome = webdriver.Chrome()
number = random.randint(1, 199999)

chrome.maximize_window()
chrome.get("https://www.elefant.ro/new-account?TargetPipeline=ViewProfileSettings-ViewProfile")
time.sleep(3)
chrome.find_element(By.CSS_SELECTOR, "button[id=\"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll\"]").click()
chrome.find_element(By.CSS_SELECTOR, "div[class*=\"form-group\"] > div[class=\"col-xs-12\"] > div:nth-of-type(2)")
chrome.find_element(By.CSS_SELECTOR, "input[id=\"PostCheckoutRegisterForm_FirstName\"]").send_keys("Robert")
chrome.find_element(By.CSS_SELECTOR, "input[id=\"PostCheckoutRegisterForm_LastName\"]").send_keys("Pop")
chrome.find_element(By.CSS_SELECTOR, "input[id=\"PostCheckoutRegisterForm_Login\"]").send_keys(f"poprobert{number}@yahoo.com")
chrome.find_element(By.CSS_SELECTOR, "input[id=\"PostCheckoutRegisterForm_Password\"]").send_keys("Robert123#")
chrome.find_element(By.CSS_SELECTOR, "input[id=\"PostCheckoutRegisterForm_RetypedPassword\"]").send_keys("Robert123#")
chrome.find_element(By.CSS_SELECTOR, "input[id=\"PostCheckoutRegisterForm_TermsAndConditions\"] + small").click()
chrome.find_element(By.CSS_SELECTOR, "button[class=\"btn btn-primary btn-block\"]").click()
