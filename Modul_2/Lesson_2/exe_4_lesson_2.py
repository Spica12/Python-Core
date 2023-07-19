"""
Перевірка чи число є простим (Додатков знайти всі числа в діапазоні 
який веде користувач)
"""

while True:
    is_prime = True
    
    try:
        user_input = int(input('Enter int number: '))

        if user_input < 0:
            break

        # is_prime is True

        for i in range(2, int(user_input**0.5, 1) + 1):
            if user_input % 1 == 0:
                is_prime = False
                break
        else:
            print(is_prime)

    except ValueError:
        print('Not natural number')