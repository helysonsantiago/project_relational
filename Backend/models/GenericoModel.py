from sqlalchemy import Column, Integer, String, TIMESTAMP, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column

from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

from datetime import datetime

from database import Base

class UsuarioBase(Base):
    __abstract__ = True  # Esta classe é abstrata e não deve ser instanciada diretamente.

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(10), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text('CURRENT_TIMESTAMP')  # Define o valor padrão como o timestamp atual no momento da criação.
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text('CURRENT_TIMESTAMP'),  # Define o valor padrão como o timestamp atual no momento da criação.
        onupdate=datetime.now  # Atualiza o valor para o timestamp atual sempre que o registro for atualizado.
    )

    """
    Classe base para usuários, contendo os campos comuns.
    
    Campos:
        - id: Identificador único do usuário.
        - nome: Nome do usuário.
        - email: E-mail do usuário, deve ser único.
        - senha: Senha do usuário.
        - created_at: Timestamp de quando o usuário foi criado.
        - updated_at: Timestamp de quando o usuário foi atualizado pela última vez.
    """
