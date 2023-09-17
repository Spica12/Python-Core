def decorator(func):

    def inner(*args, **kwargs):

        print('Before')
        result = func(*args, **kwargs)
        print('After')

        return result

    return inner

@decorator
def sum(iterable, func=sum):
    print('Custom sum')

    return func(iterable)

print(sum([1, 2, 3, 4, 5])) # 15

# Before
# Custom sum
# After
# 15
