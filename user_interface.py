from telebot import types


def drawing_question(message, bot):
    keyboard = types.InlineKeyboardMarkup()
    # 1. Что такое Python и для чего его используют?
    key = types.InlineKeyboardButton(text="1. Что такое Python и для чего его используют", callback_data="1")
    keyboard.add(key)  # добавляем кнопку в клавиатуру
    # 2. Как установить Python на компьютер?
    key = types.InlineKeyboardButton(text="2. Установка Python на компьютер", callback_data="2")
    keyboard.add(key)
    # 3. Как создать переменную в Python и какие типы данных поддерживает язык?
    key = types.InlineKeyboardButton(text="3. Создание переменной и типы данных в языке", callback_data="3")
    keyboard.add(key)
    # 4. Какие операторы условий и циклов есть в Python?
    key = types.InlineKeyboardButton(text="4. Операторы условий и циклов", callback_data="4")
    keyboard.add(key)
    # 5. Что такое функции в Python и как их объявлять?
    key = types.InlineKeyboardButton(text="5. Функции и как их объявлять", callback_data="5")
    keyboard.add(key)
    # 6. Как работать с файлами в Python?
    key = types.InlineKeyboardButton(text="6. Работа с файлами", callback_data="6")
    keyboard.add(key)
    # 7. Как импортировать модули в Python?
    key = types.InlineKeyboardButton(text="7. Импорт модулей", callback_data="7")
    keyboard.add(key)
    # 8. Какие основные структуры данных поддерживает Python?
    key = types.InlineKeyboardButton(text="8. Основные структуры данных", callback_data="8")
    keyboard.add(key)
    # 9. Как обрабатывать исключения в Python?
    key = types.InlineKeyboardButton(text="9. Обработка исключений", callback_data="9")
    keyboard.add(key)
    # 10. Какие библиотеки и фреймворки широко используются в разработке на Python?
    key = types.InlineKeyboardButton(text="10. Популярные библиотеки и фреймворки", callback_data="10")
    keyboard.add(key)

    question = "Выберите ответ📕 на популярные вопросы❓ или задайте его сами😎"
    bot.send_message(message, text=question, reply_markup=keyboard)
