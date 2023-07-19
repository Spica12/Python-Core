""" DESCRIPTION:
Create a function that takes a positive integer and returns the 
next bigger number that can be formed by rearranging its digits. 

For example:
12 ==> 21
513 ==> 531
2017 ==> 2071       # Maybe 7210 

If the digits can't be rearranged to form a bigger number, 
return -1 (or nil in Swift, None in Rust):

9 ==> -1
111 ==> -1
531 ==> -1

"""

def bigger_number(number):

    # Визначаємо кількість цифр в числі
    length = len(str(number))
    # print(f'Length number "{number}" equal {length}')

    # Створюємо тимчасовий список з числа
    temp_number = [int(i) for i in str(number)]
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

    # За умовою, якщо число вже є максимальним, то вивести -1
    if max_number == number:
        return -1
    else:
        return max_number
            
   
# 1 2 8 7 6 4
print(bigger_number(12), 21)
print(bigger_number(513), 531)
print(bigger_number(2017), 7210)
print(bigger_number(9), -1)
print(bigger_number(111), -1)
print(bigger_number(531), -1)
print()
print(bigger_number(128764))
print(bigger_number(34529745))