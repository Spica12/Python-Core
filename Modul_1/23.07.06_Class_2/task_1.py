# Скласти програму розв'язання лінійного рівняння а*х + b = 0 (а≠0). 
# (a і b вводяться користувачем)

value_a = int(input('Enter value a: '))
value_b = int(input('Enter value b: '))

value_x = - value_b / value_a

print(f'Result equal: {value_x}')