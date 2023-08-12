"""
Ваша компанія веде блог. Треба реалізувати функцію find_articles 
для пошуку за статтями цього блогу. Є список articles_dict, в 
якому міститься опис статей блогу. Кожен елемент цього списку є 
словником з наступними ключами: прізвища авторів - ключ 'author', 
назва статті - ключ 'title', рік видання - ключ 'year'.

Реалізуйте функцію find_articles,

Параметр key функції визначає поєднання букв для пошуку.
Наприклад, при key="Python" функція шукає, чи є у списку 
articles_dict статті, у назві чи іменах авторів яких зустрічається
це поєднання літер. Якщо такі елементи списку були знайдені, 
треба повернути новий список зі словників, що містять прізвища 
авторів, назву та рік видання всіх таких статей.

Другий ключовий параметр функції letter_case визначає, чи треба 
враховувати під час пошуку регістр літер. За умовчанням він 
дорівнює False і регістр немає значення тобто пошук в тексті 
"Python" і "python" це те ж саме. Інакше потрібно шукати повний 
збіг.
-------------------------------------
articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
"""
articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
        
    new_articles = []

    if not letter_case:
        key = key.lower()

    for article in articles_dict:
        
        title = article['title']
        author = article['author']
        year = article['year']

        if not letter_case:
            title = title.lower()
            author = author.lower()
        
        # print(f'\n{title = };\n {author = };\n {year = }')
        # print(f'{title.find(key) = }')
        # print(f'{author.find(key) = }')

        if title.find(key) >= 0 or author.find(key) >= 0:
            new_articles.append(article)

    return new_articles

first_article = find_articles(key='Ocean', letter_case=False)
print(f'{first_article = }\n')

second_article = find_articles(key='Ocean', letter_case=True)
print(f'{second_article = }\n')

