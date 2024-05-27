from random import randint, choice


class Buiding:
    total = 0
    build_name = ['Дом', 'Сарай', 'Ратуша', 'Высотка', 'Церковь', 'Стадион', 'Бассейн', 'Университет']

    def __init__(self):
        self.name = choice( Buiding.build_name )
        Buiding.total += 1

    def __str__(self):
        return 'Строение ' + self.name + ' всего зданий ' + str( self.total )


for i in range( 40 ):
    my_house = Buiding()
    print( my_house )
