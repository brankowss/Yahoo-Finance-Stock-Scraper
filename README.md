# Yahoo Finance Stock Scraper

## Overview

This project demonstrates a very simple web scraping script written in Python using the BeautifulSoup library to scrape data from Yahoo Finance's most active stocks page and saves it to both a CSV file and a SQLite database.

## Description

The script fetches data from Yahoo Finance's most active stocks page, parses the HTML using BeautifulSoup, and extracts relevant information such as symbol, name, price, change, volume, etc. The extracted data is then saved to a CSV file and SQLite3 database. I used this table as an example, and the website has many similar tables available, demonstrating the fast data extraction process.


## Requirements

- Python 3.x
- BeautifulSoup4
- Pandas
- Requests

## Setup Instructions

Create a virtual environment:
```
python3 -m venv venv
```
Activate the virtual environment:

On macOS and Linux:
```
source venv/bin/activate
```
On Windows:
```
venv\Scripts\activate
```

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/brankowss/Yahoo-Finance-Stock-Scraper.git
    ```

2. Navigate to the project directory:

    ```
    cd yahoo-finance-scraper
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

Run the main script to perform the scraping:

```
python main.py
```

## Configuration

Customize the script by modifying the following parameters:

- range(0, 200, 25): Adjust the range and step in the main() function to control the number of pages to scrape.
- csv_filename: Change the name of the CSV file where the data will be saved.
- headers["User-Agent"]: Modify the User-Agent header in the fetch_page() function to match your preferred user agent.

## Logging

The script logs information about the scraping process to a log file (scraping.log) and displays it in the terminal. You can view detailed information about the scraping process, including errors and the duration of the process, in the log file.

## Scrape Statistics

- 2024-06-09 20:10:35,556 - INFO - Number of data scraped: 200
- 2024-06-09 20:10:35,558 - INFO - CSV filename: most_active_stocks.csv
- 2024-06-09 20:10:35,596 - INFO - Data saved to SQLite database
- 2024-06-09 20:10:35,596 - INFO - Scraping process completed in 0:00:09.749470






 