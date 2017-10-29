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
        response = urllib2.urlopen(url)

    return response