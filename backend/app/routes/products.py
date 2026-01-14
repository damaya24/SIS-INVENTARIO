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
'''EDITAR PRODUCTO'''
@router.put("/{product_id}")
def update_product(
    product_id: int,
    product: dict,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_product = db.query(Product).filter(Product.id == product_id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    for key, value in product.items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product

"""ELIMINAR PRODUCTO"""
@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    db.delete(product)
    db.commit()
    return {"message": "Producto eliminado"}

