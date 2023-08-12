import re

string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
         "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
         "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
         "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
         "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."


pattern = r'\b[A-Za-z]{2}'

pattern_one = r'\d{4}-\d{4}'
pattern_two = r'\d{4}-(\d{4})'
pattern_three = r'(\d{4})-(\d{4})'

print(re.findall(pattern_one, string)) 
print(re.findall(pattern_two, string))
print(re.findall(pattern_three, string))