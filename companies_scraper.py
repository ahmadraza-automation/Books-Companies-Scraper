"""
Companies / Books Scraper
Scrapes product data from books.toscrape.com (demo site)
and exports to JSON, CSV and Excel.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import logging
import re

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def scrape_books(url: str = "https://books.toscrape.com") -> list[dict]:
    logger.info("Starting scrape: %s", url)

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")

    data = []
    for book in books:
        name = book.h3.a.get("title", "").strip()
        name = re.sub(r"\s+", " ", name)

        price_el = book.select_one(".price_color")
        price = price_el.text.strip() if price_el else "N/A"

        rating_el = book.select_one("p.star-rating")
        rating = rating_el.get("class", [""])[1] if rating_el else "N/A"

        data.append({
            "name": name,
            "price": price,
            "rating": rating,
            "category": "Books",
            "source": "books.toscrape.com"
        })

    logger.info("Scraped %d items", len(data))
    return data


def save_outputs(data: list[dict]):
    # JSON
    with open("companies.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    logger.info("Saved companies.json")

    # CSV + Excel
    df = pd.DataFrame(data)
    df.to_csv("companies.csv", index=False)
    logger.info("Saved companies.csv")

    df.to_excel("companies.xlsx", index=False)
    logger.info("Saved companies.xlsx")

    print("\n--- Preview ---")
    print(df.head())
    print(f"\nTotal records: {len(df)}")


if __name__ == "__main__":
    try:
        records = scrape_books()
        save_outputs(records)
        logger.info("Program completed successfully")
    except Exception as e:
        logger.error("Failed: %s", e)
        raise
