from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.product import Product
from app.auth.deps import get_current_user

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def list_products(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Product).all()

@router.post("/")
def create_product(
    product: dict,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    new_product = Product(**product)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
