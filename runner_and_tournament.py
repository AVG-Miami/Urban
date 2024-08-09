class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance( other, str ):
            return self.name == other
        elif isinstance( other, Runner ):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list( participants )

    def start(self):
        #        print("Новый забег")
        #  Если передаваемы список бегунов будет содержать бегуна с меньшей скоростью в начале списка
        # то возможны дистанции например 61м  при которой 1м придет бегун с меньшей скоростью
        new_partipans = []
        speed_participan = {}
        # Формируем словарь с элементами {Имя_бегуна:его скорость}
        for participant in self.participants:
            speed_participan.update( {participant.name: participant.speed} )
        #        print(self.participants)
        #        print(speed_participan)
        # Сортируем словарь по скорости
        sort_speed_participan = dict( sorted( speed_participan.items(), key=lambda item: item[1], reverse=True ) )
        #        print(sort_speed_participan)
        # Создаем новый список бегунов на основе сортированного списка по скорости
        # (список должен содержать спортсменов в порядке убывания скорости)
        for i in range( len( sort_speed_participan ) ):
            for participant in self.participants:
                if participant.name == list( sort_speed_participan.keys() )[i]:
                    new_partipans.append( participant )
        #        print(new_partipans)
        # Заменяем исходный список бегунов на сортированный по скорости
        self.participants = new_partipans

        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                #                print("Бегун ",  participant,' пробежал ', participant.distance)
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove( participant )
        return finishers
