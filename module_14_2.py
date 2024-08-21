'''
Домашнее задание по теме "Выбор элементов и функции в SQL запросах
'''
import sqlite3
import random
from pprint import pprint

connnection = sqlite3.connect( 'not_telegram.db ' )
cursor = connnection.cursor()
cursor.execute( '''
               CREATE TABLE IF NOT EXISTS Users(
               id INTEGER PRIMARY KEY,
               username TEXT NOT NULL,
               email TEXT NOT NULL,
               age INTEGER,
               balance INTEGER NOT NULL 
               )
               ''' )
# Удаляем все записи
cursor.execute( "DELETE FROM Users" )

# Заполните её 10 записями:
for i in range( 1, 11 ):
    cursor.execute( " INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
                    (f"User{i}", f"example{i}@gmail.com", 10 * i, 1000) )

# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
cursor.execute( "UPDATE Users SET balance = ? WHERE ID%2", (500,) )

# Удалите каждую 3ую запись в таблице начиная с 1ой:
cursor.execute( "DELETE FROM Users WHERE NOT (ID-1)%3" )

# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
cursor.execute( "SELECT username, email, age, balance FROM Users WHERE age<>60" )
users = cursor.fetchall()
for user in users:
    print( user[0], "|", user[1], "|", user[2], "|", user[3] )

# Удаление пользователя с id=6
cursor.execute("DELETE FROM Users WHERE id = 6")

# Подсчёт кол-ва всех пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users=cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances=cursor.fetchone()[0]
print(all_balances / total_users)


connnection.commit()
connnection.close()
