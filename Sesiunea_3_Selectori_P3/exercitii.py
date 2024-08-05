from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
#Exercitii XPATH pe site ul formy
chrome = webdriver.Chrome()

chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/form")
chrome.find_element(By.XPATH, "//input[@id=\"first-name\"]").send_keys("Robert")#Adaugam numele Robert la First name