from colorama import init, Fore
# Задание №1. На вход программе подается натуральное число 𝑛. Напишите программу, которая выводит звездный треугольник в
# соответствии с примером.
print( Fore.BLUE + "*********************************************************")
print("Задание №1. На вход программе подается натуральное число 𝑛. Напишите программу, которая выводит звездный ")
print("треугольник в соответствии с примером." )
print( "*********************************************************" )

a = int(input( Fore.RED + "Введите натуральное число: " ))
print( Fore.YELLOW )
for i in range(1, a + 1):
    ii=a-i+1
    for j in range(1, ii + 1):
        print("*", end="")
    print("")

# Задание №2
# Напишите программу, на вход которой даются четыре числа a, b, c и d
# Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [𝑎;𝑏] на все числа отрезка [𝑐;𝑑].
# Числа 𝑎, b, c и 𝑑 являются натуральными и не превосходят 10, 𝑎≤𝑏, 𝑐≤𝑑.
# Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции.
# Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков —
# заголовочные столбец и строка таблицы.

print( Fore.BLUE + "*********************************************************" )
print("Задание №2. Напишите программу, на вход которой даются четыре числа a, b, c и d" )
print("Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [𝑎;𝑏] на все числа отрезка [𝑐;𝑑].")
print("Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции." )
print("Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — " )
print("заголовочные столбец и строка таблицы.")
print( "*********************************************************" )

a, b, c, d = input( Fore.RED + "Введите четыре числа через пробел: ").split()
print( Fore.YELLOW )
for i in range(int(a),int(b)+1):
    if (i==int(a)):
        for j in range(int(c), int(d)+1):
            print('\t', j, end="" )
        print('')
    print(i, end='')
    for j in range(int(c), int(d)+1):
        print('\t', i*j, end="")
    print("")

# Задание №3.
# Дано натуральное число 𝑛. Напишите программу, которая печатает численный треугольник с высотой равной n,
# в соответствии с примером:
print( Fore.BLUE + "*********************************************************" )
print("Задание №3. Дано натуральное число 𝑛. Напишите программу, которая печатает численный треугольник " )
print( "с высотой равной n, в соответствии с примером:" )
print( "*********************************************************" )

a = int( input( Fore.RED + "Введите натуральное число: " ) )
print( Fore.YELLOW )
result=0
for i in range(1,int(a)+1):
    for j in range(1, i+1):
        result +=1
        print('\t', result, end='')
    print()