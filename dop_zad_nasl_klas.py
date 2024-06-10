from colorama import Fore


class Figure():
    sides_count = 0
    __sides = [0]
    __color = [0, 0, 0]
    fields = False
    r = 0
    g = 0
    b = 0

    def __init__(self, color, *sides):
        self.__color = [*color]
        self.__sides = []
        for sid in sides:
            self.__sides += [sid]
        print( 'new figure color =', self.__color, 'sides = ', self.__sides )

    def get_sides(self):
        return self.__sides

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r >= 0 and r <= 255 and g >= 0 and g <= 255 and b >= 0 and b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color( r, g, b ):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *n):
        flag = True
        for i in n:
            try:
                int( i )
            except ValueError:
                flag = False
        if len( n ) != self.sides_count:
            flag = False
        if flag:
            return True
        else:
            return False

    def set_sides(self, *n):
        if self.__is_valid_sides( *n ):
            self.__sides = [*n]

    def __len__(self):
        perimiter = 0
        for i in self.__sides:
            perimiter += i
        return perimiter


class Circle( Figure ):
    sides_count = 1
    __radius = 0

    def __init__(self, color, *sides):
        new_sides = 0
        if len( sides ) != self.sides_count:
            new_sides = [1]
        else:
            new_sides = sides
        super().__init__( color, *new_sides )
        self.__radius = float( *new_sides ) / 6.28

    def get_square(self):
        s = 3.14 * self.__radius * self.__radius
        return s


class Triangle( Figure ):
    sides_count = 3
    __height = 0

    def __init__(self, color, *sides):
        if len( sides ) != self.sides_count:
            new_sides = [1, 1, 1]
        else:
            new_sides = sides
        super().__init__( color, *new_sides )

    def get_square(self):
        s = 0
        return s


class Cube( Figure ):
    sides_count = 12

    def __init__(self, color, *sides):
        if len( sides ) != 1:
            new_sides = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        else:
            new_sides = [*sides, *sides, *sides, *sides, *sides, *sides, *sides, *sides, *sides, *sides, *sides, *sides]
        super().__init__( color, *new_sides )

    def get_volume(self):
        # print (self.get_sides())
        v = self.get_sides()[1] ** 3
        return v


print( Fore.RED + ' Создание элементов' )
print( Fore.BLUE + 'Команда : circle1 = Circle((200, 200, 100), 10)' + Fore.GREEN )
circle1 = Circle( (200, 200, 100), 10 )  # (Цвет, стороны)
print( Fore.BLUE + 'Команда : cube1 = Cube((222, 35, 130), 6)' + Fore.GREEN )
cube1 = Cube( (222, 35, 130), 6 )

# Проверка на изменение цветов:
print( Fore.RED + ' Проверка на изменение цветов:' )
print( Fore.BLUE + 'Команда : circle1.set_color(55, 66, 77)' + Fore.GREEN )
circle1.set_color( 55, 66, 77 )  # Изменится
print( Fore.BLUE + 'Команда : print(circle1.get_color())' + Fore.GREEN )
print( circle1.get_color() )

print( Fore.BLUE + 'Команда : cube1.set_color(300, 70, 15) ' + Fore.GREEN )
cube1.set_color( 300, 70, 15 )  # Не изменится
print( Fore.BLUE + 'Команда : print(cube1.get_color()) ' + Fore.GREEN )
print( cube1.get_color() )

# Проверка на изменение сторон:
print( Fore.RED + ' Проверка на изменение сторон:' )
print( Fore.BLUE + 'Команда : cube1.set_sides(5, 3, 12, 4, 5) # Не изменится' + Fore.GREEN )
cube1.set_sides( 5, 3, 12, 4, 5 )  # Не изменится
print( Fore.BLUE + 'Команда : print(cube1.get_sides()) ' + Fore.GREEN )
print( cube1.get_sides() )
print( Fore.BLUE + 'Команда : circle1.set_sides(15) # Изменится' + Fore.GREEN )
circle1.set_sides( 15 )  # Изменится
print( Fore.BLUE + 'Команда : print(circle1.get_sides()) ' + Fore.GREEN )
print( circle1.get_sides() )

# Проверка периметра (круга), это и есть длина:
print( Fore.RED + ' Проверка периметра (круга), это и есть длина:' )
print( Fore.BLUE + 'Команда : print(len(circle1))' + Fore.GREEN )
print( 'периметра (круга)=', len( circle1 ) )

# Проверка объёма (куба):
print( Fore.RED + ' Проверка объёма (куба):' )
print( Fore.BLUE + 'Команда : print(cube1.get_volume())' + Fore.GREEN )
print( 'Объем =', cube1.get_volume() )

# Проверка площади (круга):
print( Fore.RED + ' Проверка площади (круга):' )
print( Fore.BLUE + 'Команда : print(cube1.get_volume())' + Fore.GREEN )
print( 'Площадь =', circle1.get_square() )
