# Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать
# скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
# цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
# orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
import json


def write_order_to_json(item, quantity, price, buyer, date):
    order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }

    json_data = json.load(open('files/orders.json', encoding='windows-1251'))
    json_data['orders'].append(order)

    json.dump(json_data, open('files/orders.json', mode='w', encoding='windows-1251'), sort_keys=True, indent=4)


if __name__ == '__main__':
    orders = [
        {
            'item': 'phone',
            'quantity': 1,
            'price': 10000,
            'buyer': 'Ivan',
            'date': '01.01.2000',
        },
        {
            'item': 'printer',
            'quantity': 1,
            'price': 15000,
            'buyer': 'Egor',
            'date': '01.02.2000',
        },
    ]
    for order in orders:
        write_order_to_json(order['item'], order['quantity'], order['price'], order['buyer'], order['date'])
