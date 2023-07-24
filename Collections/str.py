# Використання "" та ''
game_string = 'My "Game"'

# Як звернутись до елемента
s = 'Hello world!'

print(s[0])         # H
print(s[-1])        # !

# Вносити зміни до рядку не можна. Не змінюваний тип
s = 'Hello world!'
#s[0] = Q # Викличе помилку

# Методи:
#                                               upper()
# Усі літери рядка перевести у верхній регістр
s = 'Hello world!'
s = s.upper()

print(s) # HELLO WORLD!

#                                               lower()
# Усі літери рядка перевести у нижній регістр
s = 'Hello World!'
s = s.lower() # hello world!

print(s)

#                                               startswith()
# Перевірити, що рядок починається з підрядка
s = 'Bill John'

print(s.startswith('Bi')) # True
print(s.startswith('Jo')) # False

#                                               endswith()
# Перевірити, що рядок закінчується підрядком
s = 'Hello World!'

print(s.endswith('ld!')) # True
print(s.endswith('ld')) # False

#                                               in
password = 'qwerty123'
if 'qwerty' in password or '123' in password:
    print('This password is too weak')

#                                               len
password = input('Password: ')
if len(password) < 8:
    print('Your password is too short')

#                                               for
alphabet = 'abcdefghiklmnoprstuvwxyz'
for char in alphabet:
    print(char)

#                                               title
# Символ кожного слова з великої букви
name = 'avril lavigne'
print(name.title()) # Avril Lavigne

#                                               rstrip
# Видалити пропуски біля ПРАВОГО краю
name = '               Avril Lavigne         '  
print(name.rstrip()) # Avril Lavigne

#                                               lstrip
# Видалити пропуски біля ЛІВОГО краю
name = '               Avril Lavigne         ' 
print(name.lstrip()) # Avril Lavigne

#                                               strip
# Видалити пропуски З ОБОХ БОКІВ
name = '               Avril Lavigne         ' 
print(name.strip()) # Avril Lavigne

#                                               strip
# Розбити строку на слова використовуючі пробіл
text = 'fsdf sdfsd dd d dfsdfj asdlqwe csvcxv'
words = text.split()
print(words)
