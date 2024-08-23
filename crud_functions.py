import sqlite3
import random


def initiate_db():
    connnection = sqlite3.connect('db_product.db')
    cursor = connnection.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Products(
                   id INTEGER PRIMARY KEY,
                   title TEXT NOT NULL,
                   description TEXT,
                   price INTEGER NOT NULL
                   )
                   ''')
    cursor.execute('''
                       CREATE TABLE IF NOT EXISTS Users(
                       id INTEGER PRIMARY KEY,
                       username TEXT NOT NULL,
                       email TEXT NOT NULL,
                       age INTEGER NOT NULL,
                       balance INTEGER NOT NULL
                       )
                       ''')

    cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?,?,?)", ("Продукт_1", "Описание_1", 100))
    cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?,?,?)", ("Продукт_2", "Описание_2", 200))
    cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?,?,?)", ("Продукт_3", "Описание_3", 300))
    cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?,?,?)", ("Продукт_4", "Описание_4", 400))
    connnection.commit()
    connnection.close()


def is_included(username):
    connnection = sqlite3.connect('db_product.db')
    cursor = connnection.cursor()
    sql = "SELECT * FROM Users WHERE username = ?"
    print()
    print("in function ", sql, username)
    print()
    cursor.execute(sql, (username,))

    user = cursor.fetchone()
    connnection.commit()
    print()
    print("Пользователь", user)
    print()
    if user == None:
        return False
    else:
        return True
    #    connnection.commit()
    connnection.close()


def add_user(username, email, age):
    print('222222')
    connnection = sqlite3.connect('db_product.db')
    cursor = connnection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age,balance) VALUES (?,?,?,?)", (username, email, age, 1000))
    connnection.commit()
    connnection.close()


def get_all_products():
    connnection = sqlite3.connect('db_product.db')
    cursor = connnection.cursor()
    cursor.execute("SELECT title, description, price FROM Products")
    return cursor.fetchall()
    connnection.commit()
    connnection.close()


def get_all_users():
    connnection = sqlite3.connect('db_product.db')
    cursor = connnection.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()
    connnection.commit()
    connnection.close()

# initiate_db()
# is_included("a")
