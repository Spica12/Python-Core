# Є чотирикутна схема польотів дронів з координатами (0, 1, 2, 3).
# У нас є словник points, ключі якого — кортежі, точки польоту 
# між координатами чотирикутника, вигляду (1, 2). Значення 
# словника — це відстані між вказаними точками.

# Приклад:
# points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7, (1, 2): 2.5, 
#           (1, 3): 4.1, (2, 3): 3.9}

# Напишіть функцію calculate_distance, яка на вхід приймає список 
# координат чотирикутника зі словника виду [0, 1, 3, 2, 0]. 
# Функція повинна підрахувати, використовуючи вказаний словник, 
# яку загальну відстань пролетить дрон, рухаючись між точками 
# польоту.

# Примітки:
#  -    Коли беремо у словника points значення, у ключі кортежі 
#       завжди має бути першою координата з меншим значенням — 
        # (2, 3), але не (3, 2);

#  -    Для порожнього списку та списку з однією координатою 
#       функція calculate_distance має повертати 0.

# --------------------------------------------------------
# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9,
# }


# def calculate_distance(coordinates):
# --------------------------------------------------------
points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):

    global points

    if len(coordinates) <= 1:
        return 0
    
    else:

        distance = 0
        start_point = None
        finish_point = None

        for point in coordinates:

            start_point = point
            
            if finish_point is None:
                finish_point = start_point
                continue

            if start_point < finish_point:
                current_key = (start_point, finish_point)
            else:
                current_key = (finish_point,start_point)

            distance += points.get(current_key, 0)

            finish_point = start_point

    return distance


# 2 + 4.1 + 3.9 + 3.9 + 3.9 + 2.5 = 20.3
coordinats = [0, 1, 3, 2, 3, 2, 1]
distance = calculate_distance(coordinats)
print(distance)

coordinats = [0]
distance = calculate_distance(coordinats)
print(distance)

coordinats = []
distance = calculate_distance(coordinats)
print(distance)