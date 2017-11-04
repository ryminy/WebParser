#!/usr/bin/env python
#  coding=utf-8
# import libraries
import urllib2
from bs4 import BeautifulSoup

def getURL(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    print url
    printProduct(soup)


#Gets Name, Location, Data, ID and Price of an offer from a soup
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
    # Find the string before the date begins.
    startIndex = words.index("La")
    timestamp =  words[startIndex + 1][:-1] + '-' + words[startIndex + 2] + '-' + words[startIndex + 3] + '-' + words[startIndex + 4][:-1]
    print 'Date: ' + timestamp

    #get ID
    UniqueID = str(words[-1])
    print 'ID: ' + UniqueID

    #get price
    price_box = soup.find('div', attrs={'class':'price-label'})
    price = price_box.find('strong')
    print 'Price: ' + price.text.strip()
    print '##########################################################'
    return





