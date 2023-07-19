"""
Перевірити чи всі значення першої строки знаходяться в другій строці
Input: s = "abc", t = "ahbgdc" Output: true
Input: s = "axc", t = "ahbgdc" Output: false
"""

string_one = input('Enter string: ')
string_two = input('Enter string to compare: ')

for char in string_one:
    if char not in string_two:
        print(False)
        break
else:
    print(True)