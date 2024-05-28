from typing import Optional
from pydantic import BaseModel, validator


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class User(BaseModel):
    email: str

    class Config:
        orm_mode = True
                

class UserUpdate(BaseModel):

    nome: Optional[str] = None
    email : Optional[str] = None
    senha: Optional[str] = None 


class UserCreate(BaseModel):
    role : str
    nome: str
    email: str   
    senha: str


    @validator('senha')
    def password_strength(cls, v: str) -> str:
        if len(v) < 6:
            raise ValueError('A senha deve ter pelo menos 6 caracteres')
        if not any(char.isdigit() for char in v):
            raise ValueError('A senha deve conter pelo menos um dígito')
        if not any(char.isupper() for char in v):
            raise ValueError('A senha deve conter pelo menos uma letra maiúscula')
        if not any(char.islower() for char in v):
            raise ValueError('A senha deve conter pelo menos uma letra minúscula')
        return v