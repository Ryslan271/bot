from models.start import bot
from telebot import types


def op(message):

    mar = types.InlineKeyboardMarkup()

    mar.add(types.InlineKeyboardButton('Мой сайт по обущению на языке питон', url='https://t.me/Dog_Python'))
    mar.add(types.InlineKeyboardButton('Яндекс лицей', url='https://yandexlyceum.ru/'))

    bot.send_message(message.chat.id,
                     'Я выпускник Яндекс лицея, где обучался программированию на языке Python и в процессе научился '
                     'делать сайты.\n'
                     'Опыта не много, но многое умею и знаю, ведь закончил лицей с отличием,\n'
                     'прочитал много книг, одна из самых популярных:\n'
                     '<a href="https://yadi.sk/i/lU0JDvB0sX9m8g">Рамальо Лучано - Python. К вершинам мастерства - '
                     '2016</a>\n'
                     "Так же другие по темам:\n"
                     "Java script + Html\n"
                     "Современный Веб-дизайн\n"
                     "Новая большая книга\n"
                     'И множеств других книг по Python и Html',
                     parse_mode='html',
                     reply_markup=mar)


def buy_s(message):

    sti = open('assets/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    mar = types.InlineKeyboardMarkup()

    mar.add(types.InlineKeyboardButton('Мой вк', url='https://vk.com/id131836293'))
    mar.add(types.InlineKeyboardButton('Моя телега', url='https://t.me/Dog_Python'))

    bot.send_message(message.chat.id, '   Я создаю сайты, дорабатываю или изменяю их.\n'
                                      'Я не создаю сайты в конструкторах.\n'
                                      'Работаю на Python + Html и кст этот бот тоже создан на них )\n'
                                      '   Не разбераюсь с доменами , я могу загрузить сайт на ваш домен,\n'
                                      'но не буду покупать и не обещаю , что смогу. Это не входит в стоимость\n'
                                      'если смогу загрузить, то бесплатно\n'
                                      'Цена:\n'
                                      '   Цена сайта зависит от самого сайта, но обычно от 1500 рублей за маленький'
                                      ' и простой сайт.\n'
                                      'Если надумали сделать себе сайт то напишите мне, буду рад помочь ))\n'
                                      '\n'
                                      ' <i><b>/Купить</b></i>\n'
                                      '\n'
                                      'Этой командой вы сможете подать заявку на покупку бота или сайта )',
                     parse_mode='html',
                     reply_markup=mar
                     )


def buy_bot(message):

    sti = open('assets/hi2.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    mar = types.InlineKeyboardMarkup()

    mar.add(types.InlineKeyboardButton('Мой вк', url='https://vk.com/id131836293'))
    mar.add(types.InlineKeyboardButton('Моя телега', url='https://t.me/Dog_Python'))

    bot.send_message(message.chat.id, 'Я могу создать тебе бота\n'
                                      'Допустим этот бот был создан за 3 часа писания кода и 1 день подготовки:\n'
                                      '(прочтение книг, блогов, сайтов и статей)\n'
                                      'Цена:\n'
                                      'О цене кнч договоримся и обсудим что и как )'
                                      '\n'
                                      '\n'
                                      ' <i><b>/Купить</b></i>\n'
                                      '\n'
                                      'Этой командой вы сможете подать заявку на покупку бота или сайта )',
                     parse_mode='html',
                     reply_markup=mar
                     )


def echo_user(message):
    sti = open('assets/hi1.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("Опыт работы")
    item2 = types.KeyboardButton("Купить сайт")
    item3 = types.KeyboardButton("Купить бота")
    item4 = types.KeyboardButton("/Telegram")
    item5 = types.KeyboardButton("/vk")
    item6 = types.KeyboardButton("/help")

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id,
                     'Спасибо, что написали мне :D\n'
                     'Ваше сообщение успешно доставлено и ответ придет в ближайшее время',
                     reply_markup=markup)


def echo_buy_s(message):
    sti = open('assets/3.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("Опыт работы")
    item2 = types.KeyboardButton("Купить сайт")
    item3 = types.KeyboardButton("Купить бота")
    item4 = types.KeyboardButton("/Telegram")
    item5 = types.KeyboardButton("/vk")
    item6 = types.KeyboardButton("/help")

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id,
                     'Спасибо, что написали мне :D\n'
                     'Ваш заказ на покупку сайта скоро будет доставлен и ответ придет в ближайшее время',
                     reply_markup=markup)


def echo_buy_bot(message):
    sti = open('assets/hi2.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("Опыт работы")
    item2 = types.KeyboardButton("Купить сайт")
    item3 = types.KeyboardButton("Купить бота")
    item4 = types.KeyboardButton("/Telegram")
    item5 = types.KeyboardButton("/vk")
    item6 = types.KeyboardButton("/help")

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id,
                     'Спасибо, что написали мне :D\n'
                     'Ваш заказ на покупку бота скоро будет доставлен и ответ придет в ближайшее время',
                     reply_markup=markup)


def error(message):
    mar = types.InlineKeyboardMarkup()

    mar.add(types.InlineKeyboardButton('Мой вк', url='https://vk.com/id131836293'))
    mar.add(types.InlineKeyboardButton('Моя телега', url='https://t.me/Dog_Python'))

    bot.send_message(message.chat.id,
                     'Вы мне отправляете пустую строку )\n'
                     'Вы не знаете, что значит команда /связь?\n'
                     'Команда:\n'
                     '\n'
                     '<i><b>/связь "ваш текст" </b></i>\n'
                     '\n'
                     'Эта команда отправляет мне ваше сообщение и вы можете мне написать какой-либо вопрос '
                     'или же отправить то что хотите купить :D\n'
                     '\n'
                     'Связаться:',
                     parse_mode='html',
                     reply_markup=mar
                     )


def back(message):

    sti = open('assets/4.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("Опыт работы")
    item2 = types.KeyboardButton("Купить сайт")
    item3 = types.KeyboardButton("Купить бота")
    item4 = types.KeyboardButton("/Telegram")
    item5 = types.KeyboardButton("/vk")
    item6 = types.KeyboardButton("/help")

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id,
                     "Ну что же, выбери, что будем делать дальше?", reply_markup=markup)
