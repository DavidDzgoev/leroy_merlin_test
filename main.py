import json

with open('input.json') as json_data:
    data = json.load(json_data)

    item_name = data['displayedName']['displayedName']['value'][0]
    shops = ', '.join(k for k, v in data['stock']['stocks']['34'].items() if v != '0')
    max_shop = max(data['stock']['stocks']['34'], key=lambda k: int(data['stock']['stocks']['34'][k]))

    print(f"Название товара - {item_name}")
    print(f"Массив номеров магазинов, в которых есть товары в наличии - {shops}")
    print(f"Найти максимальное количество товара в регионе, вернуть это количество и номер магазина - {max_shop}")
