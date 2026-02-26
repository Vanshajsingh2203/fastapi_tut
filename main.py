from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def abc():
    return {'data' : 'This is just a function to test'}

@app.get('/blog/{id}')
def dynamic_handling(id):
    return {'purpose': f'to show the dynamic handling with number {id}'}

## to show the post method using BaseModel 
class Blog(BaseModel):
    id: int
    title: str
    comment : Optional[str]

@app.post('/postmethod')
def use_post_method(request: Blog):
    return {'data': f'the title is {request.title}'}