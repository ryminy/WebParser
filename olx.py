# coding=utf-8
# import libraries
import urllib2
from bs4 import BeautifulSoup

def printProduct(soup):
    #get name
    name_box = soup.find('h1')
    name = name_box.text.strip()
    print 'Name: ' + name

    #get location
    location_box = soup.find('a', attrs={'class':'show-map-link'})
    location = location_box.find('strong')
    print 'Location: ' + location.text.strip()

    #get timestamp
    timestamp_box = soup.find('em')
    words = timestamp_box.text.strip().split()
    timestamp =  words[2][:-1] + '-' + words[3] + '-' + words[4] + '-' + words[5][:-1]
    print 'Date: ' + timestamp

    #get ID
    UniqueID = str(words[-1])
    print 'ID: ' + UniqueID

    #get price
    price_box = soup.find('div', attrs={'class':'price-label'})
    price = price_box.find('strong')
    print 'Price: ' + price.text.strip()
    return

# specify the url
quote_page = 'https://www.olx.ro/oferta/poseta-geanta-dama-chloe-ID9sIwl.html'

# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

printProduct(soup)



