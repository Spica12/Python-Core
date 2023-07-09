# Скласти програму обчислення відстані між точками з координатами, 
# що вводяться користувачем.
# 
# Distance - sqrt((x2-x1)^2 + (y2-y1)^2)

point_1_X = int(input('Enter coordinate X point 1: '))
point_1_Y = int(input('Enter coordinate Y point 1: '))

point_2_X = int(input('Enter coordinate X point 2: '))
point_2_Y = int(input('Enter coordinate Y point 2: '))

distance = ((point_2_X - point_1_X) **2 + \
            (point_2_Y - point_1_Y) ** 2) ** 0.5

print(f'Distance between point 1 [{point_1_X}, {point_1_Y}] and \
        point 2 [{point_2_X}, {point_2_Y}] equal {distance}')