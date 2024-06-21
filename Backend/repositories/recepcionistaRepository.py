import bcrypt
from sqlalchemy.orm import Session
from models.recepcionistaModel import Recepcionista

class recepcionistaRepository:
    """
    Repositório para operações CRUD relacionadas ao modelo Recepcionista.

    Métodos:
        find_all(db: Session) -> list[Recepcionista]:
            Retorna uma lista com todos os recepcionistas no banco de dados.
        save(db: Session, recepcionista: Recepcionista) -> Recepcionista:
            Salva um objeto Recepcionista no banco de dados. Se o recepcionista já possui um ID, ele é atualizado;
            caso contrário, um novo recepcionista é criado com uma senha criptografada.
        find_by_id(db: Session, id: int) -> Recepcionista:
            Retorna um recepcionista pelo ID.
        exists_by_id(db: Session, id: int) -> bool:
            Verifica se um recepcionista com o ID especificado existe no banco de dados.
        delete_by_id(db: Session, id: int) -> None:
            Deleta um recepcionista pelo ID.
    """

    @staticmethod
    def find_all(db: Session) -> list[Recepcionista]:
        """
        Retorna uma lista com todos os recepcionistas no banco de dados.

        Parâmetros:
            db (Session): Sessão do banco de dados.

        Retorna:
            list[Recepcionista]: Lista de recepcionistas.
        """
        return db.query(Recepcionista).all()

    @staticmethod
    def save(db: Session, recepcionista: Recepcionista) -> Recepcionista:
        """
        Salva um objeto Recepcionista no banco de dados.

        Parâmetros:
            db (Session): Sessão do banco de dados.
            recepcionista (Recepcionista): Instância de Recepcionista a ser salva.

        Retorna:
            Recepcionista: A instância de Recepcionista salva.
        """
        if recepcionista.id:
            # Atualiza um recepcionista existente
            db.merge(recepcionista)
        else:
            # Cria um novo recepcionista com a senha criptografada
            hashed_password = bcrypt.hashpw(recepcionista.senha.encode(), bcrypt.gensalt())
            recepcionista.senha = hashed_password.decode()
            db.add(recepcionista)
        db.commit()
        return recepcionista

    @staticmethod
    def find_by_id(db: Session, id: int) -> Recepcionista:
        """
        Retorna um recepcionista pelo ID.

        Parâmetros:
            db (Session): Sessão do banco de dados.
            id (int): ID do recepcionista.

        Retorna:
            Recepcionista: A instância de Recepcionista correspondente ao ID, ou None se não encontrado.
        """
        return db.query(Recepcionista).filter(Recepcionista.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        """
        Verifica se um recepcionista com o ID especificado existe no banco de dados.

        Parâmetros:
            db (Session): Sessão do banco de dados.
            id (int): ID do recepcionista.

        Retorna:
            bool: True se o recepcionista existe, False caso contrário.
        """
        return db.query(Recepcionista).filter(Recepcionista.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        """
        Deleta um recepcionista pelo ID.

        Parâmetros:
            db (Session): Sessão do banco de dados.
            id (int): ID do recepcionista a ser deletado.

        Retorna:
            None
        """
        recepcionista = db.query(Recepcionista).filter(Recepcionista.id == id).first()
        if recepcionista is not None:
            db.delete(recepcionista)
            db.commit()
