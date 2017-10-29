# coding=utf-8
# import libraries
from parse import printProduct
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.olx.ro/oferta/poseta-geanta-dama-chloe-ID9sIwl.html'

# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

printProduct(soup)