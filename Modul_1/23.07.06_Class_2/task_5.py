# Скласти програму обчислення суми модулів трьох дійсних чисел

num_1 = float(input('Enter first number: '))
num_2 = float(input('Enter second number: '))
num_3 = float(input('Enter third number: '))

module_num_1 = (num_1 ** 2) ** 0.5
module_num_2 = (num_1 ** 2) ** 0.5
module_num_3 = (num_1 ** 2) ** 0.5

sum = module_num_1 + module_num_2 + module_num_3

print(f'Sum module of numbers equal: {sum}')