result = 0
operand = None
operator = None
wait_for_number = True

while True:

    user_input = input('Wait for input: ')

    if wait_for_number and result is None:
        try:
            result = float(user_input)
            wait_for_number = False
        except ValueError:
            print(f'{user_input} is not a number. Try again.')
    
    elif user_input == '=':
        print(result)
        break

    elif not wait_for_number:
        
        if user_input == '+' or user_input == '-' or\
            user_input == '*' or user_input == '/':

            operator = user_input
            wait_for_number = True
        else:
            print(f"{user_input} is not '+' or.... ")

    elif wait_for_number:
        try:
            operand = float(user_input)
            result = eval(f'{result}{operator}{operand}')

            operand = None
            operator = None
            wait_for_number = False

            wait_for_number = False
        except ZeroDivisionError:
            operand = None
            continue
        except ValueError:
            print(f'{user_input} is not a number. Try again.')
