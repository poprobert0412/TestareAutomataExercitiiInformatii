import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import random

chrome = webdriver.Chrome()
nr = random.randint(1, 9999999)

chrome.maximize_window()
chrome.get("https://www.elefant.ro/new-account?TargetPipeline=ViewProfileSettings-ViewProfile")
chrome.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
chrome.find_element(By.XPATH, "//div[@class='radio radio-inline'][2]/label").click()
chrome.find_element(By.ID, 'PostCheckoutRegisterForm_FirstName').send_keys('Robert')
chrome.find_element(By.ID, 'PostCheckoutRegisterForm_LastName').send_keys('Pop')
chrome.find_element(By.NAME, 'PostCheckoutRegisterForm_Login').send_keys(f'poprobert{nr}@yahoo.com')
chrome.find_element(By.ID, 'PostCheckoutRegisterForm_Password').send_keys('Robert321@')
chrome.find_element(By.ID, 'PostCheckoutRegisterForm_RetypedPassword').send_keys('Robert321@')
chrome.find_element(By.XPATH, "//input[@id='PostCheckoutRegisterForm_TermsAndConditions']/following-sibling::small").click()
chrome.find_element(By.NAME, 'login').click()
# chrome.find_element(By.CLASS_NAME, "btn btn-primary btn-block").click()
# chrome.find_element(By.CLASS_NAME, "btn btn-primary select-all").click()

last_item = chrome.find_element(By.XPATH, "//div[@class='errorpage-cta row']/h3")

assert last_item.text, 'Ne pare rau, pagina nu a fost gasita!'

path_tigi = chrome.find_element(By.LINK_TEXT, "TIGI")
chrome.execute_script("arguments[0].scrollIntoView(true);", path_tigi)
chrome.find_element(By.PARTIAL_LINK_TEXT, "TIG").click()
text_tigi = chrome.find_element(By.XPATH, "//h1[@class='current-category-name']")

time.sleep(5)

assert text_tigi.text, 'Cosmetice Tigi'