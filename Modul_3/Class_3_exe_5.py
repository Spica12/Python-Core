def max_value_of_function(x_start, x_end, step=0.5):

    a = 2.14
    b = -4.21
    c = 3.25

    max_value = float('-inf')

    x = x_start

    while x <= x_end:

        y = a * pow(x, 3) + b * x - c

        if y > max_value:
            max_value = y

        x += step

    return max_value

print(max_value_of_function(0, 10))
