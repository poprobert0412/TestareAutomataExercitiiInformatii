from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random
import time
#Exercitii XPATH pe site ul formy
chrome = webdriver.Chrome()

chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/form")
chrome.find_element(By.XPATH, "//input[@id=\"first-name\"]").send_keys("Robert")#Adaugam prenumele Robert la First name
chrome.find_element(By.XPATH, "//input[@id=\"last-name\" and @placeholder=\"Enter last name\"]").send_keys("Pop")#Adaugam numele de Pop
chrome.find_element(By.XPATH, "//input[@id=\"job-title\"]").send_keys("QA")#Adaugam job title
chrome.find_element(By.XPATH, "//input[@id=\"radio-button-1\"]").click()
chrome.find_element(By.XPATH, "//input[@id=\"checkbox-1\"]").click()
chrome.find_element(By.XPATH, "//input[@id=\"datepicker\"]").send_keys("08/29/1999")

drop_down = Select(chrome.find_element(By.XPATH, "//select[@id=\"select-menu\"]"))
drop_down.select_by_value(value="1")
job_title = chrome.find_element(By.XPATH, "//input[@id=\"job-title\"]/preceding-sibling::strong/label")

assert job_title, "Job title"
chrome.find_element(By.XPATH, "//a[contains(text(), \"Submit\")]").click()#Submit button
time.sleep(2)
test_finish_text = chrome.find_element(By.XPATH, "//h1[contains(text(), \"Thanks for submitting your form\")]")
assert test_finish_text, "Thanks for submitting your form"#Verificam textul de pe urmatoarea pagina sa vedem daca am terminat taste case ul fara probleme

