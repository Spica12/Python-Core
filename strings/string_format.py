# Порядкове
print('{} {} {} {}'.format('a', 'b', 'c', 'd')) # a b c d

# Нумероване
print('{0} {1} {2} {3} {0}'.format('a', 'b', 'c', 'd')) # a b c d a

# Іменовані поля
print('{name} {last_name}'.format(last_name='John', name='Erusciante')) # Erusciante John


print('------------------')#                int, hex, oct, bin

for i in range(16):
    # s = 'int: {0:d}; hex: {0:#x}; oct: {0:#o}; bin: {0:#b}'.format(i)
    s = f'int: {i:d}; hex: {i:#x}; oct: {i:#o}; bin: {i:#b}'
    print(s)

a = 10
print(f'{int(a)} {hex(a)} {oct(a)} {bin(a)}') # 10 0xa 0o12 0b1010


print('------------------')#                metalanguage
width = 5
for num in range(21):
    print('{:^10} {:^10} {:^10}'.format(num, num**2, num**3))



print('------------------')#                modificators
# Ім'я поля
s = '{name} {last_name}'.format(last_name='Dilan', name='Bob')
print(s)    # Bob Dilan



print('------------------')#                modificators
# Перетворення, необов'язковий, вказується після !
# !r - показати елемент як є
# !s - спробувати перетворити елемент 
s = '{name!r} {last_name!s}'.format(last_name='Dilan', name='Bob')
print(s)    # 'Bob' Dilan

print('------------------')#                Specification
# Специфікація вказується після : 
# Відповідає за те як відобарзити елемент

# Змінити розрядність представлення цілих чисел
# :d - десяткові
print('dec: {:d}'.format(15))   # dec: 15

# :o - вісімкові
print('oct: {:o}'.format(15))   # oct: 17

# :x - шістнадцяткові
print('hex: {:x}'.format(15))   # hex: а

# :b - двійкові
print('bin: {:b}'.format(15))   # bin: 1111

# Змінити точність представлення дробових чисел
# Округлюється до вказаної кількості знаків.
print('pi: {:0.3}'.format(3.1415))   # pi: 3.14

# Як відобарзити знак чисел
print('"{}" "{:+}" "{:-}" "{: }"'.format(1, 2, -3, 4))   
# "1" "+2" "-3" " 4"

# Вирівняти положення елементу і чим (якими символами) доповнити
left, center, rirght = 10, 20, 10
print('|{:<10}|{:^12}|{:>10}|'\
      .format('1234567890', '1234567890', '1234567890'))     
    # |left      |**center**|     right|

print('|{:<10}|{:^12}|{:>10}|'\
      .format('123456789', '123456789', '123456789'))      
    # |left      |**center**|     right|

text = '1234567890'
row = ''
for i in range(len(text)):
    row += text[i]
    print('|{:-<10}|{:*^12}|{:>10}|'.format(row, row, row)) 
print()
text = '1234567890'
row = ''
for i in range(len(text)):
    row += text[i]
    print(f'|{row:-<10}|{row:*^12}|{row:>10}|') 


print('------------------')
print('{0:*^10}'.format('asd')) #  ***asd****
word = 'asd'
num  = 20
print(f'{word:*^{num}}') #  ********asd*********
