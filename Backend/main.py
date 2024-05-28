from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import Dentista,Recepcionista
from database import engine, Base, get_db
from repositories import recepcionistaRepository , dentistaRepository
from schemas import recepcionistaResponse , recepcionistaRequest, dentistaResponse , dentistaRequest

Base.metadata.create_all(bind=engine)

app = FastAPI()


######################## ROTAS DENTISTA #################################

@app.post("/api/dentista", response_model=dentistaResponse, status_code=status.HTTP_201_CREATED)
def create(request: dentistaRequest , db: Session = Depends(get_db)):
    dentista =  dentistaRepository.save(db, Dentista(**request.dict()))
    return dentistaResponse.from_orm(dentista)

@app.get("/api/dentistas", response_model=list[dentistaResponse])
def find_all(db: Session = Depends(get_db)):
    dentistas =  dentistaRepository.find_all(db)
    return [dentistaResponse.from_orm(dentista) for dentista in dentistas]

@app.get("/api/dentista/{id}", response_model=dentistaResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    dentista =  dentistaRepository.find_by_id(db, id)
    if not dentista:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Dentista não encontrado"
        )
    return dentistaResponse.from_orm(dentista)

@app.delete("/api/dentista/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not  dentistaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Dentista não encontrado"
        )
    dentistaRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/api/dentista/{id}", response_model=dentistaResponse)
def update(id: int, request: dentistaRequest, db: Session = Depends(get_db)):
    if not  dentistaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Dentista não encontrado"
        )
    dentista =  dentistaRepository.save(db, Dentista(id=id, **request.dict()))
    return dentistaResponse.from_orm(dentista)


######################## ROTAS RECEPCIONISTA #################################

@app.post("/api/recepcionista", response_model=recepcionistaResponse, status_code=status.HTTP_201_CREATED)
def create(request: recepcionistaRequest , db: Session = Depends(get_db)):
    recepcionista = recepcionistaRepository.save(db, Recepcionista(**request.dict()))
    return recepcionistaResponse.from_orm(recepcionista)

@app.get("/api/recepcionistas", response_model=list[recepcionistaResponse])
def find_all(db: Session = Depends(get_db)):
    recepcionistas = recepcionistaRepository.find_all(db)
    return [recepcionistaResponse.from_orm(recepcionistas) for recepcionista in recepcionistas]

@app.get("/api/recepcionista/{id}", response_model=recepcionistaResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    recepcionista= recepcionistaRepository.find_by_id(db, id)
    if not recepcionista:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recepcionista não encontrado(a)"
        )
    return recepcionistaResponse.from_orm(recepcionista)

@app.delete("/api/recepcionista/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not recepcionistaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recepcionista não encontrado(a)"
        )
    recepcionistaRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/api/recepcionista/{id}", response_model=recepcionistaResponse)
def update(id: int, request: recepcionistaRequest, db: Session = Depends(get_db)):
    if not recepcionistaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recepcionista não encontrado(a)"
        )
    recepcionista = recepcionistaRepository.save(db, Recepcionista(id=id, **request.dict()))
    return recepcionistaResponse.from_orm(recepcionista)
