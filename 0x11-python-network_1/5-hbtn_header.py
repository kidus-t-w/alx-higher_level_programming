#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the 
value of the variable X-Request-Id in the response header"""
import sys
import requests

url_form_argument = sys.argv[1]

response = requests.get(url_form_argument)
headers = response.headers # Got the headers

x_request_id = headers["X-Request-Id"]
print(x_request_id)