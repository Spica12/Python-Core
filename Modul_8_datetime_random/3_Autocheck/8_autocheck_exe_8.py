"""
Є список IP адрес:

IP = [
    "85.157.172.253",
    ...
]
Реалізуйте дві функції. Перша get_count_visits_from_ip за допомогою Counter 
повертатиме словник, де ключ це IP, а значення – кількість входжень у вказаний список.

Приклад:

{
    '85.157.172.253': 2,
    ...
}
Друга функція get_frequent_visit_from_ip повертає кортеж з найбільш часто уживаним 
в списку IP і кількістю його появ в списку.

Пример:

('66.50.38.43', 4)
----------------------------------------------------------------------------------
from collections import Counter


def get_count_visits_from_ip(ips):
    


def get_frequent_visit_from_ip(ips):
"""
from collections import Counter


def get_count_visits_from_ip(ips):
    return Counter(ips)
    


def get_frequent_visit_from_ip(ips: list):
    return Counter(ips).most_common(1)[0]