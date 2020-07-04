#python

import json
import requests

#request JSON data from HN API
topstories = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')

#write .txt file named topstories.txt 
with open('topstories.txt','w') as fd:
    fd.write(topstories.text)

#List only top 30
#topstories[:30}
#id1
#id2
#id3

#get title and URL for each of the top 30
#top1 = request.get(https://hacker-news.firebaseio.com/v0/item/{topstoryid1}.json)
#top2 = request.get(https://hacker-news.firebaseio.com/v0/item/{topstoryid2}.json)

#write .txt file named topstories.date.time.txt 
#with open('topstories.{date}.{time}.txt','w') as fd:
    fd.write(topstories.text)
