import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .adapter import DBAdapter
from .exceptions import DBError

load_dotenv()
DEBUG = os.getenv("DEBUG") in ('1', 'true', 'True', 'TRUE')


def setup_session_maker():
    sqlite_filepath = os.environ.get('DB_URL')
    # TODO: change DB engine
    db_url = f"sqlite:///{sqlite_filepath}"
    db_engine = create_engine(db_url, echo=DEBUG)
    db_session_maker = sessionmaker(bind=db_engine)

    return db_session_maker
