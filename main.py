import sqlite3
import requests
from bs4 import BeautifulSoup
import logging
from datetime import datetime
import pandas as pd

# Logging setup
logging.basicConfig(
    filename='scraping.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Stream handler to log to the terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logging.getLogger().addHandler(console_handler)

# Connect to SQLite database
connection = sqlite3.connect('scraped_data.db')
cursor = connection.cursor()

# Create table 
cursor.execute('''CREATE TABLE IF NOT EXISTS stocks
                  (symbol TEXT, name TEXT, price TEXT, change TEXT, percent_change TEXT, volume TEXT, avg_vol_3_months TEXT, market_cap TEXT, pe_ratio_ttm TEXT)''')

def fetch_page(offset):
    url = f"https://finance.yahoo.com/most-active/?count=25&offset={offset}"
    headers = {
        "User-Agent": "replace_with_your_user_agent_here" 
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching page {offset}: {e}")
        return None

def parse_table(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', {'class': 'W(100%)'})
        if not table:
            logging.error("No table found on the page")
            return []

        rows = table.find_all('tr')[1:] 
        data = []
        for row in rows:
            cols = row.find_all('td')
            # Exclude the column with <canvas> elements
            cols = [ele.text.strip() for ele in cols if not ele.find('canvas')]
            data.append(cols)
        return data
    except Exception as e:
        logging.error(f"Error parsing table: {e}")
        return []

def main():
    logging.info("Starting scraping process")
    start_time = datetime.now()

    all_data = []
    for offset in range(0, 200, 25):  # Adjust the range and step to fetch all pages
        logging.info(f"Fetching page with offset {offset}")
        html = fetch_page(offset)
        if html:
            data = parse_table(html)
            all_data.extend(data)

    # Log number of data scraped
    num_data_scraped = len(all_data)
    logging.info(f"Number of data scraped: {num_data_scraped}")

    # Save data to CSV
    csv_filename = 'most_active_stocks.csv'
    columns = ['Symbol', 'Name', 'Price', 'Change', '% Change', 'Volume', 'Avg Vol (3 months)', 'Market Cap', 'PE Ratio (TTM)']
    df = pd.DataFrame(all_data, columns=columns)
    df.to_csv(csv_filename, index=False)
    logging.info(f"CSV filename: {csv_filename}")

    # Save data to SQLite database
    for row in all_data:
        cursor.execute('''INSERT INTO stocks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', row)
    connection.commit()
    logging.info("Data saved to SQLite database")

    end_time = datetime.now()
    duration = end_time - start_time
    logging.info(f"Scraping process completed in {duration}")

if __name__ == "__main__":
    main()
