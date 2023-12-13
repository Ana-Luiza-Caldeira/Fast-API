from typing import Optional, List
from pydantic import BaseModel, EmailStr
from schemas.artigo_schema import ArtigoSchema

class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    admin: bool = False

    class Config:
        orm_mode = True

class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str

class UsuarioSchamaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]

class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    admin: Optional[bool]
    senha: Optional[str]
