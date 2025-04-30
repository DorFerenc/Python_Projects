"""
Script Purpose:
- Fetch top 3 headlines for each of the following categories: 'technology', 'science', 'business'
  from both the US and Israel using NewsAPI.
- Combine all the results into a formatted email and send it.
- Designed to avoid rate limiting and support robust logging and environment security.
"""

import requests
import time
import os
from dotenv import load_dotenv
from datetime import datetime
from send_email import send_email

def fetch_top_headlines(api_key, country, category, page_size=3):
    """
    Fetches top headlines from NewsAPI for a given country and category.

    Parameters:
        api_key (str): Your NewsAPI API key
        country (str): ISO 2-letter country code (e.g., 'us', 'il')
        category (str): One of the allowed categories (e.g., 'technology')
        page_size (int): Number of articles to retrieve (default: 3)

    Returns:
        list[dict]: List of article dictionaries
    """
    url = (
        f"https://newsapi.org/v2/top-headlines"
        f"?country={country}&category={category}&apiKey={api_key}&pageSize={page_size}"
    )
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json().get("articles", [])
    except requests.RequestException as e:
        print(f"❌ Failed to fetch headlines for {country}-{category}: {e}")
        return []

def format_articles(articles, country, category):
    """
    Formats the list of articles into a readable string.

    Parameters:
        articles (list): List of article dictionaries
        country (str): Country code for header
        category (str): Category for header

    Returns:
        str: Formatted string block for email body
    """
    if not articles:
        return f"\n===== {country.upper()} - {category.capitalize()} =====\nNo articles found.\n"

    block = f"\n===== {country.upper()} - {category.capitalize()} =====\n"
    for article in articles:
        title = article.get("title", "No Title")
        description = article.get("description", "No Description")
        url = article.get("url", "")
        published = article.get("publishedAt", "")
        block += f"{title}\n{published}\n{description}\n{url}\n\n"
    return block

def main():
    # Load API key and other environment variables
    load_dotenv()
    api_key = os.getenv("API_KEY")
    recipient_email = "bezabuilders@gmail.com"

    if not api_key:
        raise ValueError("API_KEY not found in .env file.")

    countries = ["us", "il"]
    categories = ["technology", "science", "business"]
    body = ""

    print("📡 Starting news aggregation...\n")
    for country in countries:
        for category in categories:
            print(f"Fetching: {country.upper()} - {category}")
            time.sleep(1)  # Avoid rate-limiting
            articles = fetch_top_headlines(api_key, country, category)
            body += format_articles(articles, country, category)

    print("\n✅ All news fetched successfully.")

    # Dynamic subject line with date
    date_str = datetime.now().strftime("%Y-%m-%d")
    subject = f"Top News Summary: US & IL – Tech, Science, Biz ({date_str})"

    # Send the email
    send_email(
        subject=subject,
        body=body,
        to_email=recipient_email
    )
    print("📬 Email sent.")

if __name__ == "__main__":
    main()
