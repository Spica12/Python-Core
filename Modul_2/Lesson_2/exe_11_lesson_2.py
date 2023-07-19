# Користувач вводить строку, перевірити чи дана 
# строка є паліндромом

line = input('Enter string: ')
print(line)
print(line[::-1])

if line == line[::-1]:
    print('Is palindrome')
else:
    print('Not palindrome')