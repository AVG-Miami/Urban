from colorama import init, Fore

# Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.
# Программа должна вывести на экран текст – вид треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»).
print( Fore.BLUE + "*********************************************************" )
print(
    "Задаие №1 Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам." )
print(
    "Программа должна вывести на экран текст – вид треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»)." )
print( "*********************************************************" )
a, b, c = input( Fore.RED + "Введите 3 положительных числа через пробел: " ).split()
print( Fore.YELLOW )
if (a == b and b == c):
    print( 'Треугольник Равносторонний' )
elif (a == b or a == c or b == c):
    print( 'Треугольник Равнобедренный' )
else:
    print( 'Треугольник Разносторонний' )

# На вход программы подается 3 целых числа. Напишите программу, которая находит серединное значение из этих чисел
print( Fore.BLUE + "*********************************************************" )
print(
    "Задаие №2 На вход программы подается 3 целых числа. Напишите программу, которая находит серединное значение из этих чисел" )
print( "*********************************************************" )
a, b, c = input( Fore.RED + "Введите 3 положительных числа через пробел: " ).split()
print( Fore.YELLOW )
if (a < b and b < c):
    print( "серединное значение из этих чисел: ", b )
elif (b < a and a < c):
    print( "серединное значение из этих чисел: ", a )
else:
    print( "серединное значение из этих чисел: ", c )

# Задание 3 Напишите программу, которая считывает названия двух основных цветов для смешивания. Если пользователь вводит
# что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке.
# В противном случае программа должна вывести название вторичного цвета, который получится в результате.
print( Fore.BLUE + "*********************************************************" )
print(
    "Задание 3 Напишите программу, которая считывает названия двух основных цветов для смешивания. Если пользователь вводит " )
print( "что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке." )
print( "В противном случае программа должна вывести название вторичного цвета, который получится в результате." )
print( "*********************************************************" )
a, b= input( Fore.RED + "Введите название 2х цветов через пробел (красный синий): " ).split()
list_= ["красный", "синий", "желтый"]
print( Fore.YELLOW )
if (a in list_ and b in list_):
    if (a == "красный" and b == "синий") or (b == "красный" and a == "синий"):
        print ("получится фиолетовый")
    elif (a == "красный" and b == "желтый") or (b == "красный" and a == "желтый"):
        print ("получится оранжевый")
    else:
        print( "получится зеленый" )
else:
    print("не корректный ввод названия цвета")
