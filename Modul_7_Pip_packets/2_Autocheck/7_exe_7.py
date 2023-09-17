"""
У четвертому модулі розв'язували завдання нормалізації даних. Розширимо її.

При аналізі даних часто виникає необхідність позбавитися екстремальних значень, 
перш ніж почати працювати з даними далі. Напишіть функцію data_preparation, яка 
приймає набір даних, список списків (Приклад: [[1,2,3],[3,4], [5,6]]).

Функція повинна видаляти з переданих списків найбільше і найменше значення, але 
якщо розмір списку понад два елементи. Після видалення даних з кожного списку 
необхідно злити їх разом в один список, відсортувати його за зменшенням та 
повернути отриманий список як результат (Для прикладу вище результат буде 
наступним: [6, 5, 4, 3, 2]).

---------------------------------------------------------

def data_preparation(list_data):

"""

def data_preparation(list_data):
    prepared_data = list()

    for data in list_data:

        if len(data) < 3:
            prepared_data.extend(data)
        else:
            data.remove(min(data))
            data.remove(max(data))

            prepared_data.extend(data)

    prepared_data.sort(reverse=True)

    return prepared_data

    

        





data = [[1,2,3], [3,4], [5,6]]
prepared_data = data_preparation(data)
print(prepared_data)


data = [[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]
prepared_data = data_preparation(data)
print(prepared_data)
