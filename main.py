
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# FastAPI app instance
app = FastAPI()

# In-memory database for blog posts
fake_db = {}

# Blog Post schema
class BlogPost(BaseModel):
    title: str
    content: str
    author: Optional[str] = None

# Create a blog post (C in CRUD)
@app.post("/posts/", status_code=201)
async def create_post(post: BlogPost):
    post_id = len(fake_db) + 1
    fake_db[post_id] = post
    return {"id": post_id, **post.dict()}

# Get all blog posts (R in CRUD)
@app.get("/posts/", response_model=List[BlogPost])
async def get_posts():
    return list(fake_db.values())

# Get a single blog post (R in CRUD)
@app.get("/posts/{post_id}", response_model=BlogPost)
async def get_post(post_id: int):
    if post_id not in fake_db:
        raise HTTPException(status_code=404, detail="Post not found")
    return fake_db[post_id]

# Update a blog post (U in CRUD)
@app.put("/posts/{post_id}", response_model=BlogPost)
async def update_post(post_id: int, post: BlogPost):
    if post_id not in fake_db:
        raise HTTPException(status_code=404, detail="Post not found")
    fake_db[post_id] = post
    return fake_db[post_id]

# Delete a blog post (D in CRUD)
@app.delete("/posts/{post_id}", status_code=204)
async def delete_post(post_id: int):
    if post_id not in fake_db:
        raise HTTPException(status_code=404, detail="Post not found")
    del fake_db[post_id]
    return {"message": "Post deleted successfully"}

# To run the app use the following command:
# uvicorn main:app --reload
