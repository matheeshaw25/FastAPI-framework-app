from fastapi import FastAPI


app = FastAPI() #create an instance


@app.get('/')
def index():
    return 'heyy'