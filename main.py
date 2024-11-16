from fastapi import FastAPI
from typing import Optional

app = FastAPI() #create an instance



@app.get('/blog') #  path parameter
def index(limit=10, published:bool = True, sort: Optional[str]=None): # added query parameters
    #only get 10 published blogs

    if published:
        return {'data':f'{limit} published blogs form the db'}
    else:
        return {'data':f'{limit} unpublished blogs form the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int): #id should be int
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments with blog id=id
    return {'data':{'1','2'}}