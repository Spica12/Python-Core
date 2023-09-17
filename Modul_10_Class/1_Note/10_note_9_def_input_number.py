
def input_number():

    while True:

        try:
            num = input('Enter integer number: ')
            return int(num)
        except:
            print(f'"{num}" is not a number. Try again')


num = input_number()
print(num)