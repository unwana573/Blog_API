from fastapi import APIRouter, Depends, status, HTTPException
from .. import models, schemas, database, oauth2
from typing import List
from sqlalchemy.orm import Session as SessionLocal  
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)
get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: SessionLocal = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_curent_user)):
    blogs = blog.get_all(db)
    return blogs

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: SessionLocal = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_curent_user)):
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: SessionLocal = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_curent_user)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: SessionLocal = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_curent_user)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: SessionLocal = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_curent_user)):
    return blog.show(id, db)

