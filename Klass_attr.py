class buiding:
    total = 0
    def __init__(self, name):
        self.name = name
        buiding.total += 1


print(buiding.total)
for i in range(40):
    my_house = buiding("Здание_" + str(i))
    print("Построено ", my_house.name, " общее количество зданий ", my_house.total)
