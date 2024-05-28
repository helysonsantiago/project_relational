from pydantic import BaseModel

class dentistaBase(BaseModel):
    nome: str
    email: str
    senha: str
    cro : str

class dentistaRequest(dentistaBase):
    ...

class dentistaResponse(dentistaBase):
    id: int

    class Config:
        orm_mode = True