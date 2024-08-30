# DEXTools Web Scraper

This is a Python web scraper that gathers data from the [DEXTools Hot Pairs](https://www.dextools.io/app/en/hot-pairs) page. It uses Selenium to automate browsing, BeautifulSoup for parsing HTML, and `webdriver_manager` to manage ChromeDriver installation automatically.

## Features

- Scrapes pair data such as price, DEXTscore, volume, liquidity, and more from DEXTools Hot Pairs.
- Supports scraping from different blockchain chains.
- Saves scraped data into CSV files for further analysis.

## Project Structure

```bash
dextools_web_scrapping/
├── data                  # Folder where the CSV files are saved
├── README.md             # Project README
├── requirements.txt       # Project dependencies
└── scraper.py             # Main scraper script
```

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.6+**: You can download Python from [here](https://www.python.org/downloads/).
- **Google Chrome (latest version)**: Download it from [here](https://www.google.com/chrome/). Make sure to keep Chrome updated, as the scraper uses the latest version for compatibility with the ChromeDriver.
- **pip**: Python's package installer should be installed along with Python, but if not, follow the [pip installation guide](https://pip.pypa.io/en/stable/installation/).

## Installation

1. **Clone the repository:**

   Open a terminal and run:

   ```bash
   git clone https://github.com/daniloeder/dextools_web_scrapping.git
   cd dextools_web_scrapping
   ```

2. **Create a virtual environment:**

   It's a good practice to use a virtual environment to isolate your project dependencies. Run the following commands to create and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install project dependencies:**

   All required Python packages are listed in the `requirements.txt` file. Install them using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure ChromeDriver is installed:**

   The script automatically downloads and manages the correct version of ChromeDriver using `webdriver_manager`, so no manual installation of ChromeDriver is needed.

## Usage

1. **Ensure Google Chrome is up to date.**

   The script will automatically fetch the correct ChromeDriver version based on your installed Chrome version, so keeping Chrome updated ensures compatibility.

2. **Run the scraper:**

   To start the scraping process, simply run the `scraper.py` script:

   ```bash
   python scraper.py
   ```

3. **Follow the terminal prompts:**  
   The script will gather data from DEXTools Hot Pairs and save it in CSV format in the `data/` folder.

### CSV File Structure

Each CSV file will contain the following columns:

| Pair  | Price | % 24h | DEXTscore | Audits | Created | Volume | Swaps | Volatility | Liquidity | T.M.Cap. | DEX |
|-------|-------|-------|-----------|--------|---------|--------|-------|------------|-----------|----------|-----|

- **Pair**: The name of the trading pair.
- **Price**: The current price of the pair.
- **% 24h**: The percentage change in the last 24 hours.
- **DEXTscore**: The DEXT score of the pair.
- **Audits**: Whether the pair has been audited.
- **Created**: When the pair was created.
- **Volume**: The trading volume.
- **Swaps**: The number of swaps.
- **Volatility**: The volatility of the pair.
- **Liquidity**: The available liquidity.
- **T.M.Cap.**: The total market capitalization.
- **DEX**: The decentralized exchange platform (retrieved via an image source in the page).

## Troubleshooting

- **Google Chrome version:** Ensure you have the latest version of Google Chrome installed.
- **CSS Selector changes:** If the script fails to find elements on the page, check if the DEXTools website structure has changed. You may need to update the CSS selectors in `scraper.py`.
