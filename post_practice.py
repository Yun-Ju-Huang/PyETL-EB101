import requests
from bs4 import BeautifulSoup

url = 'http://baae0774.ngrok.io/hello_post'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# To get the key of form data
form_key = soup.select('input')[0]['name']
data = {form_key: 'Allen'}

# Request again with post method
res = requests.post(url, data=data)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())