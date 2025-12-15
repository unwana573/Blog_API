import traceback
from fastapi import Depends, HTTPException, status
from api import models, schemas
from api.hashing import Hash
from sqlalchemy.orm import Session
from api.config import logger

def create_user(request: schemas.User, db: Session):
    # try:
    #     existing_user = db.query(models.User).filter(models.User.email == request.email).first()
    #     if existing_user:
    #         logger.warning(f"Attempt to create a user with existing email: {request.email}")
    #         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
    #                             detail=f'User with email {request.email} already exists')
    # except Exception as e:
    #     logger.error(f"Error checking existing user: {e}")
    try:
        new_user = models.User(
            name=request.name,
            email=request.email,
            password=Hash.hash(request.password).strip()
        )
        db.add(new_user)
        logger.debug(f"New user added to session: {new_user.email}")
        db.commit()
        db.refresh(new_user)
        logger.info(f"New user created: {new_user.email}")
    except Exception as e:
        logger.error("Unhandled error")
        logger.error(traceback.format_exc())
        raise
    return new_user

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    return user