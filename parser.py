import requests
from bs4 import BeautifulSoup
import json
import os

#인코딩 알아내기
import chardet

## pyhon 파일 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#print(BASE_DIR)

req = requests.get('http://www.naver.com')

html = req.text

#html 소스를 BeautifulSoup을 이용해 파이선 객체로 변환한다.
soup = BeautifulSoup(html, 'html.parser')

#print(soup)

# a 태그 내용만 가져온다
my_titles = soup.select(
    'div > a'
)

data = {}

for title in my_titles :
    data[title.text] = title.get('href')

# dump 할때 한글인 경우 깨지기 때문에 ensure_ascii=False 옵션을 줘야한다.
# 여기서 좀 헤맨게 옵션을 줬는데도 깨져서 뭔가 봤더니 에디터 문제였다. 
# vscode에서 encoding을 utf-8 > euc-kr로 변환했더니 잘 나온다.
with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file :
   json.dump(data, json_file, ensure_ascii=False)
