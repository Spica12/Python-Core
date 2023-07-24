# Створіть функцію parse_args, яка повертає рядок, складений з 
# аргументів командного рядка, розділених пробілами. 
# Наприклад, якщо скрипт був викликаний командою: python run.py 
# first second, то функція parse_args повинна повернути рядок 
# наступного виду 'first second'.
#  ---------------------------------------
# import sys


# def parse_args():
#     result = ""
    
        
            
        
#     return result
#  ------------------------------------------------
import sys


def parse_args():
    result = ""

    count = 0
    for arg in sys.argv:
        count += 1
        print(arg, count)

        if count == 1:
            continue
        elif count == 2:
            result += arg
        else:
            result += ' '
            result += arg
        
    return result

print(parse_args())