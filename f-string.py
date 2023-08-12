name = 'Vitalii'
string = f'Hello, {name}!!!'
print(string)

print('------------------')
str_value = 'other'
num_value = 123

print(f'the value is {str_value}')  # the value is other
print(f'{str_value = }')            # str_value = 'other'
print(f'{num_value % 2 = }')        # num_value % 2 = 1

print('------------------')
import datetime

def conversions():
    str_value = 'other 🐶'          # \U0001f436

    print(f'{str_value}')           # 'other 🐶'
    print(f'{str_value!s}')         # 'other 🐶'

    print(f'{str_value!a}')         # 'other \U0001f436'

    print(f'{str_value!r}')         # 'other 🐶'
    print(f'{repr(str_value)}')     # 'other 🐶'


conversions()

print('------------------')
def formatting():

    num_value = 123.456
    now = datetime.datetime.utcnow()
    print(f'{now = :%Y-%m-%d}')             # now = 2023-07-26
    print(f'{num_value:.2f}')               # 123.46

    nested_format = '.2f'                   # 123.46
    print(f'{num_value:{nested_format}}')


formatting()

print('------------------')

class MyClass:

    def __format__(self, format_spec) -> str:
        print(f'MyClass __format__ called with {format_spec=!r}')

        return 'MyClass()'

print(f'{MyClass():blah blah}')             # MyClass __format__ called with format_spec='blah blah'