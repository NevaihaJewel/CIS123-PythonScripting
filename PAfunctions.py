import datetime
import requests
from bs4 import BeautifulSoup

def goodbyeWorld():
    print("Goodbye world")

def checkRange():
    number = int(input("Please enter a number: "))
    if number >= 100:
        print("You entered the number ",number," and it's greater than 100.")
    else:
        print("You entered the number ",number," and your entry is less than 100.")

def daysTillGrad():
    gradDate = input("What's your graduation date? (MM/DD/YYYY): ")
    month, day, year = gradDate.split("/")
    
    Date = datetime.datetime(int(year), int(month), int(day))
    todaysDate = datetime.datetime.now()
    daysTill = Date - todaysDate
    
    print("Today's date is ",todaysDate," and there are ",daysTill," days until graduation!")

def readWeb():
    import urllib.request
    web = urllib.request.urlopen("https://quotes.toscrape.com/page/3/")
    return web
    

def readPDF():
    with open("SimplePDF.pdf", "rb") as pdf:
        print(pdf.read())
