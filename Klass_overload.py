class buiding:
    def __init__(self):
        self.numberOfFloors = 0
        self.buildingType = ''

    def setNumberOfFloors(self, floors):
        self.numberOfFloors = floors

    def setTypeBuilding(self, typeBuild):
        self.buildingType = typeBuild

    def __eq__(self, other):
        if (self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType):
            return "Этажность и тип строения совпадают"
        elif self.numberOfFloors == other.numberOfFloors:
            return "Строения одинаковой этажности"
        elif self.buildingType == other.buildingType:
            return "Строения одинакового типа"
        else: return "Строения разные"

my_build1 = buiding()
floor = (int(input("Какова этажность 1 строения ? ")))
my_build1.setNumberOfFloors(floor)
typeBuild = input("Какой тип 1 строения (жилой, хозяйственный, бытовой, гараж :")
my_build1.setTypeBuilding(typeBuild)


my_build2 = buiding()
floor = (int(input("Какова этажность 2 строения ? ")))
my_build2.setNumberOfFloors(floor)
typeBuild = input("Какой тип 2 строения (жилой, хозяйственный, бытовой, гараж :")
my_build2.setTypeBuilding(typeBuild)

print("Тип строения: ", my_build1.buildingType, " Этажность строения: ", my_build1.numberOfFloors)
print("Тип строения: ", my_build2.buildingType, " Этажность строения: ", my_build2.numberOfFloors)

print (my_build1 == my_build2)

