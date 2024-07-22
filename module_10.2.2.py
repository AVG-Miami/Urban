import multiprocessing
from time import sleep


class WarehouseManager:
    data = {}

    def process_request(self, requests):

        if requests[1] == "receipt":
            if requests[0] in self.data:
                self.data.update( {requests[0]: self.data[requests[0]] + requests[2]} )
                print( "поступил {} в количестве {}  **** состояние склада {}".format( requests[0], requests[2],
                                                                                       self.data ) )
            else:
                self.data.update( {requests[0]: requests[2]} )
                print( "поступил новый {} в количестве {}  **** состояние склада {}".format( requests[0], requests[2],
                                                                                             self.data ) )
        else:
            if requests[0] in self.data:
                self.data.update( {requests[0]: self.data[requests[0]] - requests[2]} )
                print( "отгрузили {} в количестве {}  **** состояние склада {}".format( requests[0], requests[2],
                                                                                        self.data ) )

    def run(self, requests):
        if __name__ == '__main__':
            with multiprocessing.Pool( processes=1 ) as pool:
                pool.map( self.process_request, requests )


# Создаем менеджера склада
manager = WarehouseManager()

# Множество запросов на изменение данных о складских запасах
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50),
    ("product2", "receipt", 50)
]

# Запускаем обработку запросов
manager.run( requests )

# Выводим обновленные данные о складских запасах


print( "состояние склада", manager.data )
