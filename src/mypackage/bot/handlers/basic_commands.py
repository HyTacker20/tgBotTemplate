from logging import Logger

from dotenv import load_dotenv
from telebot import TeleBot
from telebot.types import Message

from ..messages import Messages
from ...db import DBAdapter

load_dotenv()


def start_handler(
        message: Message,
        bot: TeleBot,
        db_adapter: DBAdapter,
        logger: Logger,
        **kwargs):
    """
    Handles the /start command. Registers the user if they are not already in the database and
    verifies invite codes if provided.

    :param message: The Telegram message object
    :param bot: The Telegram bot instance
    :param db_adapter: The database adapter instance
    :param logger: The logger instance
    """
    bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}!")


def help_handler(
        message: Message,
        bot: TeleBot,
        logger: Logger,
        **kwargs):
    logger.debug(f"User {message.from_user.id} @{message.from_user.username} requested help")
    bot.send_message(message.chat.id, Messages.help)


def register_handlers(bot: TeleBot):
    bot.register_message_handler(start_handler, commands=['start'], pass_bot=True)

    bot.register_message_handler(help_handler, commands=['help'], pass_bot=True)
    bot.register_message_handler(help_handler, text_equals=Messages.help, pass_bot=True)
