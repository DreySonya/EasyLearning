import telebot
from telebot import types # для указание типов

bot = telebot.TeleBot('6516287318:AAGy7FRbmO3Tb0CoJpBHdrlBsXIlXISwkoE')

@bot.message_handler()
def info(message):
    
    if message.text.lower() == 'Привет':
        bot.send_message(message.chat.id, 'Привет, рад вас видеть, для того чтобы взаимодействовать со мной или записаться на урок, то вам нужно использовать кнопочки, которые указаны ниже под строкой ввода сообщение или если вы уже взаимодействовали со мной вам, то у вас есть кнопочки под текстом коорый я вам писал')


@bot.message_handler(commands=['start'])
def main(message):


    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('test', callback_data='test'))


    bot.send_message(message.chat.id,f'Приветствуем вас, {message.from_user.first_name},в нашей онлайн школе «Учиться просто». У нас вам будет учиться не только просто, но и интересно. Вы с легкостью усвоите новый материал, а также закрепите старый. Занятия проводятся по русскому, математике, физике, истории, веб-дизайну в програме figma и создание сайтов(HTML/CSS). Вы сможете сами выбрать преподавателя, удобное время и дату. Нам интересны предметы, который мы преподаём, а также создадим интерес у вас.', reply_markup=markup)



@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data == 'test':
       bot.send_message(callback.message.chat.id, f'Succses' )

bot.polling(none_stop=True)

