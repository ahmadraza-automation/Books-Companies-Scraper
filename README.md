# Books / Companies Scraper

BeautifulSoup + Pandas scraper that extracts product data from the classic **books.toscrape.com** demo site and exports to multiple formats.

## Features
- Scrapes book name, price & rating
- Cleans whitespace with regex
- Exports to **JSON**, **CSV** and **Excel**
- Proper logging
- Error handling with `raise_for_status`

## Requirements
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

## Screenshots
> Add terminal output + Excel/CSV preview screenshots

## Video Demo
> Record short demo of running the scraper and opening the Excel file

---
Made by [Ahmad Raza](https://github.com/ahmadraza-automation)
