#python

import json
import requests
import io

#request JSON data from HN API
topstories = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')

#write .txt file named topstories.txt 
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

with open('topstory06.txt','w') as fd:
      fd.write(json.dumps(topstories.json()[5]))

with open('topstory07.txt','w') as fd:
      fd.write(json.dumps(topstories.json()[6]))

with open('topstory08.txt','w') as fd:
      fd.write(json.dumps(topstories.json()[7]))

with open('topstory09.txt','w') as fd:
      fd.write(json.dumps(topstories.json()[8]))

with open('topstory10.txt','w') as fd:
      fd.write(json.dumps(topstories.json()[9]))

#get title and URL for each of the top 30


#top1 = request.get(https://hacker-news.firebaseio.com/v0/item/{topstoryid1}.json)
#top2 = request.get(https://hacker-news.firebaseio.com/v0/item/{topstoryid2}.json)

#write .txt file named topstories.date.time.txt 
#with open('topstories.{date}.{time}.txt','w') as fd:
    #fd.write(topstories.text)
