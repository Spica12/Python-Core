"""
Повернемося до попереднього завдання та виконаємо зворотне. Напишіть 
рекурсивну функцію encode для кодування списку або рядка. Як аргумент 
функція приймає список 
(наприклад ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]) 
або рядок (наприклад, "XXXZZXXYYYZZ"). Функція повинна повернути закодований 
список елементів (наприклад ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).
---------------------------------------------
def encode(data):
"""

def encode(data):

    if data == [] or data == '':
        return []
    else:
        encode_data = [data[0], 0]
        for element in data:

            if data[0] == element:
                encode_data[1] += 1
                
            else:
                encode_data.extend(encode(data[encode_data[1]:]))
                break
        return encode_data

                




    





print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]))

print(encode([]))
print(encode(''))