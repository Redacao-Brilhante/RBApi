from sqlalchemy import Column, ForeignKey, Integer, String, PickleType
from sqlalchemy.orm import backref, relationship
from rbapi.databaseengine.database import Base


class Document(Base):
    __tablename__ = 'documents'

    documentid = Column(Integer, primary_key=True)
    title = Column(String, nullable=True)
    file = Column(PickleType, nullable=True)

    ordereddocumentid = relationship('OrderedDocument')
