import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

for i in range(0, 3):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    # print(soup.prettify())

    title = soup.select('div[class="title"] a')
    # print(title)
    for t in title:
        print('------')
        try:
            # print(t)
            article_title = t.text
            article_url = 'https://www.ptt.cc' + t['href']
            article_res = requests.get(article_url, headers=headers)
            article_soup = BeautifulSoup(article_res.text, 'html.parser')
            article_content = article_soup.select('div[id="main-content"]')[0]
            print(article_content.text.split('--')[0])
            print(article_title)
            print(article_url)
        except:
            print(t)

    last_page_url = 'https://www.ptt.cc' + soup.select('a[class="btn wide"]')[1]['href']
    url = last_page_url
    # print(last_page_url)