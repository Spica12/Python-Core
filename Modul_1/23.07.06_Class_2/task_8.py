# Скласти програму, яка вводить із клавіатури чотиризначне число і 
# виводить на екран середнє арифметичне його цифр.

num = int(input('Enter XXXX number: '))

num_1 = num // 1000
num_2 = (num - num_1 * 1000) // 100
num_3 = (num - num_1 * 1000 - num_2 * 100) // 10
num_4 = (num - num_1 * 1000 - num_2 * 100 - num_3 * 10)

print(num_1, num_2, num_3, num_4)

num_5 = (num // 1000) % 10
num_6 = (num // 100) % 10
num_7 = (num // 10) % 10
num_8 = (num // 1) % 10

# 3456
# 3456 // 1000 --> 3 --> 3 % 10 --> 3
# 3456 // 100 --> 34 --> 34 % 10 --> 4
# 3456 // 10 --> 345 --> 345 % 10 --> 5
# 3456 // 1 --> 3456 --> 3456 % 10 --> 6

print(num_5, num_6, num_7, num_8)