import requests

url = 'https://megapx-assets.dcard.tw/images/f2f56bbf-07ce-48e0-8ce8-dca9f721f56e/full.jpeg'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
res = requests.get(url)
with open('./test.jpeg', 'wb')as f:
    f.write(res.content)

