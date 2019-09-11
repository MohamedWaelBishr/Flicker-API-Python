#Astrophotography - The Solar System and Beyond  #https://www.flickr.com/groups/2657450@N23/
#Pictures Of The International Space Station (ISS)  #https://www.flickr.com/groups/spacestation
# code starts below

import urllib.parse
import urllib.request
import json
import re
import xmltodict
url = 'https://api.flickr.com/services/rest'
values = {'method': 'flickr.urls.lookupGroup',
          'api_key': 'APIKEY',
          #'tags': '',
          #'text': '',
          #'media': 'photos',
          #'extras': 'url_c',
          #'per_page': '100',
          #'page': '1',
          #'group_id': '81019155@N00',
          'url': 'https://www.flickr.com/groups/spacestation'
          #'auth_token': 'AUTHTOKEN',
          #'api_sig': 'APISIG',
          #'safe_search': '3'
          }

data = urllib.parse.urlencode(values)
data = data.encode('ascii')  # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()

#print(the_page)
Links = []
from bs4 import BeautifulSoup
soup = BeautifulSoup(the_page, "html.parser")
photo = [photo for photo in soup.find_all('group')]
from lxml import etree
i = len(photo)
for x in range(i):
    node = etree.fromstring(str(photo[x]))
    Links.append(node.get('id'))
y = 0
for link in Links:
    try:
        print(link)
    except:
        print('None')
    y += 1
