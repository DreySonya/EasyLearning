import telebot

bot = telebot.TeleBot('6516287318:AAGy7FRbmO3Tb0CoJpBHdrlBsXIlXISwkoE')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Приветствуем вас '{message.from_user.first_name} {message.from_user.last_name}',в нашей онлайн школе «Учиться просто». У нас вам будет учиться не только просто, но и интересно. Вы с легкостью усвоите новый материал, а также закрепите старый. Занятия проводятся по русскому, математике, физике, истории, веб-дизайну в програме figma и создание сайтов(HTML/CSS). Вы сможете сами выбрать преподавателя, удобное время и дату. Нам интересны предметы, который мы преподаём, а также создадим интерес у вас.')

    
bot.polling(none_stop=True)

