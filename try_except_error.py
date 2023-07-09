# Оператори try...except
# try
# except
# else
# finally


# print('------------Приклад 1------------------------')
# a = 'a'

# try:
#     val = int(a)
# except ValueError:
#     print(f'val {a} is not a number')
# else:
#     print(val > 0)
# finally:
#     print('This will be printed anyway')

# print('------------Приклад 2------------------------')
# age = input('How old are you?')

# try:
#     age = int(age)
#     if age >= 18:
#         print('You are adult.')
#     else:
#         print('You are infant')
# except ValueError:
#     print(f'{age} is not a number')

# # Основні типи виключень

# SyntaxError - синтаксична помилка

# IndentationError - у виділенні блоків інструкцій пробілами помилка

# TabError - в одному файлі використовується пробіли та табуляція

# TypeError - операція зі змінною неможлива
# 2 / 'a'

# ValueError - операнд відповідний, але операція з ним неможлива
# int('a')

# ZeroDivisionError - ділення на нуль.

# print('------------Example 3------------------------')
# while True:

#     user_input = input('Enter number: ')

#     try:
#         x = int(user_input)
#     except ValueError:
#         print('Should be a number. Please try again!')
#         continue
    
#     break
# print(user_input)
# # skkdf --> Should be a number. Please try again!
# # 234 --> 234

# print('------------Example 4------------------------')

# # Use comand  -- as --

# while True:

#     user_input = input('Enter number: ')

#     try:
#         x = int(user_input)
#     except ValueError as error:
#         print(error)
#         print('Should be a number. Please try again!')
#         continue
    
#     break
# print(user_input)
# # Enter number: ssd
# # invalid literal for int() with base 10: 'ssd'
# # Should be a number. Please try again!

# print('------------ Example 5 ------------')
# while True:

#     user_input = input('Enter number: ')

#     try:
#         x = int(user_input)
#     except (ValueError, TypeError):
#         print(error)
#         print('Should be a number. Please try again!')
#         continue
    
#     break
# print(user_input)

# print('------------ Example 6 ------------')
# while True:

#     user_input = input('Enter number: ')

#     try:
#         x = int(user_input)
#     except ValueError:
#         print(error)
#         print('Should be a number. Please try again!')
#         continue
#     except TypeError:
#         print('TypeError')
#         continue

#     break
# print(user_input)

# print('------------ Example 7 ------------')

# # Exception

# while True:

#     user_input = input('Enter number: ')

#     try:
#         x = int(user_input)
#     except ValueError:
#         print(error)
#         print('Should be a number. Please try again!')
#         continue
#     except Exception:
#         print('TypeError')
#         continue

#     break
# print(user_input)

# print('------------ Example 8 ------------')
# try:
#     num = int(input('Enter team size: '))
#     award = 10000
#     bonus_for_person = award / num
# except ValueError:
#     print('You have entered not number!')
# except ZeroDivisionError:
#     print('You have entered 0 members.')
# else:
#     print(f'Bonus for per person is {bonus_for_person} gold!')
# finally:
#     print('See you later!')

print('------------ Example 9 ------------')
while True:
    age = input('How old are you? ')

    try:    
        age = int(age)
        if age >= 18:
            print('Access allowed.')
            break
        else:
            print('Access denied.')
            break
    except ValueError:
        print(f'{age} is not a number. Please write number!')
    finally:
        print ('-'*30)