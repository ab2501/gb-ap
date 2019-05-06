
import json
import datetime


def write_order_to_json(item, quantity, price, buyer, date):
    order = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": str(date)
    }
    root = {"orders": [order]}

    with open('materials/orders.json', encoding='utf-8', mode='w') as fw:
        json.dump(root, fw, indent=4, ensure_ascii=False)


write_order_to_json('Стул', 12, 1000, 'Остап', datetime.datetime.now())
