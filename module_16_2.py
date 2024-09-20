from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/')
async def welcome():
    return ("Главная страница")


@app.get('/user/admin')
async def welcome_admin():
    return ("Вы вошли как Администратор")


@app.get('/user/{user_id}')
async def users_id(user_id: int = Path(ge=1, le=100, description="Enter User ID", example='1')):
    return (f"Вы вошли как пользователь № {user_id}")


@app.get('/user/{username}/{age}')
async def id_new(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    return (f"Информация о пользователе. Имя {username} Возраст {age}")
