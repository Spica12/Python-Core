number = None
number_sum = 0
while True:
    user_input = input('Input integer (or = for exist): ')
    if user_input == '=':
        print(number_sum)
        break
    try:
        number = int(input('Input integer: '))
    except ValueError as e:
        print(e)
        continue
    number_sum += number