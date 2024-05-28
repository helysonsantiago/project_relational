from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from auth.auth import get_current_user_in_roles
from auth.role import UserRole
from database import get_db
from repositories.dentistaRepository import dentistaRepository
from schemas.dentistaSchema import dentistaResponse, dentistaRequest
from models.dentistaModel import Dentista

router = APIRouter(
    prefix="/api/dentista",
    tags=["Dentista"]
)

@router.post("/", response_model=dentistaResponse, status_code=status.HTTP_201_CREATED)
def create(request: dentistaRequest, db: Session = Depends(get_db), current_user: str = Depends(get_current_user_in_roles([UserRole.ADMIN.value]))):
    dentista = dentistaRepository.save(db, Dentista(**request.dict()))
    return dentistaResponse.from_orm(dentista)

@router.get("/", response_model=list[dentistaResponse])
def find_all(db: Session = Depends(get_db)):
    dentistas = dentistaRepository.find_all(db)
    return [dentistaResponse.from_orm(dentista) for dentista in dentistas]

@router.get("/{id}", response_model=dentistaResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    dentista = dentistaRepository.find_by_id(db, id)
    if not dentista:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Dentista não encontrado"
        )
    return dentistaResponse.from_orm(dentista)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user_in_roles([UserRole.ADMIN.value]))):
    if not dentistaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Dentista não encontrado"
        )
    dentistaRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=dentistaResponse)
def update(id: int, request: dentistaRequest, db: Session = Depends(get_db), current_user: str = Depends(get_current_user_in_roles([UserRole.ADMIN.value]))):
    if not dentistaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Dentista não encontrado"
        )
    dentista = dentistaRepository.save(db, Dentista(id=id, **request.dict()))
    return dentistaResponse.from_orm(dentista)