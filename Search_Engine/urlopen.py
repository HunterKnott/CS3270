'''Written by professor for assignment'''

import urllib.request

url = 'http://roversgame.net/cs3270/page1.html'

# SEE THE FOLLOWING FOR INFO ABOUT THE User-Agent HEADER:
# https://stackoverflow.com/questions/56101612/python-requests-http-response-406

print("\n### URLLIB.REQUEST")

req = urllib.request.Request(url, headers={'User-Agent' : 'XY'})
response = urllib.request.urlopen(req)
print(response.read().decode())

'''
# REMOVE THE TRIPLE QUOTES (ABOVE AND BELOW) IF YOU HAVE THE 
# requests MODULE INSTALLED AND YOU WANT TO TRY IT.

import requests

print("\n### REQUESTS")
content = requests.get(url, headers={"User-Agent": "XY"}).text
print(content)
'''
