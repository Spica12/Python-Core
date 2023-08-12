import re

"""
Є наприклад два рядки прикладів

url_query = "kolichestvo-osnovnih-kamer=3630926;producer=huawei;23777=6-6-5;38435=677049"
url_search = "q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"
Напишемо універсальну функцію get_object_parameters, яка повертатиме словник із даними. Оскільки в першому рядку розділити символ ;, а в другому &, тому тут вдало підійде випадок (a|b - відповідає a або b)
"""

url_query = "kolichestvo-osnovnih-kamer=3630926;producer=huawei;23777=6-6-5;38435=677049"
url_search = "q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"


def get_url_pararmetrs(url_query, pattern=r'&|;', key_split='='):
    object_dict = dict()

    # result = re.split(pattern, url_query)
    # for element in result:

    for element in re.split(pattern, url_query):
        key, value = element.split(key_split)
        object_dict.update({key: value.replace('+', ' ')})
    
    return object_dict


print(get_url_pararmetrs(url_query))    # {'kolichestvo-osnovnih-kamer': '3630926', 'producer': 'huawei', '23777': '6-6-5', '38435': '677049'}

print(get_url_pararmetrs(url_search))   # {'q': 'Cat and dog', 'ie': 'utf-8', 'oe': 'utf-8', 'aq': 't'}
                            
