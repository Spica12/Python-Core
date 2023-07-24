def collector_of_number(operator='+'):

    result = None

    if operator == '+':
        result = 0

    if operator == '*':
        result = 1

    if result is None:
        return 'Operator is not in current function'


    while True:

        user_input = input('Enter value: ')

        if user_input == '=':
            
            break

        if operator == '+':
            result += float(user_input)

        if operator == '*':
            result *= float(user_input) 

    return result
    

res = collector_of_number()
print('1', res)

res = collector_of_number('*')
print('2', res)

res = collector_of_number('-')
print('3', res)