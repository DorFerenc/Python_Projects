"""
Script Purpose:
- Fetch the HTML content of the Yahoo Finance homepage.
- Handle basic rate-limiting by adding a delay.
- Set proper headers to avoid getting blocked with a 429 error.
"""

import requests  # Library to make HTTP requests
import time       # Library to add delays (sleep)
import os         # Library to access environment variables
from dotenv import load_dotenv  # Library to load variables from a .env file

# URL of the target webpage
# url = "https://finance.yahoo.com

load_dotenv() # Load environment variables from a .env file
API_KEY = os.getenv("API_KEY")
url = "https://newsapi.org/v2/everything?q=tesla&" \
        "from=2025-03-26&sortBy=publishedAt&" \
        f"apiKey={API_KEY}"

# HTTP headers to simulate a real web browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Adding a delay to avoid being flagged for sending requests too quickly
# This is especially important when scraping multiple pages
time.sleep(1)

request = requests.get(url, headers=headers) # Make an HTTP GET request to the target URL with the headers

if request.status_code == 200: # Check if the request was successful (HTTP status code 200)
    content = request.text  # Get the HTML content as text
    content_json = request.json()  # Parse the JSON response
    print(type(content_json))
    print(content_json['articles'][0]['title'])  # Print the title of the first article
    for article in content_json['articles']:
        print(article['title'])
else:
    # If the server responds with an error code, print the error
    print(f"Error: {request.status_code}")
