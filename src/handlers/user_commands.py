import psutil
import random



class Commands:
    def __init__(self, bot):
        self.bot = bot

        @bot.message_handler(func=lambda message: message.text == "старт") #start
        @bot.message_handler(commands=["start"])
        def send_welcome(message):
            if message.chat.id == 6815312419:
                bot.send_message(message.chat.id, "<b>Ало хуеосос, хватит меня тыкать, иди код допиши</b>")
            elif message.chat.id == 6870674749:
                bot.send_message(message.chat.id, "<b>Приветик, солнышко! <3</b>")
            else:
                bot.send_message(message.chat.id, "<b>Привет, я телеграм бот написанный @californidze\n\n"
                         "Я тут что-бы в чате появилась игра! СиськоМер + РП команды которых нету в ирисе</b>")

        @bot.message_handler(commands=["bot"])
        @bot.message_handler(func=lambda message: message.text == "бот")
        def send_bot(message):
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            response = f"<b>Работаю ^_^</b>\n\n" \
               f"<b>Нагрузка на процессор:</b> <code>{cpu_usage}%</code>\n" \
               f"<b>Нагрузка на оперативную память:</b> <code>{memory_usage}%</code>"
            bot.send_message(message.chat.id, response)
            
        @bot.message_handler(commands=["id"])
        def id(message):
            bot.send_message(message.chat.id, f'<b>@{message.from_user.username}, Твое ID:</b> <code>{message.from_user.id}</code>')
            
        @bot.message_handler(commands=['start_game'])
        def game(message):
            size = random.randint(-5, 10)
            bot.send_message(message.chat.id, f"<b>@{message.from_user.username} сыграл и получил {size}. Сыграть ещё раз сможешь через 24ч</b>")
            
        #@bot.message_handler(commands=['token'])
        #def token(message):
            #bot