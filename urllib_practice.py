from urllib import request
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

url = 'https://www.ptt.cc/bbs/joke/index.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

req = request.Request(url, headers=headers)

res = request.urlopen(req)

print(res.read().decode('utf-8'))