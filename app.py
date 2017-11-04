#!/usr/bin/env python
# coding=utf-8
# import libraries
from parse import printProduct
from proxys import FindHits
from parse import *
import urllib2
from bs4 import BeautifulSoup
import time

# specify the url
proxyUrl = "http://31.14.40.113:3128"
quote_page = 'https://www.olx.ro/bucuresti/q-geanta-dama/'

# query the website and return the html to the variable ‘page’
page = FindHits(quote_page, proxyUrl)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

table = soup.find('table',attrs={'id':'offers_table'})

numOffers_box = table.find('p')
numOffers = numOffers_box.text.split()[2]
printedOffers = 0
pageNum = 1

while (printedOffers < numOffers):
    pageNum = pageNum +1

    for x in table.find_all('td',attrs={'class':'offer'}):
        printedOffers = printedOffers + 1
        try:
            # print ID
            table_attrs_dict = x.find('table').attrs
            #print table_attrs_dict['data-id']

            # print Url
            url_attrs_dict = x.find('a').attrs
            #print url_attrs_dict['href']
            getURL(url_attrs_dict['href'])

            #sleep for 2 seconds so that you do not flood the website
            time.sleep(1)

        except:
            print "Ooops"

    #change the URL so that you can move to the next page of offers
    newPage = quote_page + '?page=' + str(pageNum)
    # query the website and return the html to the variable ‘page’
    page = FindHits(newPage, proxyUrl)

    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('table', attrs={'id': 'offers_table'})

    print 'Printed %d out of %s, next page %d' % (printedOffers,numOffers, pageNum)
