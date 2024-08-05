import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
#Exercitii CSS SELECTOR si XPATH
chrome = webdriver.Chrome()
number = random.randint(1, 199999)

chrome.maximize_window()
chrome.get("https://www.emag.ro")
chrome.find_element(By.CSS_SELECTOR, "input[id=\"searchboxTrigger\"]").send_keys("Iphone 15 pro max")
chrome.find_element(By.CSS_SELECTOR, "button[class*=\"searchbox-submit\"]").click()
chrome.find_element(By.CSS_SELECTOR, "div[class*=\"card-item\"]:nth-of-type(3)").click()
chrome.find_element(By.CSS_SELECTOR, "a[title=\"512 GB\"]").click()
chrome.find_element(By.CSS_SELECTOR, "div[class=\"product-buy-area-wrapper\"] > div > button[type=\"submit\"]").click()
time.sleep(2)
chrome.find_element(By.XPATH, "//a[contains(text(), \"Vezi detalii cos\")]").click()
time.sleep(2)

pret = chrome.find_element(By.XPATH, "//div[@class=\"order-summary-total\"] / p[contains(text(), \"7.549\")]")

assert pret, "7.549"

