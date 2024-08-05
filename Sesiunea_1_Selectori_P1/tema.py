import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
#1
chrome.maximize_window()
#2
chrome.get("https://www.elefant.ro/apa-de-toaleta-cacharel-amor-amor-100-ml-pentru-femei_7d9ee177-9e5b-4207-9ca6-4ba4cf5222b7")
#3
# chrome.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()#Click pe cookie
chrome.find_element(By.XPATH, "//div[@class='product-price vendor-offer-data js-vendor-price']")
#4

titlu = chrome.find_element(By.XPATH, "//h2[@class='product-brand']")

assert titlu.text, 'CACHAREL'

#5
time.sleep(3)
chrome.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()#Click pe cookie
chrome.find_element(By.XPATH, "//span[@class='login-prompt js-login-prompt']").click()
chrome.find_element(By.XPATH, "//a[@class='my-account-login btn btn-primary btn-block']").click()
#Introducere user si parola
chrome.find_element(By.ID, "ShopLoginForm_Login").send_keys("asdasasdasd123123124124@yahoo.com")#Introducere email incorect
chrome.find_element(By.ID, "ShopLoginForm_Password").send_keys("asdasdasdadsdas213123")#Introducere parola incorecta
chrome.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
#6
#Stergere valoare si introducere o valoare invalida
cleared_email = chrome.find_element(By.ID, "ShopLoginForm_Login")
cleared_email.clear()
chrome.find_element(By.ID, "ShopLoginForm_Login").send_keys("asdasasdasd123123124124yahoo.com")

is_enabled = chrome.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").is_enabled()

print(f"Login button is {'enabled' if is_enabled else 'disabled'} with invalid email.")