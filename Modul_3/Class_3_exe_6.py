# sum = 0

# for i in range(1, 10):
#     sum += i

# print(sum)


def factorial(n):
    
    return 1 if n < 2 else factorial(n-1) * n


def sum_inf(epsilon=0.0001):

    i = 1

    sum = pow(-1, i) / factorial(i + 1)

    while True:

        i += 1

        result = pow(-1, i) / factorial(i + 1)

        if abs(result) < epsilon:
            break
        
        sum += result

    return sum

print(sum_inf())
