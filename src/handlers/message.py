



class Messages:
    def __init__(self, bot):
        self.bot = bot
         
        
        


        #xd
        @bot.message_handler(func=lambda message: message.text.lower() == "связать")
        def link_users(message):
            user1 = message.from_user.username
            user2 = message.reply_to_message.from_user.username
            if message.reply_to_message and message.reply_to_message.from_user:
                response = f"@{user1} <b>связал</b> @{user2}\nТеперь ты будешь связаным  страдать👿"
                bot.reply_to(message, response)
            else:
                bot.reply_to(message, "Не удалось определить пользователя для связи.")

        #kiss
        @bot.message_handler(func=lambda message: message.text.lower() == "засосать")
        def kiss_users(message):
            user1 = message.from_user.username
            user2 = message.reply_to_message.from_user.username
            if message.reply_to_message and message.reply_to_message.from_user:
                kiss_text = f"@{user1} <b>Люто засосал @{user2}</b>\n Оу.. полегче.. "
                bot.reply_to(message, kiss_text)
            else:
                bot.reply_to(message, "Нужно написать ответом на сообщение")
        #boom
        @bot.message_handler(func=lambda message: message.text.lower() == "взорвать")
        def boom_user(message):
            user1 = message.from_user.username
            user2 = message.reply_to_message.from_user.username
            if message.reply_to_message and message.reply_to_message.from_user:
                boom_text = f"@{user1} <b>взорвал</b> @{user2}\n Ух ебать... @{user2}, разлетелся как новость.."
                bot.reply_to(message, boom_text)
            else:
                bot.reply_to(message, "Нужно написать ответом на сообщение")

        #уничтожить
        @bot.message_handler(func=lambda message: message.text.lower() == "уничтожить")
        def boom_user(message):
            user1 = message.from_user.username
            user2 = message.reply_to_message.from_user.username
            if message.reply_to_message and message.reply_to_message.from_user:
                boom_text = f"@{user1} <b>Уничтожил</b> @{user2}\n\n@{user2}, тебя просто люто уничтожили.. Как первоклассник карандаш"
                bot.reply_to(message, boom_text)
            else:
                bot.reply_to(message, "Нужно написать ответом на сообщение")

        @bot.message_handler(func=lambda message: message.text.lower() == "выебать")
        def ntsf_users(message):
            user1 = message.from_user.username
            user2 = message.reply_to_message.from_user.username
            if message.reply_to_message and message.reply_to_message.from_user:
                boom_text = f"@{user1} <b>Насильно выебал👌👈</b> @{user2}\n\n@{user2} Надеюсь ты не залетишь)0))"
                bot.reply_to(message, boom_text)
            else:
                bot.reply_to(message, "Нужно написать ответом на сообщение")



        @bot.message_handler(func=lambda message: message.text.lower() == "судо")
        def sudo_user(message):
            bot.send_message(message.chat.id, "Судо попущеный лошок")

        @bot.message_handler(func=lambda message: message.text.lower() == "унизить")
        def gdfg(message):
            user1 = message.from_user.username
            user2 = message.reply_to_message.from_user.username
            if message.reply_to_message and message.reply_to_message.from_user:
                boom_text = f"@{user1} <b>мОрально унизил</b> @{user2}\n\n@{user2} Надеюсь ты уже побежала плакать мамочке)0))"
                bot.reply_to(message, boom_text)
            else:
                bot.reply_to(message, "Нужно написать ответом на сообщение")
        
        @bot.message_handler(func=lambda message: message.text.lower() == "хелп")
        def help_message(message):
            bot.send_message(message.chat.id, "Список всех РП КОМАНД:"
                             "\n\nСвязать • Заставить • Повесить • Уничтожить • Продать • Щекотать\n"
                             "Взорвать • Шмальнуть • Засосать • Лечь • Унизить • Арестовать\n"
                             "Наорать • Рассмешить • Ушатать • Порвать • Отрубить • Отстрелить\n"
                             "Выкопать • Выпороть • Закопать • Выпить • Наказать • Предложить\n\n"
                             "Так-же если у вас есть прикольная идея -> @californidze")

#Связать • Заставить • Повесить • Уничтожить • Продать • Щекотать 
#Взорвать • Шмальнуть • Засосать • Лечь • Унизить • Арестовать 
#Наорать • Рассмешить • Ушатать • Порвать • Отрубить • Отстрелить 
#Выкопать • Выпороть • Закопать • Выпить • Наказать • Предложить
