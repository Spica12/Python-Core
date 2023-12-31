"""
Підсписком (sublist) називають список, що є складовою більшого списку. Підсписок може містити один елемент, множину елементів або бути порожнім.

Наприклад, [1], [2], [3] та [4] є підсписками списку [1, 2, 3, 4]. Список [2, 3] також входить до складу [1, 2, 3, 4], але при цьому список [2, 4] не є підсписком [1, 2, 3, 4], оскільки у вихідному списку числа 2 і 4 не є сусідами.

Порожній список є підсписком будь-якого списку.

Напишіть функцію all_sub_lists, що повертає список, який містить всі можливі підсписки заданого.

Наприклад, якщо функції передано аргумент список [1, 2, 3], то функція має повернути наступний список: [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]].

Функція all_sub_lists повинна повертати щонайменше один список з порожнім підсписком [[]].
"""

def all_sub_lists(data):

    list_data = [[]]
    amount = 0

    for i in range(len(data)):
        amount += 1

        for j in range(len(data)):
            
            if (j+amount) <= len(data):
                sub_list = data[j:(j+amount)]
                list_data.append(sub_list)        

    return list_data

print(all_sub_lists([1, 2, 3]))