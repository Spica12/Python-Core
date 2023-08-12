print('--- capitalize(self, /) ---')#                capitalize()
# Перша буква строки з великої
some_string = 'hello hello'.capitalize()
print(some_string)  # Hello hello 



print('--- casefold(self, /) ---')#                casefold()
# Приводить до маленьких букв всі елементи
some_string = 'hello hello'.casefold()
print(some_string)  # hello hello



print('--------- center --------')#                center(self, width, fillchar='')
# Розмістити по центру строку, пустоти заповнити 
# знаком
some_string = 'hello hello'.center(30, '*')
print(some_string)  # *********hello hello**********



print('--------- count --------')#                count(...)
# порахувати кількість певного елементу в строці
some_string = 'hello hello'.count('l')
print(some_string)  # 4
# можна вказати зріз
print('hello'.count('l', 2)) # 2


print('--------- endswith --------')#                endswith(suffix, start, end)
# bool перевіритичи закінчується строка певним
some_string = 'hello hello'.endswith('lo')
print(some_string)  # True


print('--------- endswith --------')#                endswith(suffix, start, end)
# bool перевіритичи закінчується строка певним
some_string = 'hello hello'.endswith('lo')
print(some_string)  # True



print('------------------')#                find()
# Пошук у рядках
s = 'Hi there!'

start = 0
end = 7
print('0123456789', '9876543210', s, s.find('er', start, end), sep='\n') # 5
print(s.find('q'))  # -1

message = 'Hello my little friend!'

print(message.find('li', 5, 15))    # 9
print(message.find('li', 10, 15))   # -1
print(message.find('li'))           # 9



print('------------------')#                rfind()
s = 'Some words'

print('0123456789', '9876543210', s, s.rfind('o'), sep='\n') # 6



print('------------------')#                index()
print(s.index('e'))

message = 'Hello my little friend!'

print(message.index('li', 5, 15))    # 9
try:
    print(message.index('li', 10, 15))   # -1
except ValueError:
    print('VallueError')


print('------------------')#                rindex()
print(s.rindex('o'))



print('------------------')#                split()
# Розбиття рядка на підрядки за деяким символом
s = 'I am learning strings in Python. Some new methods got now'
sentences = s.split('. ')

print(sentences[0])     # I am learning strings in Python
print(sentences[1])     # Some new methods got now
print(s.split(' '))     # ['I', 'am', 'learning', 'strings', 'in', 'Python.', 'Some', 'new', 'methods', 'got', 'now']


print('------------------')#                join()
# Об'єднання двух рядків в один через роздільник
sentences = ['I am learning strings in Python', 'Some new words got now']
text = '. '.join(sentences)
print(text)     # I am learning strings in Python. Some new methods got now

words = ['I', 
          'am', 
          'learning', 
          'strings', 
          'in', 
          'Python.', 
          'Some', 
          'new', 
          'methods', 
          'got', 
          'now']

message_from_words = ' '.join(words)
print(message_from_words)   # I am learning strings in Python. Some new methods got now



print('------------------')#                strip()
# Видалення пробілів в рядку по обидва рядки
clean = '        spacious       '.strip()
print(clean) # spacious



print('------------------')#                lstrip()
# Видалення пробілів в рядку зліва
clean = '        spacious       '.lstrip()
print(clean) # spacious



print('------------------')#                rstrip()
# Видалення пробілів в рядку зліва
clean = '        spacious       '.rstrip()
print(clean) #         spacious



print('------------------')#                replace()
# Замінити дейякий підрядок в рядку
dogs_text = 'All dogs bark like dogs'
cats_text = dogs_text.replace('dogs', 'cats')
print(cats_text)    # All cats bark like cats

message = 'У темній кімнаті всі кішки чорні (мабуть)'
square_brackets = message.replace('(', '[').replace(')', ']')
clear_brackets = message.replace('(', '').replace(')', '')

print(square_brackets)  # У темній кімнаті всі кішки чорні [мабуть]
print(clear_brackets)   # У темній кімнаті всі кішки чорні мабуть


print('------------------')#                removepreffix()
# Видалення фіксованої послідовності на початку рядка
print('TestHook'.removeprefix('Test'))  # Hook
print('TestHook'.removeprefix('Hook'))  # TestHook



print('------------------')#                removesuffix()
# Видалення фіксованої послідовності в кінці рядка
print('TestHook'.removesuffix('Test'))  # TestHook
print('TestHook'.removesuffix('Hook'))  # Test



print('------------------')#                translate()
# Дозволяє замінити символ в рядку на інший з мапи відповідностей
map = {ord('з'): 'z', ord('ю'): 'u'}

translated = 'зю'.translate(map)
print(translated)   # zu

replace_dict = {117: 'o'}
txt = 'sun'
print(txt.translate(replace_dict))  # son



print('------------------')#                maketrans()
# створити таблицю відображення
txt = 'sun'
my_table = txt.maketrans('nus', 'mot')
print(my_table) # {110: 109, 117: 111, 115: 116}
print(txt.translate(my_table))  # tom

# Третій параметр видаяє елементи 
my_table = txt.maketrans('nu', 'mo', 's')
print(my_table) # {110: 109, 117: 111, 115: None}
print(txt.translate(my_table))  # om



print('------------------')#                zip()
CYRILLIC = ('а','ч', 'ш')
LATIN = ('a', 'ch', 'sh')

TRANSLIT_DICT = {}

for c, l in zip(CYRILLIC, LATIN):
    TRANSLIT_DICT[ord(c)] = l
    TRANSLIT_DICT[ord(c.upper())] = l.upper()

print('чаша'.translate(TRANSLIT_DICT))  # chasha
print('ЧАША'.translate(TRANSLIT_DICT))  # CHASHA


