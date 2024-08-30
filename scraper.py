from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def write_to_csv(data, filename):
    # Write the data to a CSV file
    with open("data/"+filename, 'w') as f:
        f.write('Pair,Price,% 24h,DEXTscore,Audits,Created,Volume,Swaps,Volatility,Liquidity,T.M.Cap.,DEX\n')
        for item in data:
            f.write(f"{item['Pair']},{item['Price']},{item['% 24h']},{item['DEXTscore']},{item['Audits']},{item['Created']},{item['Volume']},{item['Swaps']},{item['Volatility']},{item['Liquidity']},{item['T.M.Cap.']},{item['DEX']}\n")

# Automatically download and use the correct version of ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to the page
driver.get('https://www.dextools.io/app/en/hot-pairs')

# Wait until the page is fully loaded and JavaScript has run
element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'datatable-body-row'))
)

# check if exist button with class "close", if yes click it
close_button = driver.find_element(By.CSS_SELECTOR, 'button.close')
if close_button:
    close_button.click()

while True:
    # Get the page content
    content = driver.page_source
    soup = BeautifulSoup(content, 'lxml')
    
    # Get the chain list
    select_button = driver.find_element(By.CSS_SELECTOR, 'button.button-selected')
    while True:
        try:
            select_button.click()
            break
        except:
            continue
    time.sleep(0.5)
    chain_items = driver.find_element(By.CSS_SELECTOR, 'div.chain-list.ng-star-inserted').find_elements(By.CSS_SELECTOR, 'a.chain.ng-star-inserted')
    chain_items[0].click()
    chains = {}
    
    # Loop through each item in the chain list
    for i in range(len(chain_items)):
        select_button.click()
        time.sleep(0.5)
        # update item
        item = driver.find_element(By.CSS_SELECTOR, 'div.chain-list.ng-star-inserted').find_elements(By.CSS_SELECTOR, 'a.chain.ng-star-inserted')[i]
        item_title = item.text
        print(f"Scrapping chain: {item_title}")
        
        # Select the chain item
        item.click()
        
        # Wait until the new data is loaded
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'datatable-body-row')))
        time.sleep(0.1)

        # Get pairs data
        rows = soup.find_all('datatable-body-row')
        pairs = {}

        # Loop through each row in the chain content list
        for row in rows:

            # Get the pair title and extra info
            pair_title = row.find('div', class_='pair-title__name')
            extra_info = row.find('div', class_='datatable-row-center datatable-row-group ng-star-inserted')
            cells = extra_info.find_all('datatable-body-cell')

            # Append the pair info to the pairs list
            if pair_title.text.strip() != '???':
                pairs[pair_title.text.strip().split('  ')[0]] = {
                    'Pair': pair_title.text.strip(),
                    'Price': cells[0].text.strip(),
                    '% 24h': cells[1].text.strip(),
                    'DEXTscore': cells[2].text.strip(),
                    'Audits': cells[3].text.strip(),
                    'Created': cells[4].text.strip(),
                    'Volume': cells[5].text.strip(),
                    'Swaps': cells[6].text.strip(),
                    'Volatility': cells[7].text.strip(),
                    'Liquidity': cells[8].text.strip(),
                    'T.M.Cap.': cells[9].text.strip(),
                    'DEX': cells[10].find('img')['src'].split('.')[-2].split('/')[-1]
                }

        # Save the pairs list to the chains dictionary
        chains[item_title] = pairs
        print(f"{item_title} data: {pairs}\n")
        write_to_csv(pairs.values(), f"{item_title}_{int(time.time())}.csv")
        time.sleep(0.1)
    
    # Check if the user wants to continue scrapping
    if input("Do you want to scrap again? (y/n): ") == 'n':
        driver.quit()
        break


