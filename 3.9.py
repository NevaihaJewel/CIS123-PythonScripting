import requests
from bs4 import BeautifulSoup

def scrape_quotes(page_number):
    url = "https://quotes.toscrape.com/page/2/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    quotes = soup.find_all("span", class_="text")
    for quote in quotes:
        print(quote.text)

page_number = int(input("Enter a page number (1-10): "))
scrape_quotes(page_number)
