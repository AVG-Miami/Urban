# входные данные
grades = ['5 3 3 5 4', '2 2 2 3', '4 5 5 2', '4 4 3', '5 5 5 4 5']
students = {'Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron'}
print(grades)
print(students)
print()
# преобразуем множество в список и сортируем его по алфавиту
stud = []
for i in students:
    stud.append(i)
stud = sorted (stud)

midle_ball={}
index_2=0

# обрабатываем каждый элемент из списка stud
for i in stud:
     summ=0
# Удаляем пробелы, оставляя лишь цифры в списке оценок
     grades[index_2]=grades[index_2].replace(' ', '')
# Посимвольно читаем строку преобразуем в цифру и суммируем
     for j in range(0, len(grades[index_2])):
         summ+=int(grades[index_2][j])
# вычисляем средний бал и добавляем его в словарь   
     midle_ball[i]=summ/len(grades[index_2])
     index_2+=1

print(midle_ball)
