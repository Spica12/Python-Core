# При аналізі даних часто виникає необхідність позбавитися 
# екстремальних значень, перш ніж почати працювати з даними 
# далі. Напишіть функцію prepare_data, яка видаляє з переданого 
# списку найбільше та найменше значення, сортує його в порядку 
# зростання і повертає змінений список як результат.
# ---------------------------------------
# def prepare_data(data):
# ---------------------------------------

def prepare_data(data):

    max_data = float('-inf')
    min_data = float('inf')

    for number in data:

        if number > max_data:
            max_data = number

        if number < min_data:
            min_data = number

    data.remove(max_data)
    data.remove(min_data)

    data.sort()

    return data

list_of_data = prepare_data([1, 4, 6, 8, 4, 5, 8, 9, 0, 10, 349])

print(list_of_data)
