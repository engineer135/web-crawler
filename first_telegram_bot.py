import telegram

# 텔레그램에서 받은 토큰 넣어주면 된다.
my_token = ''
bot = telegram.Bot(token = my_token)

# 메세지 확인
updates = bot.getUpdates()
for u in updates :
    print(u.message)

# 이때 중요한건 텔레그램에서 봇을 찾아 먼저 말을 걸고 실행해야 update 내역들을 가져옵니다.
# 그리고 저 getUpdates 할때 getUpdaet로 확인하지 않은 새로운 메세지가 있을때만 에러가 안나는 것 같다.

# 메세지 보내기
chat_id = bot.getUpdates()[-1].message.chat.id
bot.sendMessage(chat_id=chat_id, text="저는 봇입니다! 안녕!")