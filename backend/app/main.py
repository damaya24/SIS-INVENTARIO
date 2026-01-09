from typing import Union
from fastapi import FastAPI
from app.database import engine, Base
from app.routes import auth, products

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Inventario")

app.include_router(auth.router)
app.include_router(products.router)


@app.get("/")
def root():
    return {"status": "API Inventario activa"}
