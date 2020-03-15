import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.prettify())

title = soup.select('div[class="title"]')
# print(title)
for t in title:
    print('------')
    try:
        print(t)
        article_title = t.select('a')[0].text
        article_title = t.a.text
        article_url = 'https://www.ptt.cc' + t.select('a')[0]['href']
        print(article_title)
        print(article_url)
    except:
        print(t)