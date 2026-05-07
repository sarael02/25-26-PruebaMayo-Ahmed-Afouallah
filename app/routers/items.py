from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, database
from pydantic import BaseModel, ConfigDict
from typing import List

router = APIRouter(prefix="/items", tags=["items"])


class ItemCreate(BaseModel):
    nombre: str
    descripcion: str = None
    cantidad: int
    precio_unitario: float


class ItemOut(ItemCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
    # class Config:
    #     # orm_mode = True
    #     from_attributes = True


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ItemOut)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get("/", response_model=List[ItemOut])
def read_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()


@router.get("/{item_id}", response_model=ItemOut)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return item


@router.put("/{item_id}", response_model=ItemOut)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(db_item)
    db.commit()
    return {"message": "Producto eliminado"}
