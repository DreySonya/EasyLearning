import telebot
from telebot import types # для указание типов

bot = telebot.TeleBot('6516287318:AAGy7FRbmO3Tb0CoJpBHdrlBsXIlXISwkoE')


@bot.message_handler(commands=['start'])
def main(message):
      
    markup1 = types.InlineKeyboardMarkup()
    markup1.add(types.InlineKeyboardButton('Продолжить...', callback_data='test'))

    bot.send_message(message.chat.id,f'Приветствуем вас, {message.from_user.first_name},в нашей онлайн школе «Учиться просто». У нас вам будет учиться не только просто, но и интересно. Вы с легкостью усвоите новый материал, а также закрепите старый. Занятия проводятся по русскому, математике, физике, истории, веб-дизайну в програме figma и создание сайтов(HTML/CSS). Вы сможете сами выбрать преподавателя, удобное время и дату. Нам интересны предметы, который мы преподаём, а также создадим интерес у вас.', reply_markup=markup1)


@bot.callback_query_handler(func = lambda callback1: True)
def callback_message(callback):
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Записаться на пробный урок', callback_data='prob'))
    markup.add(types.InlineKeyboardButton('Записаться на урок', callback_data='lesson'))
    
    # markup3 = types.InlineKeyboardMarkup()
    # markup3.add(types.InlineKeyboardButton('Записаться на урок', callback_data='lesson'))
    
    if callback.data == 'test':
       bot.send_message(callback.message.chat.id, f'В школе есть определенные правила: 1. Уважать свое время, а также время преподавателя. Если вы понимаете, что не сможете посетить занятия по какой-либо причине, предупредите об этом заранее. 2.  Не опаздывать на занятие. Время очень ценно.   3. Экологичное общение. Не используем не цензурную брань, не ругаемся, уважительно относимся к преподавателю.', reply_markup=markup)
       
@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data == 'prob':
        bot.send_message(callback.message.chat.id, f'Пробный урок')
    
    
bot.polling(none_stop=True)


   
   
   
   
   
 # markup1 = types.InlineKeyboardMarkup()
 # markup1.add(types.InlineKeyboardButton('Нажми на меня!', callback_data='start'))


# @bot.message_handler(commands=['start'])
# def main(message):


#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('test', callback_data='test'))




#     # bot.send_message(message.chat.id,f'Приветствуем вас, {message.from_user.first_name},в нашей онлайн школе «Учиться просто». У нас вам будет учиться не только просто, но и интересно. Вы с легкостью усвоите новый материал, а также закрепите старый. Занятия проводятся по русскому, математике, физике, истории, веб-дизайну в програме figma и создание сайтов(HTML/CSS). Вы сможете сами выбрать преподавателя, удобное время и дату. Нам интересны предметы, который мы преподаём, а также создадим интерес у вас.', reply_markup=markup)

