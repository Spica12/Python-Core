"""
Напишіть функцію real_len, яка підраховує та повертає довжину 
рядка без наступних керівних символів: [\n, \f, \r, \t, \v]

Для перевірки правильності роботи функції real_len їй будуть 
передані наступні рядки:

'Alex\nKdfe23\t\f\v.\r'
'Al\nKdfe23\t\v.\r'
------------------------------------
def real_len(text):
"""
def real_len(text):
    
    len_text = 0

    for char in text:
        if '\n' in char or '\f' in char or '\r' in char or '\t' in char or '\v' in char:
            print(f'Not add: {char!r}' )
            continue
        print(char)
        len_text += 1

    return len_text

text = 'Alex\nKdfe23\t\f\v.\r'
result = real_len(text)
print(result)
print('----------------------')
text = 'Al\nKdfe23\t\v.\r'
result = real_len(text)
print(result)
