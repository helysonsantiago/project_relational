import bcrypt
from sqlalchemy.orm import Session
from models.dentistaModel import Dentista

class dentistaRepository:
    """
    Repositório para operações CRUD relacionadas ao modelo Dentista.

    Métodos:
        find_all(db: Session) -> list[Dentista]:
            Retorna uma lista com todos os dentistas no banco de dados.
        save(db: Session, dentista: Dentista) -> Dentista:
            Salva um objeto Dentista no banco de dados. Se o dentista já possui um ID, ele é atualizado;
            caso contrário, um novo dentista é criado com uma senha criptografada.
        find_by_id(db: Session, id: int) -> Dentista:
            Retorna um dentista pelo ID.
        exists_by_id(db: Session, id: int) -> bool:
            Verifica se um dentista com o ID especificado existe no banco de dados.
        delete_by_id(db: Session, id: int) -> None:
            Deleta um dentista pelo ID.
    """

    @staticmethod
    def find_all(db: Session) -> list[Dentista]:
        """
        Retorna uma lista com todos os dentistas no banco de dados.

        Parâmetros:
            db (Session): Sessão do banco de dados.

        Retorna:
            list[Dentista]: Lista de dentistas.
        """
        return db.query(Dentista).all()

    @staticmethod
    def save(db: Session, dentista: Dentista) -> Dentista:
        """
        Salva um objeto Dentista no banco de dados.

        Parâmetros:
            db (Session): Sessão do banco de dados.
            dentista (Dentista): Instância de Dentista a ser salva.

        Retorna:
            Dentista: A instância de Dentista salva.
        """
        if dentista.id:
            # Atualiza um dentista existente
            db.merge(dentista)
        else:
            # Cria um novo dentista com a senha criptografada
            hashed_password = bcrypt.hashpw(dentista.senha.encode(), bcrypt.gensalt())
            dentista.senha = hashed_password.decode()
            db.add(dentista)
        db.commit()
        return dentista

    @staticmethod
    def find_by_id(db: Session, id: int) -> Dentista:
        """
        Retorna um dentista pelo ID.

        Parâmetros:
            db (Session): Sessão do banco de dados.
            id (int): ID do dentista.

        Retorna:
            Dentista: A instância de Dentista correspondente ao ID, ou None se não encontrado.
        """
        return db.query(Dentista).filter(Dentista.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        """
        Verifica se um dentista com o ID especificado existe no banco de dados.

        Parâmetros:
            db (Session): Sessão do banco de dados.
            id (int): ID do dentista.

        Retorna:
            bool: True se o dentista existe, False caso contrário.
        """
        return db.query(Dentista).filter(Dentista.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        """
        Deleta um dentista pelo ID.

        Parâmetros:
            db (Session): Sessão do banco de dados.
            id (int): ID do dentista a ser deletado.

        Retorna:
            None
        """
        dentista = db.query(Dentista).filter(Dentista.id == id).first()
        if dentista is not None:
            db.delete(dentista)
            db.commit()
