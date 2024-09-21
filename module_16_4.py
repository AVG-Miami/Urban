from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List
from typing import Annotated

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/users')
async def get_all_users() -> List[User]:
    return users


@app.get('/user/{user_id}')
async def get_user(user_id: int) -> User:
    for user in users:
        if user['id'] == int(user_id):
            return user
    raise HTTPException(status_code=404, detail="User not found")


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
