# in - перевіряє чи входить щось в колекції
# 'строка' - це перша колекція яку ми знаємо


text = 'Hello world!'

if 'e' in text:
    print('Yes')
# Yes

if 'Hell' in text:
    print('Yes')
# Yes


if 'Hellz' in text:
    print('Yes')
else:
    print('No')
# No

if 1 in [1, 2, 3, 4]:
    print('1 in [1, 2, 3]')
# 1 in [1, 2, 3]
