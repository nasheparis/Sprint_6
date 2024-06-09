import random


def generate_order_info():
    order_info = {
        'first_name': random.choice(['Александр', 'Борис', 'Юрий', 'Лев', 'Николай']),
        'last_name': random.choice(['Смирнов', 'Петров', 'Иванов', 'Сидоров', 'Николаев']),
        'address': random.choice(
            ['улица Ленина, дом 1', 'улица Пушкина, дом 155', 'Молодежная улица, дом 90', 'Зеленая улица, дом 55']),
        'phone_number': random.randint(10000000000, 99999999999)
    }

    return order_info
