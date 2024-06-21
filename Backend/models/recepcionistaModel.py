from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from models.GenericoModel import UsuarioBase

class Recepcionista(UsuarioBase):
    """
    Modelo de banco de dados para o papel de Recepcionista, herdando de UsuarioBase.

    Atributos:
        role (str): Define o papel do usuário como 'RECEPCIONISTA'. O valor padrão é 'RECEPCIONISTA'.
    """
    __tablename__ = "RECEPCIONISTA"

    role: Mapped[str] = mapped_column(String, default='RECEPCIONISTA')
   
    _mapper_args_ = {
        'polymorphic_identity': 'RECEPCIONISTA',  # Define a identidade polimórfica para o modelo Recepcionista
        'concrete': True  # Especifica que esta classe é uma tabela concreta no banco de dados
    }
