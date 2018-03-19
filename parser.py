import requests
from bs4 import BeautifulSoup

req = requests.get('http://www.naver.com')

html = req.text

#html 소스를 BeautifulSoup을 이용해 파이선 객체로 변환한다.
soup = BeautifulSoup(html, 'html.parser')

#print(soup)

# a 태그 내용만 가져온다
my_titles = soup.select(
    'div > a'
)

# 이렇게 soup 객체로 담겨오기때문에, 원하는대로 사용이 가능함.
for title in my_titles :
    print(title.text)
    print(title.get('href'))

#result
# (myvenv) D:\web-crawler>python parser.py
# 뉴스스탠드 바로가기
# #news_cast
# 주제별캐스트 바로가기
# #themecast
# 타임스퀘어 바로가기
# #time_square
# 쇼핑캐스트 바로가기
# #shop_cast
# 로그인 바로가기
# #account
# 네이버를 시작페이지로
# http://help.naver.com/support/alias/contents2/naverhome/naverhome_1.naver
# 쥬니어네이버
# http://jr.naver.com
# 해피빈
# http://happybean.naver.com/main/SectionMain.nhn
# 한글 입력기
# javascript:;
# 자동완성 펼치기
# javascript:;
# 로그인
# https://nid.naver.com/nidlogin.login
# (이하생략) 

# header = req.headers
# status = req.status_code
# is_ok = req.ok

# print(html)
# print('------------------------')
# print(header)
# print('------------------------')
# print(status)
# print('------------------------')
# print(is_ok)
