#python

import json
import requests

response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')

print(response.json())