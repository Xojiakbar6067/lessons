import telebot
import buttons as bt

#регистрация бота
bot=telebot.TeleBot('6420185233:AAHPwX7kkN5fqLUJwVc6ys3fD4v_9JZcras')

#пропишем алгоритм
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, "приветывую в нашем боте", reply_markup=bt.choice_buttons())

@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text.lower()=='википедия':
        bot.send_message(message.from_user.id, 'Введите слово')
        bot.register_next_step_handler(message, wiki)
    elif message.text.title()=='Переводчик':
        bot.send_message(message.from_user.id, 'Введите слова для перевода(пишите на английском)')
        bot.register_next_step_handler(message, translate)
    elif message.text=='Курс валюты':
        bot.send_message(message.from_user.id, 'курс доллара \nкурс йевро \nкурс рубля', reply_markup=bt.button1())
        bot.register_next_step_handler(message, tranzak)
    else:
        bot.send_message(message.from_user.id, 'я вас не понял')
def wiki(message):
    if message.text=='кастро':
        bot.send_message(message.from_user.id,
                         'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%81%D1%82%D1%80%D0%BE,_%D0%A4%D0%B8%D0%B4%D0%B5%D0%BB%D1%8C')
    else:
        bot.send_message(message.from_user.id, 'увы я не знаю о ком вы((')

def translate(message):
    if message.text=='hello':
        bot.send_message(message.from_user.id, 'привет')
    else:
        bot.send_message(message.from_user.id, "i don't understand you((")
def tranzak(message):
    if message.text=='USD':
        bot.send_message(message.from_user.id, 'сегодняшный курс доллара 11 613.06', reply_markup=bt.choice_buttons())
        bot.register_next_step_handler(message, text_message)
    elif message.text=='EUR':
        bot.send_message(message.from_user.id, 'сегодняшный курс евро 12 824.30', reply_markup=bt.choice_buttons())
        bot.register_next_step_handler(message, text_message)
    elif message.text=='RUB':
        bot.send_message(message.from_user.id, 'сугодняшный курс рубля 129.01', reply_markup=bt.choice_buttons())
        bot.register_next_step_handler(message, text_message)
    else:
        pass
#запуск бота
bot.polling(none_stop=True)