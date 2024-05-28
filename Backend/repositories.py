from sqlalchemy.orm import Session

from models import Dentista , Recepcionista

class dentistaRepository:
    @staticmethod
    def find_all(db: Session) -> list[Dentista]:
        return db.query(Dentista).all()

    @staticmethod
    def save(db: Session, dentista: Dentista) -> Dentista:
        if dentista.id:
            db.merge(dentista)
        else:
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


class recepcionistaRepository:
    @staticmethod
    def find_all(db: Session) -> list[Recepcionista]:
        return db.query(Recepcionista).all()

    @staticmethod
    def save(db: Session, recepcionista: Recepcionista) -> Recepcionista:
        if recepcionista.id:
            db.merge(recepcionista)
        else:
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
