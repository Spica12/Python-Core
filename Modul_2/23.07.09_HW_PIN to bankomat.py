print('-'*10, 'Example 1', '-'*10)

initial_pin = '012344'
MAX_TRIES = 3

while MAX_TRIES:

    print(f'You have {MAX_TRIES} tries')

    user_pin = input('Enter your pin: ')

    if len(user_pin) == 4 or len(user_pin) == 6:

        if initial_pin == user_pin:

            amount = input('How much money you want?: ')

            if amount > 0:
                
                print(f'Take your {amount}!')
                break

        else:
            print('Sorry, wrong pin. Try again please!')
            

    else: 
        print(f'Pin should be 4 or 6 digits. ')
        
    
    MAX_TRIES -= 1
    print()
    

print('-'*29)