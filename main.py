import telebot

import logging
from dotenv import load_dotenv
import os


from src.handlers.user_commands import Commands
from src.handlers.message import Messages
from src.utils.circl import Circle


load_dotenv()
token = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(token, parse_mode="HTML")

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

circle = Circle(bot)
commands_instance = Commands(bot)
message = Messages(bot)



# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)