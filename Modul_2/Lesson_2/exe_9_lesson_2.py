"""
Усі трикутники можуть бути віднесені до того чи іншого класу 
(рівнобедрені, рівнобічні та різнобічні) на підставі довжин їхніх 
сторін. Рівносторонній трикутник характеризується однаковою довжиною 
всіх трьох сторін, рівнобедрений - двох сторін з трьох, а у 
різностороннього трикутника всі сторони різної довжини. Напишіть 
програму, яка запитуватиме у користувача довжини всіх трьох сторін 
трикутника і видаватиме повідомлення про те, до якого типу слід його 
відносити.
"""
from math import sqrt, pow

side_1 = float(input('Enter first side of triangle: '))
side_2 = float(input('Enter second side of triangle: '))
side_3 = float(input('Enter third side of triangle: '))

if side_1 + side_2 > side_3 and\
    side_1 + side_3 > side_2 or\
    side_3 + side_2 > side_1:
      

    if side_1 == side_2 and side_2 == side_3 and side_3 == side_1:
        triangle_type = "equiteral"

    elif side_1 == side_2 and side_2 == side_3 or side_3 == side_1:
            triangle_type = "isoscele"

    elif sqrt(pow(side_1, 2) + pow(side_2, 2)) == side_3 or\
        sqrt(pow(side_2, 2) + pow(side_3, 2)) == side_2 or\
        sqrt(pow(side_3, 2) + pow(side_2, 2)) == side_1:
        triangle_type = "right_angle"

    else:
        triangle_type = "differentel"