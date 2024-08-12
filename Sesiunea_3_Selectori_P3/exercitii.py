from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Test 1: Open the website and accept cookies
    driver.get("https://www.elefant.ro/")

    # Wait for the cookie acceptance button to be present and click it
    try:
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept')]"))
        )
        accept_cookies_button.click()
        print("Test 1 Passed: Cookies accepted.")
    except TimeoutException:
        print("Test 1 Failed: Cookies acceptance button not found.")

    # Test 2: Search for a product (e.g., iPhone 14) and verify at least 10 results
    search_box = driver.find_element(By.NAME, "SearchTerm")
    search_box.send_keys("iphone 14")
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load and check the number of results
    try:
        products = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product-title"))
        )
        if len(products) >= 10:
            print("Test 2 Passed: At least 10 products found.")
        else:
            print(f"Test 2 Failed: Only {len(products)} products found.")
    except TimeoutException:
        print("Test 2 Failed: Product titles not found.")

    # Test 3: Find the product with the lowest price
    try:
        prices = driver.find_elements(By.CLASS_NAME, "current-price")
        product_images = driver.find_elements(By.XPATH, "//img[@class='product-image']")

        # Extract prices as numbers
        price_numbers = [float(price.text.replace(',', '.').replace('Lei', '').strip()) for price in prices]

        # Find the index of the minimum price
        min_price_index = price_numbers.index(min(price_numbers))

        # Output the image source of the product with the lowest price
        min_price_image_src = product_images[min_price_index].get_attribute('src')
        print(f"Test 3 Passed: Product with the lowest price has image source: {min_price_image_src}")
    except Exception as e:
        print(f"Test 3 Failed: {str(e)}")

finally:
    # Close the browser
    driver.quit()
