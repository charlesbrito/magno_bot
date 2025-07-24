from pydantic import BaseModel, EmailStr

class Cliente(BaseModel):
    nome: str
    email: EmailStr
    banca: int
    