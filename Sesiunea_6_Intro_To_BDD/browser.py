from selenium import webdriver
from selenium.webdriver.chrome.options import Options#Problema cu default browser

class Browser:
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome = webdriver.Chrome(options=chrome_options)
    #driver.maximize_window()

    def close(self):
        self.chrome.quit()

