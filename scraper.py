
import requests
from bs4 import BeautifulSoup

# Example URL to scrape
url = "https://quotes.toscrape.com/"

# Send a GET request to the website
response = requests.get(url)

# Parse the content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Example: Extract quotes from the page
quotes = soup.find_all('span', class_='text')

# Print the quotes
for quote in quotes:
    print(quote.text)
