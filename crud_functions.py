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

    cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?,?,?)", ("Продукт_1", "Описание_1", 100))
    cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?,?,?)", ("Продукт_2", "Описание_2", 200))
    cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?,?,?)", ("Продукт_3", "Описание_3", 300))
    cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?,?,?)", ("Продукт_4", "Описание_4", 400))
    connnection.commit()
    connnection.close()

def get_all_products():
    connnection = sqlite3.connect('db_product.db')
    cursor = connnection.cursor()
    cursor.execute("SELECT title, description, price FROM Products")
    return cursor.fetchall()
    connnection.commit()
    connnection.close()

initiate_db()