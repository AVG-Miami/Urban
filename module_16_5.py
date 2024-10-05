from fastapi import FastAPI, status, Body, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = [{'id': 1, 'username': 'UrbanUser', 'age': 24}, {'id': 2, 'username': 'UrbanTest', 'age': 36},
         {'id': 3, 'username': 'admin', 'age': 42}]


class User(BaseModel):
    id: int = None
    username: str
    age: int


# @app.get('/users')
# async def get_all_users() -> List[User]:
#     return users


@app.get('/')
async def get_all(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "messages": users})


@app.get('/users/{user_id}')
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id - 1]})
    except:
        raise HTTPException(status_code=404, detail="User not found")


# @app.get('/user/{user_id}')
# async def get_user(user_id: int) -> User:
#     for user in users:
#         if user['id'] == int(user_id):
#             return user
#     raise HTTPException(status_code=404, detail="User not found")


@app.post('/user/{username}/{age}')
async def create_user(user: User, username: str, age: int) -> User:
    new_user = {"id": int(len(users) + 1), "username": username, "age": int(age)}
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int,
                      username: str,
                      age: int) -> User:
    for user in users:
        if user['id'] == user_id:
            user.update({'username': username, 'age': age})
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User not found")
