class InvalidDataException( Exception ):
    def __init__(self, message, e_info):
        self.message = message
        self.e_info = e_info


class ProcessingException( Exception ):
    def __init__(self, message, e_info):
        self.message = message
        self.e_info = e_info


def tru_value(one, two):
    if isinstance( one, str ) or isinstance( two, str ):
        raise InvalidDataException( "Передаваемые параметры не являются числом", {'one': one, 'two': two} )


def delenie(one, two):
    if two == 0:
        raise ProcessingException( "На ноль делить нельзя", {'one': one, 'two': two} )
    return one / two


def my_func(one, two):
    print ("Даны два значения", one , two)
    try:
        tru_value( one, two )
    except InvalidDataException as e:
        print( "Ошибка ", e.message, e.e_info )
    else:
        print("Введены числа, продолжаем")
        try:
            print( "Результат деления :", delenie( one, two ) )
        except ProcessingException as e:
            print( "Перехват ошибки внутри функции ", e.message, e.e_info )
            raise

print("Деление на 2х чисел с проверкой их значений")
one = 1
two = 2
my_func( one, two )
print()

one = 'w'
two = 2
my_func( one, two )
print()

one = 1
two = 0
try:
    my_func( one, two )
except ProcessingException as e:
    print ("Перехват ошибки из тела программы")
    print( "Ошибка ", e.message, e.e_info )
