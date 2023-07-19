"""
Скласти програму, яка запитує дату (число, місяць, рік) і перевіряє 
коректність введених даних
"""

day = int(input(;Enter days: ))
month = int(input(;Enter months: ))
year = int(input(;Enter years: ))

is_year

if month <= 0 or month > 12:
    print('Month must be from 1 to 12')

if month == 1 or month == 3 or month == 5 or month == 7 \
or month == 8 or month == 10 or month == 12:
    if day <= 1 or day > 31:
        print('Day should be from 1 to 31')
else:
    if day <= 1 or day > 30:
        print('Day should be from 1 to 30')

if month == 2:
    if year % 400 == 0:
        is_year = True
    elif year % 400 == 0:
        is_year = False
    elif year % 4 == 0:
        is_year = True
    else:
        is_year = False

    if is_year:
        if day <= 0 or day > 29:
            print('Day should be from 1 to 29')
    else:
        if day <= 0 or day > 28:
            print('Day should be from 1 to 28')