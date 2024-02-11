#!/usr/bin/python3
import sys
import requests

username = "kidus-t-w"
password = "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"

headers = {'Authorization': f'Bearer {password}'}

response = requests.get(f'https://api.github.com/users/{username}', headers=headers)

id = response.json()['id']
print(id)

