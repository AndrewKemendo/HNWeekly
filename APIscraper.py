#python

import json
import requests

#request JSON data from HN API
topstories = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')

#write .txt files with top n stories
with open('topstory01.txt','w') as fd:
    fd.write(json.dumps(topstories.json()[0]))

with open('topstory02.txt','w') as fd:
    fd.write(json.dumps(topstories.json()[1]))

with open('topstory03.txt','w') as fd:
    fd.write(json.dumps(topstories.json()[2]))

with open('topstory04.txt','w') as fd:
    fd.write(json.dumps(topstories.json()[3]))

with open('topstory05.txt','w') as fd:
    fd.write(json.dumps(topstories.json()[4]))

#get title and URL for each of the top 30
with open('topstory01.txt', 'r') as myfile:
    data_0 = myfile.read()

new_url_0 = f"https://hacker-news.firebaseio.com/v0/item/{data_0}.json"

with open('topstory02.txt', 'r') as myfile:
    data_1 = myfile.read()

new_url_1 = f"https://hacker-news.firebaseio.com/v0/item/{data_1}.json"

with open('topstory03.txt', 'r') as myfile:
    data_2 = myfile.read()

new_url_2 = f"https://hacker-news.firebaseio.com/v0/item/{data_2}.json"

with open('topstory04.txt', 'r') as myfile:
    data_3 = myfile.read()

new_url_3 = f"https://hacker-news.firebaseio.com/v0/item/{data_3}.json"

with open('topstory05.txt', 'r') as myfile:
    data_4 = myfile.read()

new_url_4 = f"https://hacker-news.firebaseio.com/v0/item/{data_4}.json"

print(new_url_0)
print(new_url_1)
print(new_url_2)
print(new_url_3)
print(new_url_4)


#story1 = requests.get(string_in_string)


#urlparse


#top1 = request.get(https://hacker-news.firebaseio.com/v0/item/{topstoryid1}.json)
#top2 = request.get(https://hacker-news.firebaseio.com/v0/item/{topstoryid2}.json)

#write .txt file named topstories.date.time.txt 
#with open('topstories.{date}.{time}.txt','w') as fd:
    #fd.write(topstories.text)
