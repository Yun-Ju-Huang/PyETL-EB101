import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

url = 'https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'

ss = requests.session()
res = ss.get(url, headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
url_over18 = 'https://www.ptt.cc' + soup.select('form')[0]['action']
data = {'yes': 'yes'}
ss.post(url_over18, headers=headers, data=data)
url_target = 'https://www.ptt.cc/bbs/Gossiping/index.html'
res = ss.get(url_target, headers=headers)
print(res.text)