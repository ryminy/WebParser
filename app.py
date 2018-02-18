#!/usr/bin/env python
# coding=utf-8
# import libraries
from parse import startCrawling
from csvClass import csvClass

# specify the url
quote_page = 'https://www.olx.ro/bucuresti/q-geanta-dama/'

csvObj = csvClass("")

startCrawling(quote_page, csvObj)

csvObj.print_csv()