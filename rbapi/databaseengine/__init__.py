from .db_session import db_session, engine
from .base import Base
from ..models.document import Document
from ..models.ordereddocuments import OrderedDocument


def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    file = open('tests/resources/cartilha_do_participante.pdf', 'rb').read()
    initial_document = Document(title="Cartilha do Participante", file=file)

    db_session.add(initial_document)
    db_session.commit()

    ordereddocuments = OrderedDocument(
        documentid=initial_document.documentid,
        position=1,
        groupname="Pdf ENEM")

    db_session.add(ordereddocuments)
    db_session.commit()


