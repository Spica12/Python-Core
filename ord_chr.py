# Функція ord() - вона перетворює символ на число, яке є позицією в 
# таблиці ASCII.
# 
# ord("a")  # 97

letter = 'b'
ord_letter = ord(letter)
print(letter, ord_letter)
# a 97
# b 98

chr_letter = chr(ord_letter + 3)
print(ord_letter, chr_letter)
