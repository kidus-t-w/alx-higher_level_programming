#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value of
    the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request

url_passed = sys.argv[1]

with urllib.request.urlopen(url_passed) as response:
    # Get all the headers as a list of (header, value) tuples
    headers = response.getheaders()
    # print(headers)
    for v in headers:
        header, value = v
        if header == "X-Request-Id":
            print(value)
