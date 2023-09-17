"""
Ви проводите розіграш кавоварок Bosch серед зареєстрованих користувачів 
вашої інтернет-сторінки.

Список зареєстрованих користувачів — це словник такого типу:

participants = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}

Ключ словника — це унікальний ідентифікатор бази даних MongoDB, а значення 
&mdash це email користувача. Вам необхідно випадково відібрати декілька 
переможців розіграшу.

Створіть функцію get_random_winners(quantity, participants), яка повертатиме 
список унікальних ідентифікаторів бази даних зі словника participants в 
кількості quantity. Це буде список переможців

Вимоги:

- Отримайте перелік ключів словника. (Після виконання методу keys() 
  використовуйте перетворення типів)
- Перемішайте отриманий список за допомогою методу shuffle
- Виберіть випадкових переможців, використовуючи метод sample.
- Якщо передана кількість переможців більша за кількість користувачів 
  (quantity > len(participants)) — поверніть порожній список.

Наприклад: виклик get_random_winners(2, participants) може повернути 
список з випадковим набором ідентифікаторів як: 

['60577ce4b536f8259cc225d2', '605b89080c318d66862db390'].

------------------------------------------------
import random


def get_random_winners(quantity, participants):
"""

import random


def get_random_winners(quantity, participants):
    winners = list()
    
    if quantity > len(participants):
        return winners
    
    keys_dict = list(participants.keys())
    random.shuffle(keys_dict)
    winners = random.sample(keys_dict, k=quantity)

    return winners


participants = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}


winners = get_random_winners(2, participants)
print(winners)