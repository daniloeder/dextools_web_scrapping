from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def setup_driver():
    service = Service("path/to/chromedriver")  # Replace with your chromedriver path
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scrape_hot_pairs(driver):
    driver.get("https://www.dextools.io/app/en/hot-pairs")
    time.sleep(5)

    pairs = driver.find_elements(By.CLASS_NAME, 'pair-name')
    prices = driver.find_elements(By.CLASS_NAME, 'pair-price')

    for pair, price in zip(pairs, prices):
        print(f'Pair: {pair.text}, Price: {price.text}')

if __name__ == "__main__":
    driver = setup_driver()
    try:
        scrape_hot_pairs(driver)
    finally:
        driver.quit()
