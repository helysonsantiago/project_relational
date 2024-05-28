from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from auth.auth import get_current_user_in_roles
from auth.role import UserRole
from database import get_db
from repositories.recepcionistaRepository import recepcionistaRepository
from schemas.recepcionista import recepcionistaResponse, recepcionistaRequest
from models.recepcionistaModel import Recepcionista

router = APIRouter(
    prefix="/api/recepcionista",
    tags=["Recepcionista"]
)

@router.post("/", response_model=recepcionistaResponse, status_code=status.HTTP_201_CREATED)
def create(request: recepcionistaRequest, db: Session = Depends(get_db), current_user: str = Depends(get_current_user_in_roles([UserRole.ADMIN.value]))):
    recepcionista = recepcionistaRepository.save(db, Recepcionista(**request.dict()))
    return recepcionistaResponse.from_orm(recepcionista)

@router.get("/", response_model=list[recepcionistaResponse])
def find_all(db: Session = Depends(get_db)):
    recepcionistas = recepcionistaRepository.find_all(db)
    return [recepcionistaResponse.from_orm(recepcionista) for recepcionista in recepcionistas]

@router.get("/{id}", response_model=recepcionistaResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    recepcionista = recepcionistaRepository.find_by_id(db, id)
    if not recepcionista:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recepcionista não encontrado(a)"
        )
    return recepcionistaResponse.from_orm(recepcionista)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user_in_roles([UserRole.ADMIN.value]))):
    if not recepcionistaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recepcionista não encontrado(a)"
        )
    recepcionistaRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=recepcionistaResponse)
def update(id: int, request: recepcionistaRequest, db: Session = Depends(get_db), current_user: str = Depends(get_current_user_in_roles([UserRole.ADMIN.value]))):
    if not recepcionistaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recepcionista não encontrado(a)"
        )
    recepcionista = recepcionistaRepository.save(db, Recepcionista(id=id, **request.dict()))
    return recepcionistaResponse.from_orm(recepcionista)