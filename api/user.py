from sqlalchemy.orm import Session
from schema import schemas
from models import models
from fastapi import HTTPException, status
from schema.hash import Hash  # this will be done during security impl


def create(request: schemas.User, db: Session):
    hashedPassword = Hash.bcrypt(request.password)
    user = models.User(first_name=request.first_name, last_name=request.last_name, email=request.email,
                       password=hashedPassword)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="User with id {id} not found")
    return user


def get_all(db: Session):
    return db.query(models.User).all()
