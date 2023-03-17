import logging

import telebot

from settings import LOGGING_BOT_TOKEN, ADMINISTRATOR_CHAT_ID

logging.basicConfig(
    format="%(asctime)s => %(filename)s => %(levelname)s => %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
    filename="logs.txt"
)

main_formater = logging.Formatter("%(asctime)s => %(filename)s => %(levelname)s => %(message)s")

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(main_formater)

file_handler = logging.FileHandler(filename="important_logs.txt")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(main_formater)


class TelegramBotHandler(logging.Handler):
    def __init__(self, API_KEY, chat_id):
        super().__init__()
        self.key = API_KEY
        self.chat_id = chat_id

    def emit(self, record):
        bot = telebot.TeleBot(self.key)

        bot.send_message(self.chat_id, self.format(record))


telegram = TelegramBotHandler(LOGGING_BOT_TOKEN, ADMINISTRATOR_CHAT_ID)
telegram.setLevel(logging.CRITICAL)
telegram.setFormatter(main_formater)

root_logger = logging.getLogger("")
root_logger.addHandler(console)
root_logger.addHandler(file_handler)
root_logger.addHandler(telegram)