import pickle


try:
    with open('12_theory_2_pickle.bin', 'rb') as f:
        animal_pickle = pickle.load(f)

    print(animal_pickle)

except SyntaxError as e:
    print(e)

# Traceback (most recent call last):
#   File "d:\GoIT\Python Core\Modul_12_Seralization_files\1_Theory\12_theory_3_continue_previos_file.py", line 5, in <module>
#     animal_pickle = pickle.load(f)
#                     ^^^^^^^^^^^^^^
# AttributeError: Can't get attribute 'Animal' on <module '__main__' from 'd:\\GoIT\\Python Core\\Modul_12_Seralization_files\\1_Theory\\12_theory_3_continue_previos_file.py'>


# Для цього треба просто зробити пустий класс Animal

class Animal:
    ...


try:
    with open('12_theory_2_pickle.bin', 'rb') as f:
        animal_pickle = pickle.load(f)

    print(animal_pickle)

except SyntaxError as e:
    print(e)