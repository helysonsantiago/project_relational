from sqlalchemy import Column, Integer, String, TIMESTAMP, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column

from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

from datetime import datetime

from database import Base

class UsuarioBase(Base):
    __abstract__ = True 

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(10), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text('CURRENT_TIMESTAMP')

    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text('CURRENT_TIMESTAMP'),
        onupdate=datetime.now
    )
    
    
