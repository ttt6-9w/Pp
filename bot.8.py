import telebot
from telebot import types

bot = telebot.TeleBot("7935120323:AAEwMhLkCgBTYkcrjUdlAIfK1ipSM23PzKo")

@bot.message_handler(content_types=['text'])
def handle_text_messages(message):

    if message.text == "/help":

        bot.send_message(
            message.chat.id,
            "Напиши Привіт"
        )

    elif message.text == "Привіт":

        bot.send_message(
            message.chat.id,
            "Привіт! Ти потрапив у космічний квест."
        )


        keyboard = types.InlineKeyboardMarkup(row_width=2)

        btn1 = types.InlineKeyboardButton(
            text="✅ Так",
            callback_data="yes"
        )

        btn2 = types.InlineKeyboardButton(
            text="❌ Ні",
            callback_data="no"
        )

        keyboard.add(btn1, btn2)

        bot.send_message(
            message.chat.id,
            "Хочеш пройти квест?",
            reply_markup=keyboard
        )

    else:

        bot.send_message(
            message.chat.id,
            "Я тебе не розумію. Напиши /help"
        )

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "yes":

        keyboard = types.InlineKeyboardMarkup(row_width=2)

        btn1 = types.InlineKeyboardButton(
            text="🔦 Взяти ліхтар",
            callback_data="flashlight"
        )

        btn2 = types.InlineKeyboardButton(
            text="🚪 Відкрити двері",
            callback_data="door"
        )

        keyboard.add(btn1, btn2)

        bot.send_message(
            call.message.chat.id,
            "Ти прокинувся на космічному кораблі. Що будеш робити?",
            reply_markup=keyboard
        )

    elif call.data == "no":

        keyboard = types.InlineKeyboardMarkup(row_width=1)

        btn1 = types.InlineKeyboardButton(
            text="🔄 Спробувати ще раз",
            callback_data="restart"
        )

        keyboard.add(btn1)

        bot.send_message(
            call.message.chat.id,
            "Добре 😄 Можеш повернутися пізніше.",
            reply_markup=keyboard
        )

    elif call.data == "flashlight":

        keyboard = types.InlineKeyboardMarkup(row_width=2)

        btn1 = types.InlineKeyboardButton(
            text="👽 Перевірити шум",
            callback_data="alien"
        )

        btn2 = types.InlineKeyboardButton(
            text="🖥 Піти до комп'ютера",
            callback_data="computer"
        )

        keyboard.add(btn1, btn2)

        bot.send_message(
            call.message.chat.id,
            "Ти взяв ліхтар і почув дивний шум.",
            reply_markup=keyboard
        )

    elif call.data == "door":

        keyboard = types.InlineKeyboardMarkup(row_width=1)

        btn1 = types.InlineKeyboardButton(
            text="🔄 Почати знову",
            callback_data="restart"
        )

        keyboard.add(btn1)

        bot.send_message(
            call.message.chat.id,
            "❌ За дверима був монстр. Ти програв.",
            reply_markup=keyboard
        )

    elif call.data == "alien":

        keyboard = types.InlineKeyboardMarkup(row_width=1)

        btn1 = types.InlineKeyboardButton(
            text="🔄 Почати знову",
            callback_data="restart"
        )

        keyboard.add(btn1)

        bot.send_message(
            call.message.chat.id,
            "👽 Прибулець допоміг тобі втекти. Перемога!",
            reply_markup=keyboard
        )

    elif call.data == "computer":

        keyboard = types.InlineKeyboardMarkup(row_width=2)

        btn1 = types.InlineKeyboardButton(
            text="📡 Відправити сигнал",
            callback_data="signal"
        )

        btn2 = types.InlineKeyboardButton(
            text="🔋 Вимкнути систему",
            callback_data="system"
        )

        keyboard.add(btn1, btn2)

        bot.send_message(
            call.message.chat.id,
            "Ти знайшов головний комп'ютер.",
            reply_markup=keyboard
        )

    elif call.data == "signal":

        keyboard = types.InlineKeyboardMarkup(row_width=1)

        btn1 = types.InlineKeyboardButton(
            text="🔄 Почати знову",
            callback_data="restart"
        )

        keyboard.add(btn1)

        bot.send_message(
            call.message.chat.id,
            "🛸 Тебе врятували. Ти переміг!",
            reply_markup=keyboard
        )

    elif call.data == "system":

        keyboard = types.InlineKeyboardMarkup(row_width=1)

        btn1 = types.InlineKeyboardButton(
            text="🔄 Почати знову",
            callback_data="restart"
        )

        keyboard.add(btn1)

        bot.send_message(
            call.message.chat.id,
            "⚠️ Корабель зупинився. Поразка.",
            reply_markup=keyboard
        )

    elif call.data == "restart":

        keyboard = types.InlineKeyboardMarkup(row_width=2)

        btn1 = types.InlineKeyboardButton(
            text="✅ Так",
            callback_data="yes"
        )

        btn2 = types.InlineKeyboardButton(
            text="❌ Ні",
            callback_data="no"
        )

        keyboard.add(btn1, btn2)

        bot.send_message(
            call.message.chat.id,
            "Хочеш пройти квест ще раз?",
            reply_markup=keyboard
        )

bot.polling(none_stop=True, interval=0)