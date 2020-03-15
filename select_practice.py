import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/joke/index.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

res = requests.get(url, headers=headers)
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')

# title = soup.select('a#logo')
title = soup.select('a[id="logo"]')
print(title)

test = soup.select('a[class="right small"]')
print(test)

s = soup.select_one('a[class="right small"]')
print(s)