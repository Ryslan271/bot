from models.start import bot
from telebot import types
from models.support import op, buy_s, buy_bot, echo_user, echo_buy_s, echo_buy_bot, error, back


@bot.message_handler(commands=['start'])
def welcome(message):
    # стартовая функция
    sti = open('assets/hi.tgs', 'rb')
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
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный для "
                     "для рекламы моего <a  href='https://t.me/Dog_Python'>создателя</a>".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['vk'])
def vk(message):
    sti = open('assets/1.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    mar = types.InlineKeyboardMarkup()
    mar.add(types.InlineKeyboardButton('Мой вк', url='https://vk.com/id131836293'))
    bot.send_message(message.chat.id,
                     'Вот мой вк для связи со мной',
                     parse_mode='html',
                     reply_markup=mar)


@bot.message_handler(commands=['Telegram'])
def telegram(message):
    sti = open('assets/2.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    mar = types.InlineKeyboardMarkup()
    mar.add(types.InlineKeyboardButton('Моя телега', url='https://t.me/Dog_Python'))

    bot.send_message(message.chat.id,
                     'Вот моя телега для связи со мной',
                     parse_mode='html',
                     reply_markup=mar)


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("Опыт работы")
    item2 = types.KeyboardButton("Купить сайт")
    item3 = types.KeyboardButton("Купить бота")
    item4 = types.KeyboardButton("/Telegram")
    item5 = types.KeyboardButton("/vk")
    item6 = types.KeyboardButton("/help")

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id,
                     '<b>Команды:</b>\n'
                     '\n'
                     '<b>/Telegram</b> - <i>Выводит ссылку на мой телеграм</i>\n'
                     '\n'
                     '<b>/vk</b> - <i>Выводит ссылку на мой вк</i>\n'
                     '\n'
                     '<b>/связь</b> - <i>Связь со мной</i>\n'
                     '\n'
                     '<b>/Купить</b> - <i>Покупка бота или же сайта</i>\n'
                     '\n'
                     '<b>Текстовые команды:</b>\n'
                     '\n'
                     '<b>Опыт работы</b> - <i>Выводит мой опыт работы и то, что я изучал</i>\n'
                     '\n'
                     '<b>Купить сайт</b> - <i>Описывает некоторые нюансы в покупке сайта</i>\n'
                     '\n'
                     '<b>Купить бота</b> - <i>Описывает некоторые нюансы в покупке бота</i>\n'
                     '\n'
                     'Если у вас есть вопросы то напишите команду <b>/связь</b> и после текст, например вот так: \n'
                     '\n'
                     '<i><b>/связь Привет у меня не работает кнопка Купить, что делать?</b></i> )\n'
                     '\n'
                     '\n'
                     'и я обязательно отвечу вам',
                     parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(func=lambda message: True, commands=['связь'])
def echo(message):
    chat_id = 943101770

    message.text = message.text.replace('/связь', '')

    if message.text:
        if message.from_user.username:
            msg = ['name: ' + message.from_user.first_name,
                   'id: ' + str(message.from_user.id),
                   'url: ' + message.from_user.username,
                   'text: ' + '\n' + message.text]
        else:
            msg = ['name: ' + message.from_user.first_name,
                   'id: ' + str(message.from_user.id),
                   'url: ' + 'None',
                   'text: ' + '\n' + message.text]
        msg_1 = ''

        for i in msg:
            msg_1 += i + '\n'

        bot.send_message(chat_id=chat_id, text=msg_1)

        echo_user(message)

    else:
        error(message)


@bot.message_handler(commands=['Купить'])
def buy_s_bot(message):

    sti = open('assets/5.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("/Купить_сайт")
    item2 = types.KeyboardButton("/Купить_бота")
    item3 = types.KeyboardButton("/Назад")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Выбери то что хочешь у меня заказать.\n'
                                      '\n'
                                      '<b>/Купить_сайт</b> - <i>это значит, что ты подаешь заявку на покупку сайта'
                                      ' и вскоре я вам напишу и мы все обсудим</i> )\n'
                                      '\n'
                                      '<b>/Купить_бота</b> - <i>это значит, что ты подаешь заявку на покупку бота'
                                      ' и вскоре я вам напишу и мы все обсудим</i> )',
                     parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(func=lambda message: True, commands=['Купить_сайт'])
def echo_s(message):
    chat_id = 943101770

    message.text = message.text.replace('/Купить сайт', '')

    if message.text:
        if message.from_user.username:
            msg = ['name: ' + message.from_user.first_name,
                   'id: ' + str(message.from_user.id),
                   'url: ' + message.from_user.username,
                   'text: ' + '\n' + message.text]
        else:
            msg = ['name: ' + message.from_user.first_name,
                   'id: ' + str(message.from_user.id),
                   'url: ' + 'None',
                   'text: Покупка сайта']
        msg_1 = ''

        for i in msg:
            msg_1 += i + '\n'

        bot.send_message(chat_id=chat_id, text=msg_1)

        echo_buy_s(message)

    else:
        error(message)


@bot.message_handler(func=lambda message: True, commands=['Купить_бота'])
def echo_bot(message):
    chat_id = 943101770

    message.text = message.text.replace('/Купить бота', '')

    if message.text:
        if message.from_user.username:
            msg = ['name: ' + message.from_user.first_name,
                   'id: ' + str(message.from_user.id),
                   'url: ' + message.from_user.username,
                   'text: ' + '\n' + message.text]
        else:
            msg = ['name: ' + message.from_user.first_name,
                   'id: ' + str(message.from_user.id),
                   'url: ' + 'None',
                   'text: Покупка бота']
        msg_1 = ''

        for i in msg:
            msg_1 += i + '\n'

        bot.send_message(chat_id=chat_id, text=msg_1)

        echo_buy_bot(message)

    else:
        error(message)


@bot.message_handler(commands=['Назад'])
def echo_bot(message):
    back(message)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == 'private':

        if message.text == 'Опыт работы':
            op(message)

        elif message.text == 'Купить сайт':
            buy_s(message)

        elif message.text == 'Купить бота':
            buy_bot(message)

        else:
            msg = message.text
            bot.send_message(message.chat.id, 'Я не знаю что ответить вам на \"' + str(msg) + "\", /help")


bot.polling(none_stop=True)
