from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship
from rbapi.databaseengine.database import Base


class Documents(Base):
    __tablename__ = 'Documents'

    documentsid = Column(Integer, primary_key=True)
    title = Column(String)
