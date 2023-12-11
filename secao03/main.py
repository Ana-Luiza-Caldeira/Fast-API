from typing import List, Optional, Any, Dict
from fastapi import FastAPI, HTTPException, status, Response, Path, Query, Header, Depends
from models import Curso, cursos
from fastapi.responses import JSONResponse

from time import sleep

def fake_db():
    try:
        print('Abrindo conexão com o BD...')
        sleep(1)
    finally:
        print('Fechando conexão com o BD...')
        sleep(1)

app = FastAPI(title="API de Cursos da Geek University", version="0.0.1", description="Uma API para estudos do FastAPI")

@app.get('/cursos', description='Retorna todos os cursos ou uma lista vazia.', summary='Retorna todos os cursos', response_model=List[Curso], response_description='Cursos encontrados com sucesso!')
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

@app.get('/cursos/{curso_id}', description='Retorna um curso a partir de um ID, caso seja encontrado.', summary='Retorna um curso')
async def get_curso(curso_id: int = Path(..., title='ID do curso', description='Deve ser entre 1 e 2', gt=0, lt=3), db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado!')

@app.post('/cursos', status_code=status.HTTP_201_CREATED, description='Cria um curso.', summary='Cria um curso', response_model=Curso)
async def post_curso(curso: Curso,db: Any = Depends(fake_db)):
    next_id = len(cursos) +1
    cursos[next_id] = curso
    del curso.id
    return curso

@app.put('/cursos/{curso_id}', description='Atualiza um curso a partir de um ID, caso seja encontrado.', summary='Atualiza um curso')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Não existe um curso com o id {curso_id}')

@app.delete('/cursos/{curso_id}', description='Deleta um curso a partir de um ID, caso seja encontrado.', summary='Deleta um curso')
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Não existe um curso com o id {curso_id}')

@app.get('/calculadora')
async def calculadora(a:int = Query(default=None, gt=5), b:int = Query(default=None, gt=10), x_geek:str = Header(default=None), c:Optional[int]=None):
    sum = a + b
    if c:
        sum = sum + c

    return {"sum":sum}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)