
from pydantic import BaseModel


class recepcionistaBase(BaseModel):
    nome: str
    email: str
    senha: str
    

class recepcionistaRequest(recepcionistaBase):
    ...

class recepcionistaResponse(recepcionistaBase):
    id: int

    class Config:
        orm_mode = True