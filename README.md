# Books / Companies Scraper

BeautifulSoup + Pandas scraper that extracts product data from the classic **books.toscrape.com** demo site and exports to multiple formats.

## Features

- Scrapes book name, price & rating
- Cleans whitespace with regex
- Exports to **JSON**, **CSV** and **Excel**
- Proper logging
- Error handling with `raise_for_status`

## Tech Stack

- Python 3
- Requests + BeautifulSoup4
- Pandas + OpenPyXL

## Installation

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

## How to Run

```bash
python companies_scraper.py
```

## Output Files

- `companies.json`
- `companies.csv`
- `companies.xlsx`

## Author

**Ahmad Raza** — Python Automation Engineer  
[GitHub](https://github.com/ahmadraza-automation) · [Portfolio](https://ahmadraza-automation.github.io/Ahmad-Raza-Automation-Portfolio/)
