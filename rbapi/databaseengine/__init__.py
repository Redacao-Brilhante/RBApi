from .db_session import db_session, engine
from .base import Base


def init_db():

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
