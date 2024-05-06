from colorama import init, Fore
# Задание "Раз, два, три, четыре, пять .... Это не всё?"
summ = 0
print( Fore.BLUE )
# Задание "Раз, два, три, четыре, пять .... Это не всё?":
def calculate_structure_sum(structure):
    global summ
#    print (Fore.BLUE, end = '')
#    print (type(structure))
    if isinstance( structure, str ):
        print( Fore.GREEN + "Строка", structure )
        summ += len( structure )

    if isinstance( structure, int ):
        print(Fore.GREEN + "Число", structure )
        summ += structure

    if (isinstance(structure, list) or isinstance(structure,tuple) or isinstance(structure,set)):
            print(Fore.YELLOW + 'Список кортеж или множество', structure)
            for j in structure:
                calculate_structure_sum(j)

    if isinstance(structure, dict):
        print(Fore.RED + "Словарь", structure)
        for j in structure:
            calculate_structure_sum( j )
        for j in structure.values():
            calculate_structure_sum( j )



    return summ



data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print("Входные данные", data_structure)

print( Fore.GREEN )
print("расчетные данные")
result = calculate_structure_sum(data_structure)
print( Fore.RED )
print("Ответ : ", result)
