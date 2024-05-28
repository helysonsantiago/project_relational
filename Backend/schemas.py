from pydantic import BaseModel, validator
from typing import Optional




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


class recepcionistaBase(BaseModel):
    nome: str
    email: str
    senha: int
    

class dentistaBase(recepcionistaBase):
    cro : str



class dentistaRequest(dentistaBase):
    ...

class recepcionistaRequest(recepcionistaBase):
    ...

class dentistaResponse(dentistaBase):
    id: int

    class Config:
        orm_mode = True

class recepcionistaResponse(recepcionistaBase):
    id: int

    class Config:
        orm_mode = True