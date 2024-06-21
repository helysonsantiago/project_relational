import bcrypt
from sqlalchemy.orm import Session
from models.adminModel import Admin

class adminRepository:
    """
    Repositório para operações CRUD relacionadas ao modelo Admin.

    Métodos:
        save(db: Session, admin: Admin) -> Admin:
            Salva um objeto Admin no banco de dados. Se o admin já possui um ID, ele é atualizado;
            caso contrário, um novo admin é criado com uma senha criptografada.
    """

    @staticmethod
    def save(db: Session, admin: Admin) -> Admin:
        """
        Salva um objeto Admin no banco de dados.

        Parâmetros:
            db (Session): Sessão do banco de dados.
            admin (Admin): Instância de Admin a ser salva.

        Retorna:
            Admin: A instância de Admin salva.
        """
        if admin.id:
            # Atualiza um admin existente
            db.merge(admin)
        else:
            # Cria um novo admin com a senha criptografada
            hashed_password = bcrypt.hashpw(admin.senha.encode(), bcrypt.gensalt())
            admin.senha = hashed_password.decode()
            db.add(admin)
        db.commit()
        return admin
