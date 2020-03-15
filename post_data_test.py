import requests
from bs4 import BeautifulSoup

url = 'http://932ddf15.ngrok.io/test?studentID=100&studentName=%E6%96%BD%E4%B8%9E%E5%84%AA'
headers = {'User-Agent': 'test'}

ss = requests.session()
res = ss.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
data = {}
key = soup.select('input')[0]['name']
value = soup.select('input')[0]['value']
data[key] = value
# print(data)
res = ss.post(url, headers=headers, data=data)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())