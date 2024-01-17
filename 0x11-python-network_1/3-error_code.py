#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)."""
import sys
import urllib.request
import urllib.error

url_passed_as_argument = sys.argv[1]

try:
    with urllib.request.urlopen(url_passed_as_argument) as response:
        byte_content = response.read()
        utf8_content = byte_content.decode("utf-8")
        print(utf8_content)
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")