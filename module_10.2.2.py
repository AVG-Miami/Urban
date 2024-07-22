import multiprocessing


class WarehouseManager:

    data = {}

    def __init__(self):
#       self.data={}
       print("e")

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

                if self.data[requests[0]]>0:
                    self.data.update( {requests[0]: self.data[requests[0]] - requests[2]} )
                    print( "отгрузили {} в количестве {}  **** состояние склада {}".format( requests[0], requests[2],
                                                                                       self.data ) )

    def run(self, requests):
        with multiprocessing.Pool( processes=4) as pool:
            pool.map(self.process_request, requests )



# Создаем менеджера склада
print(__name__)
if __name__ == '__main__':
    manager = WarehouseManager()
# Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
# Запускаем обработку запросов
    manager.run( requests)
# Выводим обновленные данные о складских запасах
    print( "состояние склада", manager.data )
