# Функция подбора второго значения
def kod_2(kod_1):
   result =''
   for i in range (1, int(kod_1 / 2)+1 ):
       for j in range (i+1, kod_1):
           summ = i + j
           if (kod_1 % summ) == 0:
               result+=str(i)+str(j)
   return result

# Основной код    
while 1 > 0:
    first = input("Введите первое число")
    if first.isnumeric():
        if int(first)>=3 and int(first)<=20:
            break
        else :
            print("Ввели недопустимое число")
print(kod_2(int(first)))
