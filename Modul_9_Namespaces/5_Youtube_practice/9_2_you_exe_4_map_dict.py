#  Перебрати колекцію і до кожного елемента 
# колекції щось добавити або щось з ним зробити

# Генератор одноразовий. Його перебрати можна тільки один раз.


#  Variant 4 Use MAP -----------------------------

my_dict = {
    'a': 1,
    'b': 2
}



for i in map(lambda i: i * 2, my_dict):
    print(i)

# aa
# bb



for i in map(lambda i: i * 2, my_dict.items()):
    print(i)

# ('a', 1, 'a', 1)
# ('b', 2, 'b', 2)



for key, value in map(lambda i: (i[0], i[1]), my_dict.items()):
    print(key)
    print(value)

# a
# 1
# b
# 2