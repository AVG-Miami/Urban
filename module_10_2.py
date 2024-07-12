from threading import Thread
import requests
from datetime import datetime
from time import sleep

# Создайте класс Knight с соответствующими описанию свойствами.
class Knight( Thread ):

    def __init__(self, name, power, enemy_count=100):
        self.name1 = name
        self.power = power
        self.enemy_count = enemy_count
        super().__init__()

    def run(self):
        print( "{}, на нас напали!".format( self.name1 ) )
        i = 0
        while self.enemy_count > 0:
            i += 1
            self.enemy_count -= self.power
            print( "{} сражается {} день(дня)..., осталось {} воинов.".format( self.name1, i, self.enemy_count ) )
            sleep( 1 )
        print( "{} одержал победу спустя {} дней(дня)!".format( self.name1, i ) )

# Создайте и запустите 2 потока на основе класса Knight.

first_knight = Knight( 'Sir Lancelot', 10 )
second_knight = Knight( "Sir Galahad", 20 )
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
#Выведите на экран строку об окончании битв.
print( "Все битвы закончились!" )
