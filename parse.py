#!/usr/bin/env python
#  coding=utf-8
# import libraries
import urllib2
from bs4 import BeautifulSoup

import time

from proxys import FindHits

proxyUrl = "http://31.14.40.113:3128"
debugOfferValue = 2

def getURL(url,csvObj):

    page = FindHits(url,"")
    soup = BeautifulSoup(page, 'html.parser')

    printProduct(soup,url,csvObj)


#Gets Name, Location, Data, ID and Price of an offer from a soup
def printProduct(soup,url,csvObj):
    #print url
    print url

    #get name
    name_box = soup.find('h1')
    name = name_box.text.strip()
    print 'Name: ' + name

    #get location
    location_box = soup.find('a', attrs={'class':'show-map-link'})
    location = location_box.find('strong')
    locationText = location.text.strip()
    print 'Location: ' + locationText

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
    priceText = price.text.strip()
    print 'Price: ' + priceText
    print '##########################################################'

    #fieldnames = ["ID", "PRICE", "DATE", "NAME", "LOCATION", "URL"]
    #encode each string as it will be converted from unicode to ascii
    csvObj.csv_write([UniqueID.encode(), priceText.encode(), timestamp.encode(), name.encode(), locationText.encode(), url.encode()])
    return

def startCrawling(quote_page, csvObj):
    # query the website and return the html to the variable ‘page’
    page = FindHits(quote_page,"")

    #page = urllib2.urlopen(quote_page)
    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    table = soup.find('table', attrs={'id': 'offers_table'})

    numOffers_box = table.find('p')
    numOffers = numOffers_box.text.split()[2]
    printedOffers = 0
    pageNum = 1

    #debug purpose
    if debugOfferValue > 0:
        maxOffers = debugOfferValue
    else:
        maxOffers = int(numOffers)

    while (printedOffers < maxOffers):
        pageNum = pageNum + 1

        for x in table.find_all('td', attrs={'class': 'offer'}):
            printedOffers = printedOffers + 1

            if printedOffers > maxOffers:
                break
            print 'Printing %d out of %s, next page %d' % (printedOffers, numOffers, pageNum)

            try:
                # print ID
                # table_attrs_dict = x.find('table').attrs
                # print table_attrs_dict['data-id']

                # print Url
                url_attrs_dict = x.find('a').attrs
                getURL(url_attrs_dict['href'],csvObj)

                # sleep for 2 seconds so that you do not flood the website
                time.sleep(5)
                # exit()

            except Exception as e:
                print "Ooops"
                print e

        # change the URL so that you can move to the next page of offers
        newPage = quote_page + '?page=' + str(pageNum)
        # query the website and return the html to the variable ‘page’
        page = FindHits(newPage, proxyUrl)

        # parse the html using beautiful soap and store in variable `soup`
        soup = BeautifulSoup(page, 'html.parser')
        table = soup.find('table', attrs={'id': 'offers_table'})

      #  csvObj.write_to_csv()


