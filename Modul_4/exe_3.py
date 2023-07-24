# Ми розробляємо кулінарний блог. І в рецептах, при написанні 
# списку інгредієнтів, ми розділяємо їх комами, а перед останнім 
# ставимо союз "and", як у прикладі нижче:

# 2 eggs, 1 liter sugar, 1 tsp salt and vinegar

# Напишіть функцію format_ingredients, яка прийматиме на вхід 
# список з інгредієнтів ["2 eggs", "1 liter sugar", 
# "1 tsp salt", "vinegar"] та повертатиме рядок зібраний з 
# його елементів в описаний вище спосіб. Ваша функція має 
# вміти обробляти списки будь-якої довжини.
#  -----------------------------------------
# def format_ingredients(items):
# ------------------------------------------

def format_ingredients(items):

    ingridients = ''

    for item in items:

        ingridients += item

        if items.index(item) == len(items) - 2:
            ingridients += ' and '
        elif items.index(item) == len(items) - 1:
            break
        else:
            ingridients += ', '


    return ingridients


ingridients = format_ingredients(['2 eggs', '1 liter sugar', '1 tsp salt', 'vinegar'])
print(ingridients)