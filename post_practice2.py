import requests
from bs4 import BeautifulSoup

url = 'https://web.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=advance'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

post_data_str = """method: search
searchMethod: true
searchTarget: ATM
orgName: 
orgId: 
hid_1: 1
tenderName: 
tenderId: 
tenderStatus: 5,6,20,28
tenderWay: 
awardAnnounceStartDate: 109/03/13
awardAnnounceEndDate: 109/03/15
proctrgCate: 
tenderRange: 
minBudget: 
maxBudget: 
item: 
hid_2: 1
gottenVendorName: 
gottenVendorId: 
hid_3: 1
submitVendorName: 
submitVendorId: 
location: 
execLocationArea: 
priorityCate: 
isReConstruct: 
btnQuery: 查詢"""

data = {}
for r in post_data_str.split('\n'):
    key = r.split(': ')[0]
    value = r.split(': ')[1]
    data[key] = value
print(data)

res = requests.post(url, headers=headers, data=data)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())