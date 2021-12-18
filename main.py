import telebot
import random
from telebot import types

import content
from content import predictions

bot = telebot.TeleBot('5002158195:AAF7fVkvQ6pXWCihoxeDjWv0HVUeje1fX5k')
# @bot.message_handler(content_types=['text', 'document'])
# def inline(message):
#     bot.send_message(message.chat.id, text='ID ' + str(message.id) + " " + message.from_user.username)
#     bot.send_message(-1001706043041, text='Сообщение от @' + message.from_user.username)
#     bot.forward_message(-1001706043041, message.chat.id, message.id)

@bot.message_handler(content_types='text', commands=['start'])
def start(message):
    begin_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    begin_btn1 = types.KeyboardButton(text='Кто мы?')
    begin_btn2 = types.KeyboardButton(text='Наши ценности')
    begin_btn3 = types.KeyboardButton(text='Открытые вакансии')
    begin_btn4 = types.KeyboardButton(text='Задать вопрос')
    begin_btn5 = types.KeyboardButton(text='Предсказание на день')
    begin_kb.add(begin_btn1)
    begin_kb.add(begin_btn2, begin_btn3)
    begin_kb.add(begin_btn4, begin_btn5)
    bot.send_message(message.chat.id, content.welcome, reply_markup=begin_kb)




# Получение сообщений от юзера
@bot.message_handler(content_types=["text","document"])
def handle_text(message):
    if message.text == 'Кто мы?':
        bot.send_message(message.chat.id, content.we, message.id, parse_mode="html")

    elif message.text == 'Наши ценности':
        bot.send_message(message.chat.id, content.values, message.id, parse_mode="html")

    elif message.text == 'Открытые вакансии':
        bot.send_message(message.chat.id, text='Наши вакансии:', reply_markup=kb)

    elif message.text == 'Задать вопрос':
        bot.send_message(message.chat.id, content.ask, message.id, parse_mode="html")
    elif message.text == 'Предсказание на день':
        bot.send_message(message.chat.id, predictions[random.randrange(len(predictions))], message.id)
    elif message.document:

        bot.reply_to(message, "Оу, кажется это резюме, наш специалист по резюме проверит его и свяжется с тобой)")
        bot.forward_message(-1001706043041, message.chat.id, message.id)
        bot.send_message(-1001706043041, text='Бусинка пора чуть чуть поработать, я знаю что ты и так устаешь ппц, но там резюме от @' + message.from_user.username, )
    else:
        # bot.send_message(message.chat.id, text='ID ' + str(message.id) + " " + message.from_user.username)
        # bot.send_message(-1001706043041, text='Сообщение от @' + message.from_user.username, )
        bot.forward_message(-1001706043041, message.chat.id, message.id)
        bot.reply_to(message, "Наш специалист уже получил твое сообщение и сейчас думает, что ответить))")


# обработка кнопок вакансий
@bot.callback_query_handler(func=lambda a: True)
def begin_a(a):
    if a.data == 'vac1':
        bot.edit_message_text(chat_id=a.message.chat.id, message_id=a.message.message_id, text=content.vac1,
                              reply_markup=kb, parse_mode="html")
    elif a.data == 'vac2':
        bot.edit_message_text(chat_id=a.message.chat.id, message_id=a.message.message_id, text=content.vac2,
                              reply_markup=kb, parse_mode="html")
    elif a.data == 'vac3':
        bot.edit_message_text(chat_id=a.message.chat.id, message_id=a.message.message_id, text=content.vac3,
                              reply_markup=kb, parse_mode="html")
    elif a.data == 'vac4':
        bot.edit_message_text(chat_id=a.message.chat.id, message_id=a.message.message_id, text=content.vac4,
                              reply_markup=kb, parse_mode="html")
    elif a.data == 'vac5':
        bot.edit_message_text(chat_id=a.message.chat.id, message_id=a.message.message_id, text=content.vac5,
                              reply_markup=kb, parse_mode="html")
    elif a.data == 'vac6':
        bot.edit_message_text(chat_id=a.message.chat.id, message_id=a.message.message_id, text=content.vac6,
                              reply_markup=kb, parse_mode="html")


kb = types.InlineKeyboardMarkup()
vac1 = types.InlineKeyboardButton(text='Middle Java-developer ', callback_data='vac1')
vac2 = types.InlineKeyboardButton(text='Machine Learning Java Engineer', callback_data='vac2')
vac3 = types.InlineKeyboardButton(text='CTO Blockchain/Solidity', callback_data='vac3')
vac4 = types.InlineKeyboardButton(text='Оператор технической поддержки', callback_data='vac4')
vac5 = types.InlineKeyboardButton(text='Менеджер по продажам со знанием английского языка', callback_data='vac5')
vac6 = types.InlineKeyboardButton(text='Менеджер по продажам со знанием китайского языка', callback_data='vac6')
kb.add(vac1, vac2)
kb.add(vac3, vac4)
kb.add(vac5, vac6)

bot.polling(none_stop=True, interval=0)