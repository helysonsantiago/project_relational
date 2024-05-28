from sqlalchemy import String
from sqlalchemy.orm  import Mapped, mapped_column
from models.GenericoModel import UsuarioBase


class Dentista(UsuarioBase):
    __tablename__ = "DENTISTA"

    role : Mapped[str] = mapped_column(String, default='DENTISTA')
     
    _mapper_args_ = {
        'polymorphic_identity':'DENTISTA',
        'concrete': True
   }
  
  