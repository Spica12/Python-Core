values = {1: 'one', 2: 'two',}


for key, value in values.items():
    print(key, value)

print('-----------------------------')

import re

string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
         "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
         "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
         "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
         "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

pattern = r'[0-9]+'

result = re.search(pattern, string)
print(result.span())
first_index, second_index = result.span()
print(first_index, second_index)
print(result.group())
print(result.string)

print('-----------------------------')

result = re.findall(pattern, string)
print(result)

print('-----------------------------')

pattern = r'\d+'

result = re.findall(pattern, string)
print(result)
