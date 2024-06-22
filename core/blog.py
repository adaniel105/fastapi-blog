from schema.oa2 import get_current_user
from sqlalchemy.orm import Session
from database import configuration
from fastapi import APIRouter, Depends, status, Response
from schema import schemas
from database import configuration
from typing import List
from api import blog

router = APIRouter(tags=["Blogs"], prefix="/blogs")
get_db = configuration.get_db


# all actions to be performed from current user, auth purposes
@router.get("/", response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db),  current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.show(id, db)


@router.put("/{id}", status_code=status.HTTP_201_CREATED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.update(id, request, db)


@router.post("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.delete(id, db)
