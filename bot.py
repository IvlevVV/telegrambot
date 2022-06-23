import telebot
TOKEN = ''

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🧡 Мой репозиторий")
	item2 = types.KeyboardButton("😋 Написать мне в личку")
	item3 = types.KeyboardButton("Рабочий день QA")

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Привет! Котик увидел тебя {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🧡 Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/IvlevVV')
		elif message.text == '😋 Написать мне в личку':
			bot.send_message(message.chat.id, 'http://t.me/IVVQA')
		elif message.text == 'Рабочий день QA':
			bot.send_message(message.chat.id, 'https://disk.yandex.ru/i/XbRdYsRBUXCkxw')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)