from telegram.ext import Updater, MessageHandler, Filters

print('telegram test start...')

# 보안을 위해 토큰을 파일로 따로 관리하고 형상관리에서 제외시킨다.
resources = {}
with open('private_info.txt', 'r') as f :
    lines = f.readlines()
    for line in lines :
        (key, val) = line.split()
        resources[key] = val

# message 응답 
def get_message(bot, update):
    #update.message.reply_text('I got you')
    update.message.reply_text(update.message.text)

# Updater는 봇 업데이트 사항이 있으면 이를 가져오는 클래스
updater = Updater(resources['my_token'])

# 메세지 다루는 클래스
message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

# polling 시작
updater.start_polling(timeout=2, clean=True)
updater.idle()