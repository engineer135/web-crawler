# Selenium을 활용해 무적 크롤러를 만들어봅니다.
# 브라우저를 제어할 수 있어서, javascript를 이용해 비동기적으로, 혹은 늦게 불러와지는 컨텐츠들을 가져올 수 있음.

# 1. 설치
# pip install selenium

# 2. webdriver(or PhantomJS webdriver) 설치
# 크롬 웹드라이버가 필요하다. 다운받아서 Selenium 객체 생성할때 넘겨준다.
# PhantomJS webdriver 로도 가능한데 여기서는 그냥 크롬 웹드라이버로 진행한다.
# 만약에 'Can not connect to the ChromeDriver' 에러가 발생한다면
# hosts 파일에 127.0.0.1       localhost를 추가해주자

from selenium import webdriver
from bs4 import BeautifulSoup

# 이렇게 하면 크롬 브라우저가 실행됩니다.
driver = webdriver.Chrome('./chromeDriver/chromedriver')
# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려준다.
driver.implicitly_wait(3)

# url 접근
driver.get('https://nid.naver.com/nidlogin.login')

# 네이버는 클리앙과 다르게 js 처리를 통해 로그인을 해서 기존방식으로 로그인하기가 어렵다.
# 하지만 Selenium으로 간단하게 처리가능하다.
## 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('id').send_keys('')
driver.find_element_by_name('pw').send_keys('')
## 로그인 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

driver.get('https://order.pay.naver.com/home') ## Naver 페이 들어가기
html = driver.page_source ## 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') ## BeautifulSoup사용하기
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip())

# 성공!! ㅋㅋ
# result
# DevTools listening on ws://127.0.0.1:12794/devtools/browser/ec698359-6d1d-401a-a213-c72488aa7924
# 한샘 샘키즈 스칸디 에디션 수납장 870 (2종/택1)
# 리락쿠마 가방 2단 스텐도시락(얼굴)/유아동 소풍 도시락통
# 트라몬티나 우드핸들 커트러리 테이블포크 195mm
# HP 63 잉크 F6U62AA F6U61AA F6U63AA F6U64AA 63XL Deskjet 2132 2130 2131 1110 1112