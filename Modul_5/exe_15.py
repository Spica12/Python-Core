"""
І останнє завдання на регулярні висловлювання — це пошук у тексті гіперпосилань.

Напишіть регулярний вираз для функції find_all_links, яка буде в тексті 
(параметр text) знаходити всі лінки та повертати список отриманих з тексту збігів.

З метою спрощення приймемо, що:

- Початок гіперпосилання може бути http:// або https://
- доменне ім'я — це набір латинських букв, цифр, символів підкреслення _ та точок .
- символи точок . не можуть зустрічатися поруч

Фактично в навчальному прикладі ми шукатимемо прості url адреси:

https://www.google.com
https://www.facebook.com
https://github.com

Даний регулярний вираз жодною мірою не претендує на покриття всіх можливих 
варіантів гіперпосилань.

При виконанні цього завдання ми рекомендуємо використовувати наступний сервіс 
для перевірок регулярних виразів regex101.
----------------------------------------------------------------
import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r"", text)
    for match in iterator:
        result.append(match.group())
    return result
"""

import re


def find_all_links(text):
    result = []
    pattern = r"http[s]?://[a-zA-Z0-9_]+\.[^\.][a-zA-Z0-9_.]+"
    iterator = re.finditer(pattern, text)
    for match in iterator:
        result.append(match.group())
    return result

urls = 'The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com '
correct_urls = ['https://www.google.com', 'https://www.facebook.com', 'http://github.com']

print(find_all_links(urls))
print(correct_urls)