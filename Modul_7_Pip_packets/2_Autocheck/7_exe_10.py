"""
При роботі веб-сервісів спілкування, за протоколом HTTP, найчастіше 
відбувається в форматі JSON. І надсилання даних на сервер при запиті POST - 
це необхідність використовувати словник, оскільки структура формату JSON ідентична словнику Python.

Реалізуйте допоміжну функцію, яка формуватиме запит на сервер у вигляді словника. 
Дана функція make_request(keys, values) приймає два параметри у вигляді списків. 
Функція повинна створити словник із ключами з списку keys та значеннями зі списку values.

Порядок відповідності збігається з індексами списків keys та values.
Якщо довжина keys та values не збігаються, поверніть порожній словник.

-----------------------------------
def make_request(keys, values):

"""

def make_request(keys, values):
    dict_request = {}
    
    if len(keys) != len(values):
        return dict_request
    else:
        for indx in range(len(keys)):
            dict_request[keys[indx]] = values[indx]

        return dict_request



keys = ['one', 'two', 'three']
values = ['1', '2', '3']

print(make_request(keys, values))

