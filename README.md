파이썬으로 웹 크롤러를 만들어보기로 했습니다.
묙표는 오늘 하루 안에 끝내기!
https://beomi.github.io/gb-crawling/
여기 가이드를 보고 진행했어요~

순서는 대강 이런식으로 진행하면 될것 같다.

0. 깃 설정
git init
.gitignore 파일 생성
git remote add origin <gitHubUrl>

1. 가상환경 만들기(이걸 꼭 만들어야하는지는 모르겠지만 일단 만들고 진행해본다)
python -m venv myvenv
혹시 윈도우 환경에서 보안 오류 이런게 뜬다면 powershell 관리자 권한으로 열고 Set-ExecutionPolicy Unrestricted -Force 실행하면 된다.

2. requests와 BeautifulSoup 설치
pip install requests
pip install beautifulsoup4

3. 파싱

4. 심화학습 ㅋ
