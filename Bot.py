import telebot
from telebot import types  # телебот для создания меню
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telebot.types import Message
from Config import token  # импортируем значение token из файла config.py
# from BD import show_for_genre
from work import make_request_by_genre_comedy, make_request_by_genre_fantastic, make_request_by_genre_action, \
    make_request_by_genre_melodramas

bot = telebot.TeleBot(token)  # создаем переменную bot и передаем ему токен


@bot.message_handler(commands=['start'])  # /обработчик на команду start
# главное меню
def start(msg: Message):  # функция принимающая message

    markup_menu = ReplyKeyboardMarkup(resize_keyboard=True)  # (, one_time_keyboard=True)

    item1 = KeyboardButton('Выбрать жанр фильма')  # кнопка отправит сообщение боту
    item2 = KeyboardButton("Фильмы из нашей фильмотеки")
    item3 = KeyboardButton('О нас')
    markup_menu.add(item1, item2, item3)
    bot.send_message(msg.chat.id,
                     text="Привет, {0.first_name}! Я чат-бот по поиску фильмов. Воспользуйся меню для выбора действия".format(
                         msg.from_user), reply_markup=markup_menu)


@bot.message_handler(content_types=['text'])
def bot_message(msg: Message):
    if msg.chat.type == 'private':  # проверка того, что сообщение является личным, а не от телеграмма
        if msg.text == 'Выбрать жанр фильма':
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("Комедия", callback_data="comedy"))
            markup.add(InlineKeyboardButton("Боевик", callback_data="action"))
            markup.add(InlineKeyboardButton("Фантастика", callback_data="fantastic"))
            markup.add(InlineKeyboardButton("Мелодрамы ", callback_data="melodramas"))
            # markup.add(InlineKeyboardButton("Назад ", callback_data="back"))

            bot.send_message(msg.chat.id, 'Выберите жанр фильма:', reply_markup=markup)

        if msg.text == 'Фильмы из нашей фильмотеки': #позже добавим базу
            bot.send_message(msg.chat.id,
                             text="Вы находитесь в разделе 'Фильмы из нашей фильмотеки'")
            bot.send_photo(msg.chat.id, photo=open('static/img/straniza-v-razrabotke.jpg', 'rb'))

            # markup = InlineKeyboardMarkup()
            # markup.add(InlineKeyboardButton("Комедия", callback_data="comedy"))
            # markup.add(InlineKeyboardButton("Боевик", callback_data="action"))
            # markup.add(InlineKeyboardButton("Фантастика", callback_data="fantastic"))
            # markup.add(InlineKeyboardButton("Мелодрамы ", callback_data="melodramas"))
            # markup.add(InlineKeyboardButton("Назад ", callback_data="back"))
            # bot.send_message(msg.chat.id, 'Выберите жанр фильма:', reply_markup=markup)
        if msg.text == 'О нас':
            # markup = InlineKeyboardMarkup()
            # markup.add(InlineKeyboardButton("Назад ", callback_data="back"))
            bot.send_message(msg.chat.id,
                             text="Данный чат-бот по поиску фильмов был разработан в качестве курсовой работы. Мы обязательно продолжим работу по его совершенствованию")
            bot.send_photo(msg.chat.id, photo=open('static/img/over.png','rb'))

@bot.callback_query_handler(func=lambda call: call.data == "comedy")
def comedy(call: types.CallbackQuery):
    bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали комедии")
    # выдает список фильмов по жанру
    bot.send_message(chat_id=call.message.chat.id, text="Список фильмов:")
    movies_comedy = make_request_by_genre_comedy('комедия')
    for movie in movies_comedy:
        bot.send_message(chat_id=call.message.chat.id, text=movie)


@bot.callback_query_handler(func=lambda call: call.data == "action")
def action(call: types.CallbackQuery):
    bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали боевик")
    # выдает список фильмов по жанру
    bot.send_message(chat_id=call.message.chat.id, text="Список фильмов:")
    movies_action = make_request_by_genre_action('боевик')
    for movie in movies_action:
        bot.send_message(chat_id=call.message.chat.id, text=movie)


@bot.callback_query_handler(func=lambda call: call.data == "fantastic")
def fantastic(call: types.CallbackQuery):
    bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали фантастику")
    # выдает список фильмов по жанру
    bot.send_message(chat_id=call.message.chat.id, text='Список фильмов: ')
    movies_fantastic = make_request_by_genre_fantastic('фантастика')
    for movie in movies_fantastic:
        bot.send_message(chat_id=call.message.chat.id, text=movie)


@bot.callback_query_handler(func=lambda call: call.data == "melodramas")
def melodramas(call: types.CallbackQuery):
    bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали мелодрамы")
    # выдает список фильмов по жанру
    bot.send_message(chat_id=call.message.chat.id, text='Список фильмов: ')
    movies_melodramas = make_request_by_genre_melodramas('мелодрама')
    for movie in movies_melodramas:
        bot.send_message(chat_id=call.message.chat.id, text=movie)


# if __name__ == '__main__':
# # bot.infinity_polling(skip_pending=True)
bot.polling(none_stop=True, interval=0)
