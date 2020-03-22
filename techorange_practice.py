import requests
from bs4 import BeautifulSoup
import json
import pprint

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

url = 'https://buzzorange.com/techorange/wp-admin/admin-ajax.php'

data_str = """action: fm_ajax_load_more
nonce: 0bb223c976
page: 2"""

data = {i.split(': ')[0]: i.split(': ')[1] for i in data_str.split('\n')}

res = requests.post(url, headers=headers, data=data)
# print(res.text)
jdata = json.loads(res.text)
# pprint.pprint(jdata)
# Get html string
html = jdata['data']
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
title_list = soup.select('h4.entry-title a')
# # print(title_list)
for i in title_list:
    article_title = i.text
    article_url = i['href']
    print(article_title)
    print(article_url)
    print()