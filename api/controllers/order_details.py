from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import models, schemas

def create(db: Session, detail: schemas.OrderDetailCreate):
    db_detail = models.OrderDetail(**detail.model_dump())
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail

def read_all(db: Session):
    return db.query(models.OrderDetail).all()

def read_one(db: Session, detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id).first()

def update(db: Session, detail_id: int, detail: schemas.OrderDetailUpdate):
    db_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id)
    if not db_detail.first():
        raise HTTPException(status_code=404, detail="Order detail not found")
    db_detail.update(detail.model_dump(exclude_unset=True), synchronize_session=False)
    db.commit()
    return db_detail.first()

def delete(db: Session, detail_id: int):
    db_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id)
    if not db_detail.first():
        raise HTTPException(status_code=404, detail="Order detail not found")
    db_detail.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)