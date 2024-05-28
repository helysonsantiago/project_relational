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
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(db: Session, email: str, password: str):
    user = db.query(Dentista).filter(Dentista.email == email).first()
    if not user:
        user = db.query(Recepcionista).filter(Recepcionista.email == email).first()
    if not user:
        user = db.query(Admin).filter(Admin.email == email).first()
    if not user or not verify_password(password, user.senha):
        return None
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido, acesso negado",
        )


def get_current_user_in_roles(roles: List[str]):
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