def  is_prime(number: int) -> bool:

    if number <= 1:
        return False
    
    for i in range(2, number):

        if number % i == 0:
            return False
    
    return True


def main():

    user_input = int(input('Enter natural value: '))

    if is_prime(user_input):
        print(f'{user_input} -- is prime number.')
    else:
        print(f'{user_input} -- is not prime number.')

if __name__ == '__main__':
    main()