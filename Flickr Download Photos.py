# code starts below

import urllib.parse
import urllib.request
import json
import re
import xmltodict
url = 'https://api.flickr.com/services/rest'
values = {'method': 'flickr.photos.search',
          'api_key': 'APIKEY',
          'tags': '',
          'text':'Space',
          'media': 'photos',
          'extras':'url_c',
          'per_page':'500',
          'page':'1',
          'safe_search':'3'}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')  # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
Links = []
from bs4 import BeautifulSoup 
soup = BeautifulSoup(the_page, "html.parser")
photo = [photo for photo in soup.find_all('photo')]
from lxml import etree
i = len(photo)
for x in range(i):
    node = etree.fromstring(str(photo[x]))
    Links.append(node.get('url_c'))
y=0
for link in Links:
    try:
        urllib.request.urlretrieve(link, str(y)+'.jpg')
        print(link)
    except:
        print('None')
    y+=1
