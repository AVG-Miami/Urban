from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Confirm, IntPrompt
from rich.columns import Columns

console = Console ()

list_items =[]
amount = []

def add_cass():
    global list_items, amount
    items = input('Что хотите добавить в корзину? ')
    price = input('Задайте цену товара ')
    print()
    print('Вы добавили в корзину ', items, ', ','по цене ', price, " руб!")
    list_items.append(items)
    amount.append(price)

def chec_card(items, price):
    global list_items
    global amount
    items_panel = Panel(
        Text('\n'.join([f'{item}' for item in items] )),
        title = "Твои продукты",
        width = 34
    )
    amount_panel = Panel(
        Text('\n'.join([f'{amount}' for amount in price] )),
        title = "Цена продуктов",
        width = 34
    )

    dvb_panel = Columns([items_panel, amount_panel])
    console.print(dvb_panel)

def clear_card():
    global list_items
    global amount
    list_items.clear()
    amount.clear()

def create_chec(items, price):
    total_price = sum([int(i) for i in price])
    len_items = len(items)
    name_saller = "Andrey Gorbunov"
    street_shop = "Karla Marksa, 1"
    console.print(Panel(
        Text(
        f'''
        Большое спасибо за покупку! 
            Будем ждать Вас еще!
        ___________________________
        Количество товаров: {len_items}
        Общая стоимость: {total_price}
        Кассир: {name_saller}
        Адрес магазина: {street_shop}


        ''',
        ),
        title = "чек",
        width = 50
     ))

def run():
    console.print(Panel(Text(
        '''
    Выберите одну из операций:
    1. Добавить товар
    2. Что в корзине?
    3. Очистить корзину
    4. Создать чек
    5. Завершить работу'''),
        title ="Kassa.py",
        width = 34
    ))

    while True:
        oper = console.input('что хочешь сделать (1-5) ')
        if oper == '1':
            add_cass()
        elif oper == '2':
            chec_card(list_items, amount)
        elif oper == '3':
            clear_card()
        elif oper == '4':
            create_chec(list_items, amount)
        elif oper == '5':
            if Confirm.ask  ('Вы действительно хотите выйти ? '):
                break
        else:
            console.print('Что то не так, выберите действие (1-5) ')

run()




