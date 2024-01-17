#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""
import sys
import urllib.request
import urllib.parse

url_passed_as_argument = sys.argv[1]
email_passed_as_argument = sys.argv[2]

data = {
    'email' : email_passed_as_argument,
}

data_encoded = urllib.parse.urlencode(data)
data_bytes = data_encoded.encode('utf-8')

with urllib.request.urlopen(url_passed_as_argument, data=data_bytes) as response:
    content = response.read()
    print(content)
