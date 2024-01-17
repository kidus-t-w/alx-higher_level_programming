#!/usr/bin/python3
import urllib.request
"""Fetches https://alx-intranet.hbtn.io/status"""

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    byte_content = response.read()
    utf8_content = byte_content.decode("utf-8")

    # Print Response
    print("Body response:")
    print("\t- type: {}".format(type(byte_content)))
    print("\t- content: {}".format(byte_content))
    print("\t- utf8 content: {}".format(utf8_content))