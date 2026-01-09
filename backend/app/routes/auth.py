from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.database import SessionLocal
from app.models.user import User
from app.auth.hash import verify_password
from app.auth.jwt import create_token

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form.username).first()

    if not user or not verify_password(form.password, user.password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    token = create_token({
        "user_id": user.id,
        "rol": user.rol
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }

