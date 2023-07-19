# Скласти програму перевірки, чи є задане тризначне число 
# паліндромом.

number = int(input('Enter 3 digit number: '))

num_1 = number // 100
num_3 = number % 10

if num_1 == num_3:
    print('Is polindrome')
else:
    print("Isn't polindrome")