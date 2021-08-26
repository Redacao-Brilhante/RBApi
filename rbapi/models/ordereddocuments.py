from datetime import datetime

from sqlalchemy import UniqueConstraint, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from rbapi.databaseengine.database import Base


class OrderedDocument(Base):
    __tablename__ = "ordereddocument"
    __table_args__ = (UniqueConstraint("position"),)

    ordereddocumentstid = Column(Integer, primary_key=True)

    documentid = Column(Integer, ForeignKey("documents.documentid"), nullable=False)
    document = relationship("Document")

    position = Column(Integer, nullable=False)

    groupname = Column(String, nullable=False)

    datecreated = Column(DateTime, default=datetime.now)
