#!/usr/bin/env python
# coding=utf-8
# import libraries
from parse import printProduct
from proxys import FindHits
from parse import *
import urllib2
from bs4 import BeautifulSoup

# specify the url
proxyUrl = "http://31.14.40.113:3128"
quote_page = 'https://www.olx.ro/bucuresti/q-geanta-dama/'

# query the website and return the html to the variable ‘page’
page = FindHits(quote_page, proxyUrl)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

table = soup.find('table',attrs={'id':'offers_table'})
for x in table.find_all('td',attrs={'class':'offer'}):
    try:
        # print ID
        table_attrs_dict = x.find('table').attrs
        #print table_attrs_dict['data-id']

        # print Url
        url_attrs_dict = x.find('a').attrs
        #print url_attrs_dict['href']

        UniqueID = getURL(url_attrs_dict['href'])
    except:
        print "Ooops"
