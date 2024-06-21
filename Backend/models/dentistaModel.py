from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from models.GenericoModel import UsuarioBase

class Dentista(UsuarioBase):
    """
    Modelo de banco de dados para o papel de Dentista, herdando de UsuarioBase.

    Atributos:
        role (str): Define o papel do usuário como 'DENTISTA'. O valor padrão é 'DENTISTA'.
    """
    __tablename__ = "DENTISTA"

    role: Mapped[str] = mapped_column(String, default='DENTISTA')
     
    _mapper_args_ = {
        'polymorphic_identity': 'DENTISTA',  # Define a identidade polimórfica para o modelo Dentista
        'concrete': True  # Especifica que esta classe é uma tabela concreta no banco de dados
    }
