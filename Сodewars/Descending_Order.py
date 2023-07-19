"""
Your task is to make a function that can take any non-negative 
integer as an argument and return it with its digits in 
descending order. Essentially, rearrange the digits to create 
the highest possible number.

Examples:
Input: 42145 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321
"""
# def descending_order(num):
#     # Bust a move right here

def descending_order(num):
    # Визначаємо кількість цифр в числі
    length = len(str(num))
    # print(f'Length number "{num}" equal {length}')

    # Створюємо тимчасовий список з числа
    temp_number = [int(i) for i in str(num)]
    # print(f'Current temp number equal {temp_number}')

    # Перший цикл for виконує цикл в кількості рівним кількості
    # цифр в числі
    for _ in range(length-1):


        # Другий цикл for виконує цикл в кількості i-1 для числа
        # Наприклад, 14567 --> 67 56 45 14 
        for i in range(length-2, -1, -1):
            # print(i)

            # Умова перевіряє чи більше остання цифра,
            # якщо так, то зберігається замість меншою цифри, 
            # а менша цифра зберігається як остання
            if temp_number[i + 1] > temp_number[i]:
                # print(temp_number[i + 1], '>', temp_number[i])
                temp_number[i], temp_number[i + 1] = temp_number[i + 1], temp_number[i]

    #  Перетворення списку з цифрами в нове максимальне число
    max_number = ''
    for i in temp_number:
        max_number += str(i)
    
    max_number = int(max_number)
    # print(f'Current afte max number equal {max_number}') 

    return max_number
        



print(descending_order(42145), 54421)
print(descending_order(145263), 654321)
print(descending_order(123456789), 987654321)