from colorama import Fore
class  Vehicle():
    vehicle_type = "none"

class Car(Vehicle):
    price = 1000000

    def horse_powers(self):
        horse_power = 100
        return horse_power

class Nissan (Car, Vehicle):
    price = 2000000
    vehicle_type = 'Легковое авто'

my_car = Nissan()
print ('Количество лошидиных сил для автомобиля', Fore.RED, my_car.vehicle_type, Fore.WHITE , ' цена ', Fore.GREEN, my_car.price)
print(my_car.horse_powers())