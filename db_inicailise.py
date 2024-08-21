import sqlite3
import random

connnection = sqlite3.connect('db1.db')
cursor = connnection.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS Users(
               id INTEGER PRIMARY KEY,
               username TEXT NOT NULL,
               email TEXT NOT NULL,
               age INTEGER
               )
               ''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
#cursor.execute(" INSERT INTO Users (username, email, age) VALUES (?,?,?)", ("newuser", "exampl@mail.ru", "28"))

# for i in range (30):
#     cursor.execute( " INSERT INTO Users (username, email, age) VALUES (?,?,?)", (f"newuser{i}", f"exampl{i}@mail.ru", random.randint(20, 60)))

#cursor.execute("UPDATE Users SET age = ? WHERE username = ?", (29, "newuser0"))

#cursor.execute("DELETE FROM Users WHERE username= ?", ("newuser0",))

#cursor.execute("DELETE FROM Users")

#cursor.execute("SELECT * FROM Users")

# SELECT FROM WHERE GROUP BY HAVING ORDER BY
#cursor.execute("SELECT username, age FROM Users WHERE age > ?", (29,))
#cursor.execute("SELECT COUNT(*) FROM Users WHERE age > ?", (33,))
cursor.execute("SELECT SUM(age) FROM Users")
total1= cursor.fetchone()[0]
#total2= cursor.fetchall()
cursor.execute("SELECT COUNT(*) FROM Users")
total2= cursor.fetchone()[0]
#print(total2)
cursor.execute("SELECT AVG(age) FROM Users")
avg_age=cursor.fetchone()[0]
cursor.execute("SELECT MIN(age) FROM Users")
min_age=cursor.fetchone()[0]
cursor.execute("SELECT MAX(age) FROM Users")
max_age=cursor.fetchone()[0]
print(total1, total1/total2, avg_age, min_age, max_age)
connnection.commit()
connnection.close()