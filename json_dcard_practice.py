import requests
from bs4 import BeautifulSoup
import json
import pprint
from urllib import request
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
import time
import random

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

url = 'https://www.dcard.tw/service/api/v2/forums/dressup/posts?limit=30&before=233303602'

# res = requests.get(url, headers=headers)
# pprint.pprint(res.text)

## Read file
with open('jsfile.txt', 'r') as f:
    res = f.read()

jdata = json.loads(res)
# pprint.pprint(jdata[0])

# for k in jdata[0]:
#     print(k)
for t in jdata:
    article_title = t['title']
    article_url = 'https://www.dcard.tw/f/dressup/p/' + str(t['id'])
    print(article_title)
    print(article_url)
    for img in t['mediaMeta']:
        img_url = img['url']
        print('\t', img_url)
        c = 0
        status = 0
        while c < 5:
            try:
                request.urlretrieve(img_url, './dcard_img/' + img_url.split('/')[-1])
                status = 1
            except :
                time.sleep(random.randint(3,10))
                try:
                    request.urlretrieve(img_url, './dcard_img/' + img_url.split('/')[-1])
                except:
                    continue
                status = 1
            if status == 1:
                break
            c += 1
# print(jdata[0]['mediaMeta'][0]['url'])