from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
#Exercitii XPATH
chrome = webdriver.Chrome()

chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/form")
