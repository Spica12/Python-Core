"""
Напишіть функцію find_word, яка приймає два параметри: перший 
text та другий word. Функція виконує пошук зазначеного слова word 
у тексті text за допомогою функції search та повертає словник.

При виклику функції:
print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))

Результат має бути наступного виду при збігу:

{
    'result': True,
    'first_index': 34,
    'last_index': 40,
    'search_string': 'Python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
}

де

result — результат пошуку True або False
first_index — початкова позиція збігу
last_index — кінцева позиція збігу
search_string — частина рядка, в якому був збіг
string — рядок, переданий у функцію

Якщо збігів не виявлено:
{
    'result': False,
    'first_index': None,
    'last_index': None,
    'search_string': 'python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
}

-------------------------------------------------
import re


def find_word(text, word):
"""
import re


def find_word(text, word):

    result_dict ={}
    
    value = re.search(word, text)

    result_dict['result'] = bool(re.search(word, text))
    result_dict['first_index'] = value.span()[0] if result_dict['result'] else None
    result_dict['last_index'] = value.span()[1] if result_dict['result'] else None
    result_dict['search_string'] = value.group() if result_dict['result'] else word
    result_dict['string'] = text
        

    return result_dict


print(find_word(
    "Guido van Rossum began working on Python in the late 1980s,"\
    " as a successor to the ABC programming language, and"\
    " first released it in 1991 as Python 0.9.0.",
    "Python"))