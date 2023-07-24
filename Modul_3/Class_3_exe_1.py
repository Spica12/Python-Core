# def fnc(x):

#     if x == 3:
#         return 3
#     else:
#         return fnc(x-1) + x
    
# print(fnc(5))


# Exersice 1
# Функція приймає рядок, а повертає словник, де ключ це 
# символ рядка, а значення код ASCII

def codef_of_string(string: str) -> dict:

    codes = dict()

    for char in string:
        if char not in codes:
            codes[char] = ord(char)
    
    return codes

print(codef_of_string('Hello world'))