import bcrypt
from sqlalchemy.orm import Session
from models.adminModel import Admin
class adminRepository:

    @staticmethod
    def save(db: Session, admin: Admin ) -> Admin:
        if admin.id:
            db.merge(admin)
        else:
            hashed_password = bcrypt.hashpw(admin.senha.encode(), bcrypt.gensalt())
            admin.senha = hashed_password.decode()
            db.add(admin)
        db.commit()
        return admin
