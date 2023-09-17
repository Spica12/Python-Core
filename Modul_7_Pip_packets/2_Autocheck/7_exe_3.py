"""
Продовжуємо модифікувати приклад. Для функції do_setup необхідно передбачити третій параметр, який буде словником, де ми можемо вказати список "точок входу" для ключа console_scripts.

Функція do_setup(args_dict, requires, entry_points) повинна викликати функцію setup з параметрами словника args_dict та параметром install_requires, який набуває значення requires. Третій параметр entry_points приймає словник, де ми можемо вказати список "точок входу" для ключа console_scripts.

Структура словника для параметра args_dicts має бути наступною

{
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}
"""
from setuptools import setup


def do_setup(args_dict, requires, entry_points):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires=requires,
          entry_points=entry_points
          )