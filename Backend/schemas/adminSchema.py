from pydantic import BaseModel


class adminBase(BaseModel):
    nome: str
    email: str
    senha: str


class adminRequest(adminBase):
    ...

class adminResponse(adminBase):
    id: int

    class Config:
        orm_mode = True