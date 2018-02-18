#!/usr/bin/env python
import urllib2

def FindHits(url, proxyUrl):

    if len(proxyUrl) > 0:
        # Proxy set up
        proxy = urllib2.ProxyHandler({'http': proxyUrl})

        # Create an URL opener utilizing proxy
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)

        # Aquire data from URL
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
    else:
        # Aquire data from URL
        request_headers = {
            "Accept-Language": "en-US,en;q=0.5",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Referer": "http://thewebsite.com",
            "Connection": "keep-alive"
        }
        request = urllib2.Request(url, headers = request_headers)
        response = urllib2.urlopen(request)

        #response = urllib2.urlopen(url)

    return response