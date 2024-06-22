from sqlalchemy.orm import Session
from models import models
from schema import schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.query(models.User).all()
    return blogs


# our req data is pulled from schemas.Blog, while actual data is pulled from db
def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title,
                           body=request.body, user_id=1)  # 1?
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if blog:
        return blog
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Blog with id {id} not found.")


def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Blog with id {id} not found.")
    blog.update(request.__dict__)  # can be done with **request?
    db.commit()
    return "Updated"


def delete(id: int, db: Session):
    blog_to_delete = db.query(models.Blog).filter(models.User.id == id)

    if not blog_to_delete.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Blog with id {id} not found.")
    blog_to_delete.delete(synchronize_session=False)
    db.commit()
    return "done"
