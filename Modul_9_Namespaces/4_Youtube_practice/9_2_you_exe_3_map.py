#  Перебрати колекцію і до кожного елемента 
# колекції щось добавити або щось з ним зробити

# Генератор одноразовий. Його перебрати можна тільки один раз.



#  How work map as simple explanation
#  Variant 1 -----------------------------
my_list = [1, 2, 3, 4, 5]
result = list()

for i in my_list:
    element = i * 2
    result.append(element)

print(result)   # [2, 4, 6, 8, 10]



#  Variant 2 -----------------------------
my_list = [1, 2, 3, 4, 5]
result = list()

def mult(i):
    return i * 2


for i in my_list:
    element = mult(i)
    result.append(element)

print(result)   # [2, 4, 6, 8, 10]



#  Variant 3 Use MAP -----------------------------

result_map = map(mult, my_list)

# Результатом є генератор
print(result_map)      # <map object at 0x000001C1BAC8B790>

some_list = list(result_map)
print(some_list)    # [2, 4, 6, 8, 10]

# Щоб ще раз перебрати, треба повторно його об'явити
result_map = map(mult, my_list)

for i in result_map:
    print(i)


#  Variant 4 Use MAP -----------------------------
for i in map(lambda i: i * 2, my_list):
    print(i)
