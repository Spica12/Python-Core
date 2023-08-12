"""
У шостій задачі ми писали функцію is_spam_words, яка визначала, 
чи є чи ні стоп-слова у тексті повідомлення. Підемо далі та 
застосуємо функцію sub модуля re для заміни вказаних у списку 
стоп-слів на деякий шаблон. Наприклад, всі "погані" слова 
замінюватимемо зірочками. Напишіть функцію replace_spam_words, 
яка приймає рядок (параметр text), перевіряє його на вміст 
заборонених слів зі списку (параметр spam_words), та повертає 
результат рядок, але замість заборонених слів, підставлений 
шаблон з *, причому довжина шаблону дорівнює довжині забороненого 
слова. Визначити нечутливість до регістру стоп-слів.
--------------------------------------------
import re


def replace_spam_words(text, spam_words):
"""
import re


def replace_spam_words(text, spam_words):
    
    def repl(m):
        return '*' * len(m[0])

    spam_list = '|'.join(spam_words)

    text = re.sub(spam_list, repl, text, flags=re.IGNORECASE )

    return text

spam_words = ['began', 'Python']

text = 'Guido van Rossum began working on Python in the late'\
    ' 1980s, as a successor to the ABC programming PYTHOn'\
    ' language, and first released pYthoN it in 1991 as'\
    ' Python 0.9.0. pythOn '

print(replace_spam_words(text, spam_words))