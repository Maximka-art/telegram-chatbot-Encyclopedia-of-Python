import telebot
from telebot import types
from user_interface import drawing_question
from open import open_file
from feedback import check_words

bot = telebot.TeleBot('ТВОЙ ТОКЕН')


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        drawing_question(message.from_user.id, bot)
    else:
        sent_message = bot.reply_to(message, "Подождите немного⏳, загружаю ответ...")
        otv = check_words(message.text)
        bot.delete_message(message.chat.id, sent_message.message_id)
        if otv:
            bot.send_message(message.chat.id, otv)
        else:
            bot.reply_to(message, "На ваш вопрос в данный момент нету ответа😔. Для получения ответов на"
                                  " популярные вопросы❓ напишите /start")


@bot.callback_query_handler(func=lambda c: c.data == '1')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, open_file("Что такое Python и для чего его используют"))


@bot.callback_query_handler(func=lambda c: c.data == '2')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, open_file("Установка Python на компьютер"))


@bot.callback_query_handler(func=lambda c: c.data == '3')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, open_file("Создание переменной и типы данных в языке"))


@bot.callback_query_handler(func=lambda c: c.data == '4')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, open_file("Операторы условий и циклов"))


@bot.callback_query_handler(func=lambda c: c.data == '5')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, open_file("Функции и как их объявлять"))


@bot.callback_query_handler(func=lambda c: c.data == '6')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, open_file("Работа с файлами"))


@bot.callback_query_handler(func=lambda c: c.data == '7')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, open_file("Импорт модулей"))


@bot.callback_query_handler(func=lambda c: c.data == '8')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, open_file("Основные структуры данных"))


@bot.callback_query_handler(func=lambda c: c.data == '9')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, open_file("Обработка исключений"))


@bot.callback_query_handler(func=lambda c: c.data == '10')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, open_file("Популярные библиотеки и фреймворки"))


bot.polling(none_stop=True, interval=0)
