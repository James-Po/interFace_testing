import requests
import postInfo

session = requests.Session()
resp = requests.post(url = postInfo.url, headers = postInfo.headers, json = postInfo.json)

my_cookie = resp.cookies

print(resp.text)
print(resp.json())
print(my_cookie)
