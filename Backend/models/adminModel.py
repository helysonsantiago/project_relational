from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from models.GenericoModel import UsuarioBase

class Admin(UsuarioBase):
    """
    Modelo de banco de dados para o papel de Admin, herdando de UsuarioBase.

    Atributos:
        role (str): Define o papel do usuário como 'ADMIN'. O valor padrão é 'ADMIN'.
    """
    __tablename__ = "ADMIN"

    role: Mapped[str] = mapped_column(String, default='ADMIN')
     
    _mapper_args_ = {
        'polymorphic_identity': 'ADMIN',  # Define a identidade polimórfica para o modelo Admin
        'concrete': True  # Especifica que esta classe é uma tabela concreta no banco de dados
    }
