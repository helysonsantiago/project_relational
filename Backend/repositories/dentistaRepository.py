import bcrypt
from sqlalchemy.orm import Session

from models.dentistaModel import Dentista

class dentistaRepository:
    @staticmethod
    def find_all(db: Session) -> list[Dentista]:
        return db.query(Dentista).all()

    @staticmethod
    def save(db: Session, dentista: Dentista) -> Dentista:
        if dentista.id:
            db.merge(dentista)
        else:
            hashed_password = bcrypt.hashpw(dentista.senha.encode(), bcrypt.gensalt())
            dentista.senha = hashed_password.decode()
            db.add(dentista)
        db.commit()
        return dentista

    @staticmethod
    def find_by_id(db: Session, id: int) -> Dentista:
        return db.query(Dentista).filter(Dentista.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Dentista).filter(Dentista.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        dentista = db.query(Dentista).filter(Dentista.id == id).first()
        if dentista is not None:
            db.delete(dentista)
            db.commit()
