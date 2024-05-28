import bcrypt
from sqlalchemy.orm import Session

from models.recepcionistaModel import Recepcionista

class recepcionistaRepository:

    @staticmethod
    def find_all(db: Session) -> list[Recepcionista]:
        return db.query(Recepcionista).all()

    @staticmethod
    def save(db: Session, recepcionista: Recepcionista) -> Recepcionista:
        if recepcionista.id:
            db.merge(recepcionista)
        else:
            hashed_password = bcrypt.hashpw(recepcionista.senha.encode(), bcrypt.gensalt())
            recepcionista.senha = hashed_password.decode()
            db.add(recepcionista)
        db.commit()
        return recepcionista

    @staticmethod
    def find_by_id(db: Session, id: int) -> Recepcionista:
        return db.query(Recepcionista).filter(Recepcionista.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Recepcionista).filter(Recepcionista.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        recepcionista = db.query(Recepcionista).filter(Recepcionista.id == id).first()
        if recepcionista is not None:
            db.delete(recepcionista)
            db.commit()
