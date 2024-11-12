from fastapi import FastAPI


app = FastAPI() #create an instance


@app.get('/') # base path
def index():
    return {'data':'blog list'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int): #id should be int
    return {'data':id}


@app.get('/blog/{id}/comments')
def show(id):

    # fetch comments with blog id=id
    return {'data':{'1','2'}}