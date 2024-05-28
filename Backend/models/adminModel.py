from sqlalchemy import String
from sqlalchemy.orm  import Mapped, mapped_column
from models.GenericoModel import UsuarioBase


class Admin(UsuarioBase):
    __tablename__ = "ADMIN"

    role : Mapped[str] = mapped_column(String, default='ADMIN')
     
    _mapper_args_ = {
        'polymorphic_identity':'ADMIN',
        'concrete': True
   }
  
  