from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_all_message() -> dict:
    return users


@app.get('/message/{message_id}')
async def get_message(message_id: str) -> dict:
    return message_db[message_id]


@app.post('/user/{username}/{age}')
async def create_message(username: str,
                         age: int) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return (f"User {current_index} is registered")


@app.put('/user/{user_id}/{username}/{age}')
async def update_message(user_id: str,
                         username: str,
                         age: int) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return (f"The user {user_id} is registered")


@app.delete('/user/{user_id}')
async def delete_message(user_id: str) -> str:
    users.pop(user_id)
    return (f"Delete message id {user_id}")