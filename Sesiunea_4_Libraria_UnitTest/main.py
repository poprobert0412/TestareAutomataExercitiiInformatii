import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options#Problema cu default browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestElefant(unittest.TestCase):
    def setUp(self):
        #Cod la initierea testului
        self.chrome = webdriver.Chrome()
        #self.chrome.minimize_window()
        self.chrome.get("https://www.elefant.ro")

    def tearDown(self):
        self.chrome.quit()#"""Closes the browser and shuts down the ChromiumDriver executable."""
        #Metoda de log out
        #Cod pentru executare la finalul testului

    def test_search_products(self):
        #Trebuie sa inceapa test_
        time.sleep(4)
        self.chrome.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
        self.chrome.find_element(By.XPATH, "//input[@name=\"SearchTerm\"]").send_keys("iphone 14")
        self.chrome.find_element(By.XPATH, "//button[contains(@class, \"btn-search\")]").click()
        time.sleep(4)
        produse = self.chrome.find_elements(By.CLASS_NAME, "product-title")#Avanmd 3 elemente scriem find_elements
        assert len(produse) == 3 #Facema assert doar cand stim rezultatul testului
        #SAU assert len(produse), 3 / Dupa aceea virgula o sa ne scrie in consola un mesaj. Depinde ce mesaj dorim sa ii punem

    def test_search_products_with_waits(self):
        WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(
            (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')))
        self.chrome.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
        self.chrome.find_element(By.XPATH, "//input[@name=\"SearchTerm\"]").send_keys("iphone 14")
        self.chrome.find_element(By.XPATH, "//button[contains(@class, \"btn-search\")]").click()
        self.chrome.implicitly_wait(6)#Asteapta 3 secunde sa se incarce elementele de mai jos
        produse = self.chrome.find_elements(By.CLASS_NAME, "product-title")  # Avanmd 3 elemente scriem find_elements
        assert len(produse) == 3
