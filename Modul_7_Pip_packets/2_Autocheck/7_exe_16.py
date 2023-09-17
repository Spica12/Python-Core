"""
Розберемо просту техніку кодування та декодування на основі серій. 
Наприклад, у нас є список із повторюваними спостереженнями якоїсь величини, 
вона може приймати значення X, Y або Z. Значення з'являються у довільному порядку 
та зберігаємо ми їх у списку 
["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"] або рядку "XXXZZXXYYYZZ".

Внаслідок чого ми можемо зменшити обсяг інформації, що зберігається? 
Стиснення можна досягти заміною групи повторюваних значень на одноразове 
значення та лічильник повторів: ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]

Напишіть рекурсивну функцію decode для декодування списку, закодованого 
цим способом. Як аргумент функція приймає закодований список. Функція 
має повернути розшифрований список елементів.
----------------------------------------------------------------------------
def decode(data):
"""

def decode(data):
    decode_data = []
    if data == []:

        return decode_data
        
    else:
        value = data.pop(0)
        times = data.pop(0)

        for _ in range(times):
            decode_data.append(value)

        decode_data.extend(decode(data))

        return decode_data




    # for indx in range(0, len(data), 2):
    #     value = data[indx]
    #     amount_value = data[indx+1]
        
    #     for amount in range(amount_value):
    #         decode_data.append(value)

    return decode_data


encode_data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]

print(decode(encode_data))