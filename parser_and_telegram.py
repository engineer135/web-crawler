# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import json
import os
import telegram

# 게시판 글 제목중 첫번째 제목을 가져와서 txt 파일에 저장해두자.
# 그리고 저장된 제목과 다른 경우 새글이 올라왔어요! 라는 메세지를 텔레그램으로 보낸다.

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://www.clien.net/service/group/allsell')
req.encoding= 'utf-8'

html = req.text
soup = bs(html, 'html.parser')
# 장터의 제목만 가져옵니다. 첫번째 span은 <span>장터</span> 공통 텍스트라서 빼고 두번째 span인 실제 제목만 가져옵니다.
posts = soup.select('div#div_content > div.list_item > div.list_title > a.list_subject > span:nth-of-type(2) ')
#for post in posts:
#    print(post.text)
latest = posts[0].text
print('latest post %s' % latest)
# latest 와 저장된 latest 비교해서 다르면 메세지 보내고 아니면 안 보낸다.
with open(os.path.join(BASE_DIR, 'latest'), 'r+') as f_read:
    line = f_read.readline()
    print('line %s' % line)
    if line == latest :
        print('same... not send')
    else :
        print('different... send!')

        # 텔레그램 보내기
        resources = {}
        with open('private_info.txt', 'r') as f :
            lines = f.readlines()
            for line in lines :
                (key, val) = line.split()
                resources[key] = val
        #print(resources)

        my_token = resources['my_token']
        bot = telegram.Bot(token = my_token)

        id_channel = resources['id_channel']
        bot.sendMessage(chat_id=id_channel, text=latest)
    
    #f_read.close()


with open(os.path.join(BASE_DIR, 'latest'), 'w+') as f_write:
    f_write.write(latest)
    #f_write.close()

# 일단 텔레그램으로 보내는것만 했습니다. 스케쥴러 돌리는 거는 vultr 가입후 서버에서 해보겠습니다.
