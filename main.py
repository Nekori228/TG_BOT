import telebot
import datetime
import requests
from telebot import types

now = datetime.datetime.now()


bot = telebot.TeleBot('6133502208:AAHSCu3lLvNoRq83npanikAyn3L4svaJ5_s')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Nice photo')

@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    vk = types.KeyboardButton('vk')
    start = types.KeyboardButton('/start')
    markup.add(vk, start)
    bot.send_message(message.chat.id, 'Перейти на сайт', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    btn2 = types.KeyboardButton("Полезные функции")
    markup.add(btn1, btn2)
    mess = f"Привет, {message.from_user.first_name}. Я бот, принадлежащий моему владельцу Nekori (vk.com/power228f)"
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Поздороваться"):
        bot.send_message(message.chat.id, 'Привет, рад что ты здесь')
    elif (message.text == "Полезные функции"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Временя")
        btn2 = types.KeyboardButton("Погода (в разработке)")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Возможности", reply_markup=markup)

    elif (message.text == "Време"):
        bot.send_message(message.chat.id, now.strftime("%d-%m-%Y %H:%M"))

    elif message.text == "Расписание (в разработке)":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Поздороваться")
        button2 = types.KeyboardButton("Полезные функции")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

@bot.message_handler(content_types=['weather'])
def weather(message):
    bot.send_message(message.chat.id, 'Nice photo')

city = input('input the city name')
print(city)

print('Displaying Weather report for: ' + city)

url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

print(res.text)

# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
#     bot.send_message(message.chat.id, mess, parse_mode='html')

# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == "Hello":
#         bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
#     elif message.text == "photo":
#         photo = open('image.PNG', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "Неизвестный запрос", parse_mode='html')

# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Посетить", url="https://vk.com/power228f"))
#     bot.send_message(message.chat.id, 'Перейти на сайт', reply_markup=markup)

bot.polling(none_stop=True)