num = int(input('Введіть число (0 для виходу): '))

while num != 0:
    repeat = int(input('Скільки разів помножити число на 2? '))

    for i in range(repeat):
        num = num * 2
    print(num)
    
    num = int(input('Введіть число (0 для виходу): '))

