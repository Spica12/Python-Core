"""
Створіть функцію format_string для форматування рядка. У функцію 
ми передаємо рядок string та length довжину нового рядка. 
Функція повертає новий рядок за наступним алгоритмом:

1. Якщо довжина вихідного рядка більша або дорівнює length, ми 
   повертаємо його в тому ж вигляді;
2. Якщо вона менша length, ми додаємо попереду рядка пробіли в 
   кількості (length - len(string)) // 2.

Тести на правильність роботи функції виконуються для наступних 
наборів аргументів:
- string='aaaaaaaaaaaaaaaaac', length=12
- length=15, string='abaa'
"""
# def format_string(string, length):
# --------------------------------------------------------
def format_string(string, length):
    print('String', string, ', len=', len(string))
    print('Length', length)

    if len(string) >= length:
        print('if')
        return string
    else:
        print('else')
        spaces = ' ' * ((length - len(string) ) // 2)
        string = spaces + string
        return string
    
string = format_string(string='aaaaaaaaaaaaaaaaac', length=12)
print(string)

string = format_string(length=15, string='abaa')
print(string)