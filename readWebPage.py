import requests
from bs4 import BeautifulSoup

print("nevada3921")

def readwebpage(url):
    output = requests.get(url)
    return(output)

def parsehtml(html):
    parsed = BeautifulSoup(html.content, 'html.parser')
    return parsed

def outputquotes(parsed):
    quotes = parsed.find_all("div", class_="quote")
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        print(text, author)


url = "http://quotes.toscrape.com"
html = readwebpage(url)
parsed = parsehtml(html)
outputquotes(parsed)
print(parsed.text)
