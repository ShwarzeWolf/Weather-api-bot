import logging
from logging import Handler, LogRecord
from settings import CHAT_ID, LOGGING_BOT_TOKEN

import telebot


logging.basicConfig(
    format="%(asctime)s => %(filename)s => %(levelname)s => %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="logs.txt",
    level=logging.INFO
)

main_formatter = logging.Formatter("%(asctime)s => %(filename)s => %(levelname)s => %(message)s")

# All logs from INFO level we will write to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(main_formatter)

# All ERROR and CRITICAL errors we will write to another file
file = logging.FileHandler(filename="important_logs.txt")
file.setLevel(logging.ERROR)
file.setFormatter(main_formatter)


# And also, to telegram chat via special handler
class TelegramBotHandler(Handler):
    """Handler to send telegram messages using bot"""
    def __init__(self, api_key: str, chat_id: str):
        super().__init__()
        self.api_key = api_key
        self.chat_id = chat_id

    def emit(self, record: LogRecord):
        """Sends message to chat specified in .env file"""
        bot = telebot.TeleBot(self.api_key)

        bot.send_message(
            self.chat_id,
            self.format(record)
        )


telegram = TelegramBotHandler(LOGGING_BOT_TOKEN, CHAT_ID)
telegram.setLevel(logging.ERROR)
telegram.setFormatter(main_formatter)


# Getting root logger
root_logger = logging.getLogger("")

# Adding handlers and filters to the root logger
root_logger.addHandler(console)
root_logger.addHandler(file)
root_logger.addHandler(telegram)
