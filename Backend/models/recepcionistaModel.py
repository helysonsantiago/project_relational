from sqlalchemy import String
from sqlalchemy.orm  import Mapped, mapped_column
from models.GenericoModel import UsuarioBase


class Recepcionista(UsuarioBase):
    __tablename__ = "RECEPCIONISTA"

    role : Mapped[str] = mapped_column(String, default='RECEPCIONISTA')
   
    _mapper_args_ = {
        'polymorphic_identity':'RECEPCIONISTA',
        'concrete': True
   }
    