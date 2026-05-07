from fastapi import FastAPI
from .database import Base, engine
from .routers import items

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(items.router)


# Código que se añade
@app.get("/status")
def version():
    return {"status": "Apellidos, Nombre - v.xx"}
