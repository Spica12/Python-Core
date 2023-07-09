# Напишіть програму, яка буде виконувати найпростіші математичні операції 
# з числами послідовно, приймаючи від користувача операнди (числа) та 
# оператор.
# 
# Умови для цієї задачі
# 
# - Додаток працює з цілими та дійсними числами.
# - Додаток вміє виконувати такі математичні операції:
#   - ДОДАВАННЯ (+)
#   - ВІДНІМАННЯ(-)
#   - МНОЖЕННЯ (*)
#   - ДІЛЕННЯ (/)
# 
# Програма приймає один операнд або один оператор за один цикл 
# запит-відповідь.
# 
# Всі операції програма виконує в порядку надходження — одну за одною.
# 
# Програма виводить результат обчислень, коли отримує від користувача 
# символ =.
# 
# Додаток закінчує роботу після того, як виведе результат обчислення.
# 
# Користувач по черзі вводить числа та оператори.
# 
# Якщо користувач вводить оператор двічі поспіль, він отримує 
# повідомлення про помилку і може ввести повторно.

# Якщо користувач вводить число двічі поспіль, він отримує повідомлення 
# про помилку і може ввести повторно.

# Додаток коректно опрацьовує ситуацію некоректного введення (exception).
# --------------------------------------------------------------------
# result = None
# operand = None
# operator = None
# wait_for_number = True
# 
# while True:
# --------------------------------------------------------------------
# result — сюди поміщаємо підсумковий результат 
# operand — завжди зберігає поточне число 
# operator — рядковий параметр, може містити чотири значення,
#            "+", "-", "*", "/" 
# wait_for_number — прапорець, який вказує, що очікують на вводі 
#                   оператор (operator) або операнд (operand).

# Приклад виконання програми:
# >>> 3
# >>> +
# >>> 3
# >>> 2
# 2 is not '+' or '-' or '/' or '*'. Try again
# >>> -
# >>> -
# '-' is not a number. Try again.
# >>> 5
# >>> *
# >>> 3
# >>> =
# Result: 3.0

# Тестові послідовності:
# Перша: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "= "],
# результат 18.0
# Друга: ["2", "3", "-", "1", "+", "10", "*", "2", "="], 
# результат 22.0

result = 0
operand = None
operator = None
wait_for_number = True

while True:

    while wait_for_number:
        try:
            operand = input('Enter number: ')
            operand = float(operand)

            if operator is None or operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
            elif operator == '*':
                result *= operand
            elif operator == '/':
                result /= operand

            break

        except ValueError:
            print(f'{operand} is not a number. Try again.')
    

    while not wait_for_number:
        try:
            operator = input('Enter operator (+, -, *, /, =): ')
            operator = float(operator)
            print(f"{operator} is not a '+' or '-' or '/' or '*'. Try again")
        except ValueError:
            break
    
    if operator == '=':
                print(f'Result: {result}')
                break  

    if wait_for_number:
        wait_for_number = False
    else:
        wait_for_number = True
    
    # print(result, operand, operator, wait_for_number)
        
        

    # if wait_for_number is True:

    #     try:
    #         operand = input('Enter number: ')
    #         operand = float(operand)
    #     except ValueError:
    #         print(f'operand is not a number. Try again.')

    #     if operator == '+':
    #         result += operand
    #     elif operator == '-':
    #         result -= operand
    #     elif operator == '*':
    #         result *= operand
    #     elif operator == '/':
    #         result /= operand
        
    #     wait_for_number = False

    # else:
       
    #     operator = input('Enter operator (+, -, *, /) or = for result: ')
    #     print('operator', operator)
    #     if operator == '=':
            
    #         break

    #     wait_for_number = True

        
    