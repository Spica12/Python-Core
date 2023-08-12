import re

# Regular expressions
# regexp

print('>--------------------------- re.search()')
# Шукає тільки першу відповідність заданій умові
s = 'I am 25 years old'
age = re.search('\d+', s)
print(f'{age = }') # age = <re.Match object; span=(5, 7), match='25'>
print(age.group(), '', sep='\n') # 25
print(age.span())   # (5, 7)
# print(age.string())



print('>--------------------------- re.findall()')
# Знайти всі відповідно шаблону значення
s = 'I bought 7 nuts for 6$ and 10 bolts for 3$'
numbers = re.findall('\d+', s)
print(numbers, '', sep='\n')  # ['7', '6', '10', '3']

print(re.findall("[0,1,3,6,7]", s))
# ['7', '6', '1', '0', '3']
print(re.findall("[^0,1,3,6,7]", s))
# ['I', ' ', 'b', 'o', 'u', 'g', 'h', 't', ' ', ' ', 'n', 'u',
#  't', 's', ' ', 'f', 'o', 'r', ' ', '$', ' ', 'a', 'n', 'd',
#  ' ', ' ', 'b', 'o', 'l', 't', 's', ' ', 'f', 'o', 'r', ' ',
#  '$']

# re.IGNORECASE - флаг нечутливості до регістру
word = 'pYtHON'
print(re.findall('Python', word)) # []
print(re.findall('Python', word, flags=re.IGNORECASE)) # ['pYtHON']


print('>--------------------------- re.sub()')
# Замінити всі підрядки, що відповідають
# регулярному виразу.
# Приклад, замінити кольори blue, red, white 
# на слово colour
text = 'blue socks and red shoes'
p = re.sub(r'(blue|while|red)', 'colour', text)
print(p, '', sep='\n')  # colour socks and colour shoes

print('>--------------------------- re.finditer()')
# re.finditer(pattern, string, flags=0)
regex = r'[a-zA-Z]{1}[\w\.]+@[a-zA-z]+\.[a-zA-Z]{2,}'

test_str = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net"

matches = re.finditer(regex, test_str)
for match in matches:
    print(f"{match.group()} start: {match.start()} end: {match.end()}")

# Складання регулярних виразів

# Складаються з блоків та модифікаторів
# Приклад
# [a,b,c,z]     у квадратні дужки беруть набір символів, з яких 
#               повинен складатися рядок
# [^a, b, c, z] символ ^ говорить про те що треба зробити поушк 
#               усіх символів алфавіту, крім заданих
# [a-c, z]      символ (-) говорить про діапазон символів, пошук 
#               яких треба зробити
# .     будь-який символ
# \d    число або [0-9]
# \D    не число, або [^0-9]
# \s    будь-який символ, позначає пробіл або табуляцію, 
#       перенесення 
#       рядка та ін.
# \w    будь-яке число або літера, включаючи нижнє підкреслення, 
#       або [a-zA-Z0-9_]
# \W    не літера, не число і не нижнє підкреслення
# \S    збігається із не пробільними символами
# \b    збіги шукатимуться лише на межах слів (на початку або в 
#       кінці)
# \B    збіги шукатимуться тільки не на межах слів
# \n    збігається із символами переводу рядка

# [?]   знайти мінімальну кількість, принцип "скряги"

# Модифікатори можуть вказувати на кількість повторень блоку у 
# виразі, наприклад:
# ? 0       або 1 раз
# + 1       або більше разів
# * 0       або більше разів
# {n}       суворо n разів (n ціле число)
# {n, m}    від n до m разів

#  ----------------- ---------------------------------------------
# |   Регулярка     | Її призначення                              |
#  ----------------- ---------------------------------------------
# |   simple text   | В точності текст "simple text"              |
# |      \d{5}      | Послідовність із 5 цифр \d означає будь-яку |
# |                 | цифру {5} - рівно 5 разів                   |
# | \d\d/\d\d/\d{4} | Дати в форматі ДД/ММ/РРРР (та інші шматки   |
# |                 | схожі на них, наприклад, 98/76/5432)        |
# |    \b\w{3}\b    | Слова в точності з трьох літер \b означає   |
# |                 | межу слова (з однією сторони літера, а з    |
# |                 | другої - ні) \w - будь-яка літера,          |
# |                 | {3} - рівно три рази                        |
# | [-+]?\d+        | Ціле число, наприклад 7, +17, -42, 0013     |
# |                 | (можливі провідні нулі) [-+]? - або -,      |
# |                 | або +, або порожньо \d+ - послідовність з   |
# |                 | 1 або більше цифр                           |
# | [-+]?(?:\d+     | .\d+)(?:[eE][-+]?\d+)?`                     |
# | (?:.\d*)?       |                                             |
#  ----------------- ---------------------------------------------






