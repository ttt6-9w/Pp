import telebot

bot = telebot.TeleBot("7935120323:AAEwMhLkCgBTYkcrjUdlAIfK1ipSM23PzKo")

user_states = {}

def show_main_menu(user_id):
    bot.send_message(
        user_id,
        "Обери тему:\n"
        "🎬 Фільми\n"
        "🎮 Ігри\n"
        "🎵 Музика\n\n"
        "Напиши: Фільми, Ігри або Музика"
    )

@bot.message_handler(content_types=['text'])
def handle_text(message):

    user_id = message.from_user.id
    text = message.text.lower()

    if user_id not in user_states:
        user_states[user_id] = "main"

    if text == "/start":

        user_states[user_id] = "main"

        bot.send_message(
            user_id,
            "Привіт! Я бот з пам'яттю діалогу 🤖"
        )

        show_main_menu(user_id)

    elif text == "назад":

        user_states[user_id] = "main"

        bot.send_message(
            user_id,
            "Ти повернувся у головне меню."
        )

        show_main_menu(user_id)

    elif user_states[user_id] == "main":

        if text == "фільми":

            user_states[user_id] = "movies"

            bot.send_message(
                user_id,
                "🎬 Добре! Про що хочеш поговорити?\n\n"
                "Жанри\n"
                "Актори\n"
                "Улюблений фільм\n\n"
                "Для повернення напиши: Назад"
            )

        elif text == "ігри":

            user_states[user_id] = "games"

            bot.send_message(
                user_id,
                "🎮 Круто! Що саме?\n\n"
                "Жанри\n"
                "Улюблена гра\n"
                "Онлайн ігри\n\n"
                "Для повернення напиши: Назад"
            )

        elif text == "музика":

            user_states[user_id] = "music"

            bot.send_message(
                user_id,
                "🎵 Любиш музику? Обери:\n\n"
                "Жанри\n"
                "Улюблений співак\n"
                "Улюблена пісня\n\n"
                "Для повернення напиши: Назад"
            )

        else:
            bot.send_message(
                user_id,
                "Я не зрозумів 😅\n"
                "Напиши: Фільми, Ігри або Музика"
            )

    elif user_states[user_id] == "movies":

        if text == "жанри":

            user_states[user_id] = "movie_genres"

            bot.send_message(
                user_id,
                "🎬 Обери жанр:\n\n"
                "Жахи\n"
                "Фантастика\n"
                "Комедія\n"
                "Бойовик\n\n"
                "Напиши Назад для повернення."
            )

        elif text == "актори":
            bot.send_message(
                user_id,
                "🎭 Відомі актори:\n"
                "- Арнольд Шварценеггер\n"
                "- Кіану Рівз\n"
                "- Роберт Дауні молодший\n"
                "- Том Голланд\n"
                "- Леонардо Ді Капріо\n"
                "- Райан Гослінг"
            )

        elif text == "улюблений фільм":
            bot.send_message(
                user_id,
                "📽 Хороші фільми:\n"
                "- Термінатор\n"
                "- Матриця\n"
                "- Інтерстеллар\n"
                "- Бойцівський клуб\n"
                "- Blade Runner 2049\n"
                "- Джон Вік"
            )

        else:
            bot.send_message(
                user_id,
                "Я не зрозумів 😅\n"
                "Напиши: Жанри, Актори або Улюблений фільм"
            )

    elif user_states[user_id] == "movie_genres":

        if text == "жахи":
            bot.send_message(
                user_id,
                "👻 Фільми жахів:\n"
                "- Астрал\n"
                "- Закляття\n"
                "- Пила\n"
                "- Воно\n"
                "- Тихе місце"
            )

        elif text == "фантастика":
            bot.send_message(
                user_id,
                "🚀 Фантастика:\n"
                "- Матриця\n"
                "- Інтерстеллар\n"
                "- Термінатор\n"
                "- Дюна\n"
                "- Blade Runner 2049"
            )

        elif text == "комедія":
            bot.send_message(
                user_id,
                "😂 Комедії:\n"
                "- Маска\n"
                "- Один вдома\n"
                "- Дедпул\n"
                "- Мачо і ботан\n"
                "- Брюс Всемогутній"
            )

        elif text == "бойовик":
            bot.send_message(
                user_id,
                "💥 Бойовики:\n"
                "- Джон Вік\n"
                "- Ніхто\n"
                "- Форсаж\n"
                "- Міцний горішок\n"
                "- Месники"
            )

        elif text == "назад":

            user_states[user_id] = "movies"

            bot.send_message(
                user_id,
                "Ти повернувся до розділу Фільми 🎬"
            )

        else:
            bot.send_message(
                user_id,
                "Я не зрозумів 😅\n"
                "Напиши: Жахи, Фантастика, Комедія або Бойовик"
            )

    elif user_states[user_id] == "games":

        if text == "жанри":
            bot.send_message(
                user_id,
                "🎮 Жанри ігор:\n"
                "- RPG\n"
                "- Шутери\n"
                "- Виживання\n"
                "- Хорори\n"
                "- Гонки\n"
                "- Пісочниці"
            )

        elif text == "улюблена гра":
            bot.send_message(
                user_id,
                "🔥 Популярні ігри:\n"
                "- Detroit: Become Human\n"
                "- Minecraft\n"
                "- GTA V\n"
                "- Cyberpunk 2077\n"
                "- Red Dead Redemption 2\n"
                "- The Last of Us"
            )

        elif text == "онлайн ігри":
            bot.send_message(
                user_id,
                "🌐 Онлайн ігри:\n"
                "- Fortnite\n"
                "- CS2\n"
                "- Roblox\n"
                "- Valorant\n"
                "- PUBG\n"
                "- Apex Legends"
            )

        else:
            bot.send_message(
                user_id,
                "Я не зрозумів 😅\n"
                "Напиши: Жанри, Улюблена гра або Онлайн ігри"
            )

    elif user_states[user_id] == "music":

        if text == "жанри":
            bot.send_message(
                user_id,
                "🎵 Жанри музики:\n"
                "- Рок\n"
                "- Реп\n"
                "- Фонк\n"
                "- Поп\n"
                "- Електронна музика\n"
                "- Lo-fi"
            )

        elif text == "улюблений співак":
            bot.send_message(
                user_id,
                "🎤 Відомі виконавці:\n"
                "- The Weeknd\n"
                "- Eminem\n"
                "- Travis Scott\n"
                "- Imagine Dragons\n"
                "- Linkin Park\n"
                "- Arctic Monkeys"
            )

        elif text == "улюблена пісня":
            bot.send_message(
                user_id,
                "🎶 Популярні пісні:\n"
                "- Blinding Lights\n"
                "- Mockingbird\n"
                "- Numb\n"
                "- Starboy\n"
                "- Believer\n"
                "- Sweater Weather"
            )

        else:
            bot.send_message(
                user_id,
                "Я не зрозумів 😅\n"
                "Напиши: Жанри, Улюблений співак або Улюблена пісня"
            )

bot.polling(none_stop=True)