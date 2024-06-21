from datetime import datetime, timedelta
from typing import List, Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, Header, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from models.dentistaModel import Dentista
from models.recepcionistaModel import Recepcionista
from models.adminModel import Admin
from database import get_db

SECRET_KEY = "chave_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    """
    Verifica se a senha fornecida corresponde à senha hash armazenada.
    
    :param plain_password: A senha fornecida pelo usuário.
    :param hashed_password: A senha hash armazenada no banco de dados.
    :return: True se as senhas corresponderem, False caso contrário.
    """
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, email: str, password: str):
    """
    Autentica um usuário verificando seu e-mail e senha. 
    Procura o usuário nas tabelas Dentista, Recepcionista e Admin.
    
    :param db: Sessão do banco de dados.
    :param email: E-mail do usuário.
    :param password: Senha do usuário.
    :return: O usuário autenticado se as credenciais estiverem corretas, None caso contrário.
    """
    user = db.query(Dentista).filter(Dentista.email == email).first()
    if not user:
        user = db.query(Recepcionista).filter(Recepcionista.email == email).first()
    if not user:
        user = db.query(Admin).filter(Admin.email == email).first()
    if not user or not verify_password(password, user.senha):
        return None
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Cria um token JWT para o usuário autenticado.
    
    :param data: Dados a serem codificados no token.
    :param expires_delta: Tempo de expiração do token.
    :return: O token JWT codificado.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token: str):
    """
    Decodifica o token JWT.
    
    :param token: O token JWT a ser decodificado.
    :return: O payload decodificado do token.
    :raises HTTPException: Se o token for inválido.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido, acesso negado",
        )

def get_current_user_in_roles(roles: List[str]):
    """
    Obtém o usuário atual se ele tiver uma das funções especificadas.
    
    :param roles: Lista de funções permitidas.
    :return: A função que verifica o usuário atual e suas permissões.
    :raises HTTPException: Se o usuário não tiver permissão para acessar o recurso.
    """
    def _get_current_user(token: str = Header(...), db: Session = Depends(get_db)):
        payload = decode_token(token)
        role = payload.get("role")
        print(role)
        print(roles)
        if role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permissão insuficiente para acessar este recurso",
            )
        return payload
    return _get_current_user
