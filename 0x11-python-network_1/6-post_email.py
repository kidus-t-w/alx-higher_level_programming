#!/usr/bin/python3
""" takes in a URL and an email address, sends a POST request to the passed URL with 
the email as a parameter, and finally displays the body of the response."""
import sys
import requests

if name == __main__ 
    url_from_argument = sys.argv[1]
    email_from_argument = sys.argv[2]

    response = requests.post(url_from_argument, 
        data={"email": email_from_argument},
        headers={"Content-Type": "text/plain"},
    )

    print(response.text)
