import logging

from sqlalchemy.orm import sessionmaker
from telebot.handler_backends import BaseMiddleware

from ...db import DBAdapter


class ExtraArgumentsMiddleware(BaseMiddleware):
    def __init__(
            self,
            db_session_maker: sessionmaker,
            db_logger: logging.Logger,
            logger: logging.Logger,
            page_size: int):
        super().__init__()
        self.db_session_maker = db_session_maker
        self.db_logger = db_logger
        self.logger = logger
        self.page_size = page_size
        self.update_types = ['message', 'callback_query']

    # argument naming is kept from the base class to avoid possible errors if passed as kwargs
    def pre_process(self, message, data: dict):
        # passing extra arguments to handlers
        db_adapter = DBAdapter(self.db_session_maker(), self.db_logger)
        data['db_adapter'] = db_adapter
        data['logger'] = self.logger
        data['page_size'] = self.page_size

    # argument naming is kept from the base class to avoid possible errors if passed as kwargs
    def post_process(self, message, data: dict, exception: BaseException):
        data['db_adapter'].session.close()
