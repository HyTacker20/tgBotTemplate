from telebot import TeleBot

from src.mypackage.bot.handlers import (
    basic_commands,
    unhandled
)


def register_handlers(bot: TeleBot):
    basic_commands.register_handlers(bot)
    unhandled.register_handlers(bot)

    # TODO: register your handlers here
