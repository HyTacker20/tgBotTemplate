import logging

from sqlalchemy.orm import sessionmaker
from telebot import TeleBot

from .callback_query_antiflood import CallbackQueryAntiFloodMiddleware
from .extra_arguments import ExtraArgumentsMiddleware
from .message_antiflood import MessageAntiFloodMiddleware


def setup_middlewares(
        bot: TeleBot,
        db_session_maker: sessionmaker,
        db_logger: logging.Logger,
        timeout_message: str,
        timeout: float,
        logger: logging.Logger,
        page_size: int):
    # TODO: setup all middlewares here
    bot.setup_middleware(MessageAntiFloodMiddleware(bot, timeout_message, timeout))
    bot.setup_middleware(CallbackQueryAntiFloodMiddleware(bot, timeout_message, timeout))
    bot.setup_middleware(ExtraArgumentsMiddleware(db_session_maker, db_logger, logger, page_size))
    pass
