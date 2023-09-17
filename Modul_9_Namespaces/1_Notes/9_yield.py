# Yield

# yield - при наступному зверненні не розпочинає виконання функції з початку, а продовжує з місця зупинки

# next - необхідний для отриманння значення з такого генераторв

def interval_generator(x, y):

    while x <= y:
        yield x
        x += 1

five_to_ten_generator = interval_generator(5, 10)

next(five_to_ten_generator) # 5
next(five_to_ten_generator) # 6
next(five_to_ten_generator) # 7
next(five_to_ten_generator) # 8
next(five_to_ten_generator) # 9
next(five_to_ten_generator) # 10

five_to_ten_generator_second = interval_generator(5, 10)
for i in five_to_ten_generator_second:
    print(i)
