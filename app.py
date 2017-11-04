#!/usr/bin/env python
# coding=utf-8
# import libraries
from parse import startCrawling
from data import read_csv

# specify the url
quote_page = 'https://www.olx.ro/bucuresti/q-geanta-dama/'

#startCrawling(quote_page)

reader = read_csv()
print reader
for line in reader:
    print line