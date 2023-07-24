from random import randint


def predict_number(number):

    count = 0

    goal = randint(0, number)

    while True:

        user_input = int(input(f'Enter natural number from 0 to {number}: '))
        count += 1

        if user_input > goal:
            print('Smaller')
        elif user_input < goal:
            print('Larger')
        else:
            print(f'You win! Number of attempts {count}')
            break

predict_number(10)

