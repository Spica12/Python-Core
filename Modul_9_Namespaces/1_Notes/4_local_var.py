SOME_VAR = 3


def func(x):

    SOME_VAR = x

    print(f'func: {SOME_VAR = }')


def procedure():
    print(f'procedure: {SOME_VAR = }')


procedure()         # procedure: SOME_VAR = 3
func(5)             # func: SOME_VAR = 5
print(SOME_VAR)     # 3


