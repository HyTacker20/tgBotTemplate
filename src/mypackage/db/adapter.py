import logging
from typing import Optional, Callable, Iterable, Type, Tuple

from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from .exceptions import DBError


class DBAdapter:
    def __init__(self, session: Session, logger: logging.Logger):
        self.logger = logger
        self.session = session

    def _session_wrapper(self, method: Callable, *args, **kwargs):
        try:
            return method(self.session, *args, **kwargs)
        except IntegrityError as e:
            self.logger.debug(e)
            return False
        except SQLAlchemyError as e:
            self.logger.exception(e)
            raise DBError(f"Error occurred while {method.__name__}: {e}")

    # TODO: register your DB operations here
