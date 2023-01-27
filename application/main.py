from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine
import datetime

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/registry", response_model=schemas.Registry)
def create_registry(registry: schemas.RegistryCreate, db: Session = Depends(get_db)):
    date_now = datetime.datetime.now()
    db_registry = models.Registry(day=date_now.strftime("%d"),
                                  month=date_now.strftime("%m"),
                                  year=date_now.strftime("%Y"),
                                  hour=date_now.strftime("%H"),
                                  minute=date_now.strftime("%M"),
                                  temperatura_ambiente=registry.temperatura_ambiente,
                                  humedad_ambiente=registry.humedad_ambiente,
                                  humedad_planta=registry.humedad_planta,
                                  luminosidad=registry.luminosidad,
                                  riego=registry.riego
                                  )

    return crud.create_registry(db=db, db_registry=db_registry)
