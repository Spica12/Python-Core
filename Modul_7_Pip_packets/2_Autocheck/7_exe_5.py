"""
Дуже часто люди у своїх повідомленнях не ставлять великі літери, 
особливо це стало масовим явищем в еру мобільних. пристроїв. Розробіть 
функцію capital_text, яка прийматиме на вхід рядок з текстом і 
повертатиме рядок з відновленими великими літерами.

Функція повинна:

зробити великою першу літеру в рядку, попри прогалини
зробити великою першу літеру після точки, попри прогалини
зробити великою першу літеру після знака оклику, попри прогалини
зробити великою першу літеру після знака питання, попри прогалини

---------------------------------------
def capital_text(s):
    

"""

def capital_text(s):
    new_text = ''

    is_capital = True

    for letter in s:

        if is_capital and letter != ' ':
            letter = letter.capitalize()
            is_capital = False
        
        if letter == '.' or letter == '!' or letter == '?':
             is_capital = True

        new_text += letter

    return new_text



text = ' my name is Vitalii. i am from Kyiv! what is your name? i understand.'
new_text = capital_text(text)

print(new_text)