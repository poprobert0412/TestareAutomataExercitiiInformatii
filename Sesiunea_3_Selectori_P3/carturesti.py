from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random
import time

chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get("https://carturesti.ro")
time.sleep(2)
chrome.find_element(By.XPATH, "//md-menu-item[3]/button").click()
time.sleep(2)
chrome.find_element(By.XPATH, "//a[@class=\"cc-btn cc-allow\"]").click()
chrome.find_element(By.XPATH, "//button[@id=\"loginTrigger\"]").click()
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "Ai pierdut parola?").click()

