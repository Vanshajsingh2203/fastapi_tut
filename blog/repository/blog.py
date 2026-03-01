from sqlalchemy.orm import Session
from blog import models, schemas
from fastapi import status, HTTPException

def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db:Session):
    new_blog = models.Blog(title= request.title ,body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id== id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = 'not found the blog')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def updated(id:int, request: schemas.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    # first is kind of an action , without using it , blog is merely a kind of a lazy evaluation which acts 
    # like a ennvelope not sent to database 
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    blog.update(request.model_dump())
    db.commit()
    return 'updated'

def show(id:int , db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'the blog with id {id} is not found')
        '''response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': f'the blog with id {id} is not found'}'''
    return blog