# Як ми знаємо, ключ у словнику має бути унікальним, тоді як 
# значення його ні. Реалізуйте функцію lookup_key для пошуку 
# всіх ключів за значенням у словнику. Першим параметром у 
# функцію ми передаємо словник, а другим — значення, що хочемо 
# знайти. Таким чином, результат може бути як список ключів, 
# так і порожній список, якщо ми нічого не знайдемо.
#  ---------------------------------
# def lookup_key(data, value):
#  ---------------------------------


def lookup_key(data, value):

    result = []

    for key, val in data.items():

        if val == value:
            result.append(key)
        
    return result

some_dict = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 2}

print(lookup_key(some_dict, 1))
print(lookup_key(some_dict, 2))
print(lookup_key(some_dict, 3))