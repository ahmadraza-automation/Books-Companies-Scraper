# Books / Companies Scraper

BeautifulSoup + Pandas scraper that extracts product data from the classic **books.toscrape.com** demo site and exports to **JSON, CSV & Excel**.

**Status:** Fully tested and working ✅  
**Author:** [Ahmad Raza](https://github.com/ahmadraza-automation)

---

## Features

- Scrapes book name, price & rating
- Correct Unicode handling (prices show £ correctly)
- Exports to **JSON**, **CSV** and professionally formatted **Excel**
- Clean logging
- Error handling with `raise_for_status`

---

## Sample Output

| name | price | rating |
|------|-------|--------|
| A Light in the Attic | £51.77 | Three |
| Tipping the Velvet | £53.74 | One |
| Soumission | £50.10 | One |
| Sharp Objects | £47.82 | Four |
| Sapiens: A Brief History of Humankind | £54.23 | Five |

---

## Tech Stack

- Python 3
- Requests + BeautifulSoup4
- Pandas + OpenPyXL

---

## Installation

```bash
pip install -r requirements.txt
```

---

## How to Run

```bash
python companies_scraper.py
```

Output files appear in the `output/` folder:

- `companies.json`
- `companies.csv`
- `companies.xlsx` (formatted with filters + frozen header)

---

## Author

**Ahmad Raza** — Python Automation Engineer  
[GitHub](https://github.com/ahmadraza-automation) · [Portfolio](https://ahmadraza-automation.github.io/Ahmad-Raza-Automation-Portfolio/)
