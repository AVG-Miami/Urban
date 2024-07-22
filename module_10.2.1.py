from threading import Thread
import queue
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = True


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        for i in range( 1, 21 ):
            print( "Посетитель номер {} прибыл".format( i ) )
            customer = Customer( i )
            cafe.serve_customer( customer )
            sleep( 1 )

    def serve_customer(self, customer):
        for table in tables:
            is_busy = True
            if table.is_busy:
                table.is_busy = False
                customer.table = table
                #                print("Для посетителя ", customer.number, " есть свободный столик ", table.number)
                customer.start()
                is_busy = False
                break
        if is_busy:
            print( "Посетитель номер {} ожидает свободный стол".format( customer.number ) )
            self.queue.put( customer )


class Customer( Thread ):
    def __init__(self, number: int = 1, *args, **kwargs):
        super().__init__( *args, *kwargs )
        self.number = number
        self.table = None

    def run(self):
        print( "Посетитель номер {} сел за стол {}. (начало обслуживания)".format( self.number, self.table.number ) )
        sleep( 5 )
        print( "Посетитель номер {} покушал и ушёл. (конец обслуживания)".format( self.number ) )
        self.table.is_busy = True
        # Если очередь не пустая то обслужить следующего в очереди посетителя
        if cafe.queue.qsize():
            cus1 = cafe.queue.get()
            cafe.serve_customer( cus1 )


# Создаем столики в кафе
table1 = Table( 1 )
table2 = Table( 2 )
table3 = Table( 3 )
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe( tables )

# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread( target=cafe.customer_arrival )
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
