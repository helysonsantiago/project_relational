from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from repositories.adminRepository import adminRepository
from schemas.adminSchema import adminResponse, adminRequest
from models.adminModel import Admin

router = APIRouter(
    prefix="/api/admin",
    tags=["Admin"]
)

@router.post("/", response_model=adminResponse, status_code=status.HTTP_201_CREATED)
def create(request: adminRequest, db: Session = Depends(get_db)):
    admin = adminRepository.save(db, Admin(**request.dict()))
    return adminResponse.from_orm(admin)

