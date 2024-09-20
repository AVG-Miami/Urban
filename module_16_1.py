from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome():
    return ("Главная страница")


@app.get('/user/admin')
async def welcome_admin():
    return ("Вы вошли как Администратор")


@app.get('/user/{user_id}')
async def users_id(user_id: str):
    return (f"Вы вошли как пользователь № {user_id}")


@app.get('/user')
async def id_new(username: str = " Andrey ", age: int = 45):
    return (f"Информация о пользователе. Имя {username} Возраст {age}")
