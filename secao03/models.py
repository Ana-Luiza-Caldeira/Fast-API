from typing import Optional
from pydantic import BaseModel, validator

class Curso(BaseModel):
    id:Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O título deve conter pelo menos 3 palavras!')
        
        return value

cursos = [
    Curso(id = 1, titulo = "Programação para leigos", aulas = 112, horas = 58),
    Curso(id = 2, titulo = "Algoritmos e Lógica de Programação", aulas = 87, horas = 65)
]