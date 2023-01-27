from sqlalchemy.orm import Session
from . import models, schemas
import datetime


def get_registry(db: Session, registry_id: int):
    return db.query(models.Registry).filter(models.Registry.id == registry_id).first()


def create_registry(db: Session, db_registry: schemas.Registry):
    db.add(db_registry)
    db.commit()
    db.refresh(db_registry)
    return db_registry
