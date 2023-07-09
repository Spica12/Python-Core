# У тризначному числі х закреслили його другу цифру. Коли до двозначного 
# числа, що утворилося, ліворуч приписали другу цифру числа х, то вийшло 
# число y. Скласти програму знаходження числа y.

num = int(input('Enter XXX number: '))

num_1 = (num // 100) % 10
num_2 = (num // 10) % 10
num_3 = (num // 1) % 10

new_num = int(str(num_2) + str(num_1) + str(num_3))

print(num_1, num_2, num_3)
print(f'New number equal: {new_num}')