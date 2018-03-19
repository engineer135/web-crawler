import requests

req = requests.get('http://www.naver.com')

html = req.text
header = req.headers
status = req.status_code
is_ok = req.ok

print(html)
print('------------------------')
print(header)
print('------------------------')
print(status)
print('------------------------')
print(is_ok)
